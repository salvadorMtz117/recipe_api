from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql  = MySQL(app)


"""
*** Consulta todas las recetas **
"""
def get_all_recipes():
    try:
        cursor = mysql.connection.cursor()
        sql = 'SELECT id, name, short_description, long_description, ranking, type FROM tc_recipe'
        cursor.execute(sql)
        data = cursor.fetchall()
        recipes = []
        for item in data:
            recipe = {'id':item[0],'name':item[1],'short_description':item[2],'long_description':item[3],'ranking':item[4],'type':item[5]}
            recipes.append(recipe)
        return jsonify({'recetas':recipes, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        return jsonify({'recetas':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Consulta todas las recetas **
"""
def get_one_recipe(id):
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT id, name, short_description, long_description, ranking, type FROM tc_recipe WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        data = cursor.fetchall()
        if len(data) == 0:
            return jsonify({'recetas':{}, 'message':'Receta no encontrada', 'code':404})
        recipe = {'id':data[0][0],'name':data[0][1],'short_description':data[0][2],'long_description':data[0][3],'ranking':data[0][4],'type':data[0][5]}
        return jsonify({'recetas':recipe, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        return jsonify({'recetas':{}, 'message':'Error al realizar la operación', 'code':400})

"""
*** Actualiza una receta **
"""
def update_recipe(data):
    try:
        # Logica de Operación
        cursor = mysql.connection.cursor()
        sql = "UPDATE tc_recipe SET name = {0}, short_description = {1}, long_description = {2} , ranking = {3}, type = {4} WHERE id = {5};'".format(data.name,data.short_description,data.long_description,data.ranking,data.type,data.id)
        cursor.execute(sql)
        cursor.fetchall()
        return jsonify({'receta':{}, 'message':'Actualización exitosa', 'code':200})
    except Exception as ex:
        return jsonify({'receta':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Elimina una receta **
"""
def delete_recipe(id):
    try:
        # Logica de Operación
        cursor = mysql.connection.cursor()
        sql = "DELETE FROM tc_recipe WHERE id = {0}".format(id)
        cursor.execute(sql)
        cursor.fetchall()
        return jsonify({'receta':{}, 'message':'Borrado exitoso', 'code':200})
    except Exception as ex:
        return jsonify({'receta':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Inserta una receta **
"""
def insert_recipe(data):
    try:
        # Logica de Operación
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO tc_recipe(id,name,short_description,long_description,ranking,type) VALUES({0},{1},{2},{3},{4},{5})".format(data.id,data.name,data.short_description,data.long_description,data.ranking,data.type)
        cursor.execute(sql)
        cursor.fetchall()
        return jsonify({'receta':{}, 'message':'Inserción exitosa', 'code':200})
    except Exception as ex:
        return jsonify({'receta':{}, 'message':'Error al realizar la operación', 'code':400})
    

