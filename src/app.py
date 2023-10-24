from flask import Flask, jsonify
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)
conexion = MySQL(app)


# Servicio de consulta de recetas
@app.route('/ConsultRecipe')
def listarRecetas():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT id, name, type FROM tc_recipe'
        cursor.execute(sql)
        data = cursor.fetchall()
        recipes = []
        for item in data:
            recipe = {'id':item[0], 'name':item[1], 'type':item[2]}
            recipes.append(recipe)
        return jsonify({'recetas':recipes, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        return jsonify({'recetas':{}, 'message':'Error al realizar la operación', 'code':400})


def Notfound(error):
    return '<h1>Pagina no encontrada</h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, Notfound)
    app.run()

