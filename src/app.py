from flask import Flask, request
from config import config
from flask_mysqldb import MySQL
from flask_cors import CORS

"""** Servicios **"""
from service import recipe_service as recipe
from service import user_service as user
from service import utils_service as utils
from service import pdfBuilder as builder

app = Flask(__name__)
mysql  = MySQL(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})

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

"""
    **** Consulta las recetas de una categoría ***
"""
@app.route('/recipe/RecipeByCategory', methods=['GET'])
def recipeByCategory():
    id = request.args['id']
    return recipe.get_Recetas_Categoria(id)

"""
    **** Genera el PDF de una receta (Base 64) ***
"""
@app.route('/recipe/GeneratePDFRecipe', methods=['GET'])
def generatePDFRecipe():
    id = request.args['id']
    return builder.build_pdf_recipe(id)


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


# **********************************************
# * Operaciones CRUD sobre UTILS  *
# **********************************************

"""
    **** Consulta banners de carrusel ***
"""
@app.route('/utils/GetCarrusel', methods=['GET'])
def getCarrusel():
    return utils.get_banners()

"""
    **** Consulta categorias principales ***
"""
@app.route('/utils/GetCategories', methods=['GET'])
def getCategories():
    return utils.get_Categories()

"""
    **** Consulta detalle de catogoría ***
"""
@app.route('/utils/GetCategoryDetail', methods=['GET'])
def getCategoryDetail():
    id = request.args['id']
    return utils.get_CategoryDetail(id)

"""
    **** Consulta recetas principales ***
"""
@app.route('/utils/TopRecetas', methods=['GET'])
def getTopRecetas():
    return utils.get_Top_Recetas()

# Función 404
def Notfound(error):
    return '<h1>Pagina no encontrada</h1>'

# Función principal de proyecto
if __name__ == '__main__':
    app.config.from_object(config['gcp'])
    app.register_error_handler(404, Notfound)
    app.run()


