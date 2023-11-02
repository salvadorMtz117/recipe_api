from flask import Flask, request
from config import config
from flask_mysqldb import MySQL

"""** Servicios **"""
from service import recipe_service as recipe
from service import user_service as user

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


# ***********************************************
# * Operaciones CRUD sobre registro de usuarios *
# ***********************************************
"""
    **** Método de consulta usuario ***
"""
@app.route('/user/GetUserAccess', methods=["POST"])
def getUserAccess():
    data = request.get_json()
    return user.get_access(data)

"""
    **** Método de creación de usuario ***
"""
@app.route('/user/CreateUser', methods=['POST'])
def createUser():
    data = request.get_json()
    return user.create_user(data)

"""
    **** Método de actualización de usuario ***
"""
@app.route('/user/UpdateUser', methods=['PUT'])
def updateUser():
    data = request.get_json()
    return user.update_user(data)

"""
    **** Método de actualización de usuario ***
"""
@app.route('/user/DeleteUser', methods=['DELETE'])
def deleteUser():
    id = request.args['id']
    return user.udelete_user(id)


# Función 404
def Notfound(error):
    return '<h1>Pagina no encontrada</h1>'

# Función principal de proyecto
if __name__ == '__main__':
    app.config.from_object(config['local'])
    app.register_error_handler(404, Notfound)
    app.run()


