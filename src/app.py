from flask import Flask, request
from config import config
from flask_mysqldb import MySQL

"""** Servicios **"""
from service import recipe_service as recipe

app = Flask(__name__)
mysql  = MySQL(app)

# **********************************************
# * Operaciones CRUD sobre registro de recetas *
# **********************************************

"""
    **** Método de consulta de recetas (GetAll) ***
"""
@app.route('/recipe/GetRecipes', methods=["GET"])
def listarRecetas():
    return recipe.get_all_recipes()

"""
    **** Método de consulta receta (GetOne) ***
"""
@app.route('/recipe/GetRecipe', methods=["GET"])
def consultaRecetas():
    id = request.args['id']
    return recipe.get_one_recipe(id)

"""
    **** Método de actualización de receta ***
"""
@app.route('/recipe/UpdateRecipe', methods=["PUT"])
def actualizarReceta():
    data = request.get_json()
    return recipe.update_recipe(data)

"""
    **** Método de borrado de una recetas ***
"""
@app.route('/recipe/DeleteRecipe', methods=['DELETE'])
def eliminarReceta():
    id = request.args['id']
    return recipe.delete_recipe(id)

"""
    **** Método de insertado de una receta ***
"""
@app.route('/recipe/InsertRecipe', methods=['POST'])
def insertarReceta():
    data = request.get_json()
    return recipe.insert_recipe(data)


# Función 404
def Notfound(error):
    return '<h1>Pagina no encontrada</h1>'

# Función principal de proyecto
if __name__ == '__main__':
    app.config.from_object(config['local'])
    app.register_error_handler(404, Notfound)
    app.run()


