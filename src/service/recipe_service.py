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
        sql = 'SELECT id, name, short_description, long_description, ranking, type_id FROM tc_recipe'
        cursor.execute(sql)
        data = cursor.fetchall()
        recipes = []
        for item in data:
            recipe = {'id':item[0],'name':item[1],'short_description':item[2],'long_description':item[3],'ranking':item[4],'type':item[5]}
            recipes.append(recipe)
        return jsonify({'recetas':recipes, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'recetas':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Consulta una receta **
"""
def get_one_recipe(id):
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT id, name, short_description, long_description, ranking, type_id FROM tc_recipe WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        if len(data) == 0:
            return jsonify({'recetas':{}, 'message':'Receta no encontrada', 'code':404})
        recipe = {'id':data[0][0],'name':data[0][1],'short_description':data[0][2],'long_description':data[0][3],'ranking':data[0][4],'type':data[0][5]}
        return jsonify({'recetas':recipe, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'recetas':{}, 'message':'Error al realizar la operación', 'code':400})

"""
*** Actualiza una receta **
"""
def update_recipe(data):
    try:
        # Logica de Operación
        cursor = mysql.connection.cursor()
        sqlGet = "SELECT id FROM tc_recipe WHERE id = '{0}'".format(data['id'])
        cursor.execute(sqlGet)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'receta':{}, 'message':'Receta no encontrada', 'code':404})
        else : 
            sql = "UPDATE tc_recipe SET name = %s, short_description = %s, long_description = %s, ranking = %s, type_id = %s WHERE id = %s"
            values = (data['name'], data['short_description'], data['long_description'], data['ranking'], data['type'], data['id'])
            cursor.execute(sql,values)
            mysql.connection.commit()
            cursor.fetchall()
            return jsonify({'receta':{}, 'message':'Actualización exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'receta':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Elimina una receta **
"""
def delete_recipe(id):
    try:
        # Logica de Operación
        cursor = mysql.connection.cursor()
        sqlGet = "SELECT id FROM tc_recipe WHERE id = '{0}'".format(id)
        cursor.execute(sqlGet)
        data = cursor.fetchall()
        if len(data) == 0:
            return jsonify({'receta':{}, 'message':'Receta no encontrada', 'code':404})
        else: 
            sql = "DELETE FROM tc_recipe WHERE id = {0}".format(id)
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.fetchall()
            return jsonify({'receta':{}, 'message':'Borrado exitoso', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'receta':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Inserta una receta **
"""
def insert_recipe(data):
    try:
        # Logica de Operación
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO tc_recipe (name, short_description, long_description, ranking, type_id) VALUES (%s, %s, %s, %s, %s)"
        values = (data['name'], data['short_description'], data['long_description'], data['ranking'], data['type'])
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.fetchall()
        return jsonify({'receta':{}, 'message':'Inserción exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'receta':{}, 'message':'Error al realizar la operación', 'code':400})
    

