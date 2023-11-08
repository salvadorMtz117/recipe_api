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
        sql = "select name,description,key_image_1 from tc_type where id in (3,8,11)"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'categorias': [], 'message':'No se encontraron registros', 'code':400})
        return jsonify({'categorias': res, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'categorias':[], 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Consulta categorias principales **
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