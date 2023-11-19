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
        results = []
        steps = []
        ingredients = []
        comments = []
        recipeData = {}
        queries = [
            "SELECT r.id, r.name, r.short_description, r.long_description, r.ranking, r.type_id, r.key_image_1, t.description FROM tc_recipe r INNER JOIN tc_type t ON t.id = r.type_id WHERE r.id = '{0}'".format(id),
            "SELECT description FROM tc_steps WHERE recipe_id = {0};".format(id),
            "SELECT description FROM tc_ingredient WHERE recipe_id = {0};".format(id),
            "SELECT comment, date FROM tc_comment WHERE recipe_id = {0};".format(id),
        ]
        for query in queries:
            cursor.execute(query)
            data = cursor.fetchall()
            results.append(data)
        if len(results) == 0:
            return jsonify({'recetas':{}, 'message':'Receta no encontrada', 'code':404})
        recipeData['detail'] = {'id':results[0][0][0],'name':results[0][0][1],'short_description':results[0][0][2],'long_description':results[0][0][3],'ranking':results[0][0][4],'type':results[0][0][5], "key_img": results[0][0][6], "type_description": results[0][0][7]}
        for step in results[1]:
            steps.append(step[0])
        for ingredient in results[2]:
            ingredients.append(ingredient[0])
        for comment in results[3]:
            comments.append({'comment':comment[0], 'date':comment[1]})
        recipeData['steps'] = steps
        recipeData['ingredients'] = ingredients
        recipeData['comments'] = comments
        return jsonify({'receta':recipeData, 'message':'Consulta exitosa', 'code':200})
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
    
"""
*** Consulta las recetas de una categoría **
"""
def get_Recetas_Categoria(id):
    try:
        cursor = mysql.connection.cursor()
        sql = "select id,name,ranking,key_image_1,short_description from tc_recipe where type_id = '{0}' order by ranking desc".format(id)
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'recetas': [], 'message':'No se encontraron registros', 'code':400})
        return jsonify({'recetas': res, 'message':'Consulta exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'recetas':[], 'message':'Error al realizar la operación', 'code':400})
    

