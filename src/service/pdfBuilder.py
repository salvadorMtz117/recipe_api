from reportlab.platypus import Paragraph,Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from service import recipe_service as recipe
import json
import base64
import config as config

app = Flask(__name__)
mysql = MySQL(app)

def build_pdf_recipe(id):
    try:
        data = recipe.get_one_recipe(id).data
        data = json.loads(data.decode('utf-8'))  # Decodificar los bytes a una cadena y luego convertir la cadena JSON a un objeto Python
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        styles = getSampleStyleSheet()
        styles.wordWrap = 'LTR'

        # Dibujar los límites de la página
        width, height = letter
        p.rect(0, 0, width, height)
        counter = 0
        space = -250

        # Create a PDF document
        p.drawString(15, 750, f"{data.get('receta').get('detail').get('name')}") # Titulo
        y = 635
        p.drawImage(f"{config.S3Bucket.BUCKET_URL}{data.get('receta').get('detail').get('key_img')}", 15,y,200,100,None,True) # Imagen
        y = y - 20
        frame = Frame(15, -60, width-100, height-100, showBoundary=0)
        story = [Paragraph(data.get('receta').get('detail').get('long_description'), styles['Normal'])]
        frame.addFromList(story, p)
        y = y - 40
        p.drawString(15, y, f"Ingredientes:")
        for row in data.get('receta').get('ingredients'):
            y = y - 15
            p.drawString(15, y, f"- {row}")
        y = y - 30
        p.drawString(15, y, f"Pasos para preparación:")
        for row in data.get('receta').get('steps'):
            counter += 1
            space -= 25
            frame = Frame(15, space, width-100, height-100, showBoundary=0)
            story = [Paragraph(f"{counter}.- {row}", styles['Normal'])]
            frame.addFromList(story, p)

        p.showPage()
        p.save()
    
        buffer.seek(0)
        base64_pdf = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        return jsonify({'pdf': base64_pdf, 'message': 'Consulta exitosa', 'code': 200})
    except Exception as ex:
        print(ex)
        return jsonify({'recetas': {}, 'message': 'Error al realizar la operación', 'code': 400})