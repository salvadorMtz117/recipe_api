from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql  = MySQL(app)


"""
*** Consulta banners de carrusel **
"""
def get_banners():
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT b.recipe_id,b.key_image,b.orden,r.name,r.short_description FROM te_banner b inner join tc_recipe r on (b.recipe_id = r.id)"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'banners': [], 'message':'No se encontraron registros', 'code':400})
        return jsonify({'banners': res, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'banners':[], 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Consulta categorias principales **
"""
def get_Categories():
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT id,name,description,key_image_1 FROM tc_type WHERE id IN (SELECT DISTINCT(type_id) FROM tc_recipe);"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'categorias': [], 'message':'No se encontraron registros', 'code':400})
        return jsonify({'categorias': res, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'categorias':[], 'message':'Error al realizar la operación', 'code':400})

"""
*** Consulta detalle de catogoría **
"""
def get_CategoryDetail(id):
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT description, key_image_1,name FROM tc_type WHERE id = '{0}';".format(id)
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'categoria': {}, 'message':'No se encontraron registros', 'code':400})
        return jsonify({'categoria': {'Detalle': res[0][0], 'img': res[0][1], 'Nombre': res[0][2]}, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'categoria':{}, 'message':'Error al realizar la operación', 'code':400})

"""
*** Consulta recetas principales **
"""
def get_Top_Recetas():
    try:
        cursor = mysql.connection.cursor()
        sql = "select id,name,ranking,key_image_1 from tc_recipe order by ranking desc limit 6"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'toprecetas': [], 'message':'No se encontraron registros', 'code':400})
        return jsonify({'toprecetas': res, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'toprecetas':[], 'message':'Error al realizar la operación', 'code':400})