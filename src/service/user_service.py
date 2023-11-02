from flask import Flask, jsonify
from flask_mysqldb import MySQL

import utils.cripto as cripto

app = Flask(__name__)
mysql  = MySQL(app)

"""
*** Crea un usuario **
"""
def create_user(data):
    try:
        cursor = mysql.connection.cursor()
        # Valida que los datos no esten vacios
        if data['name'] == '' or data['surname'] == '' or data['last_name'] == '' or data['email'] == '' or data['password'] == '' or data['age'] == '' or data['bithday'] == '':
            return jsonify({'user': {}, 'message':'Todos los datos son obligatorios', 'code':400})
        # Valida que el email no este registrado
        sqlGet = "SELECT email FROM tc_user WHERE email = '{0}'".format(data['email'])
        cursor.execute(sqlGet)
        res = cursor.fetchall()
        if len(res) > 0:
            return jsonify({'user': {}, 'message':'El email ya se encuentra registrado', 'code':400})
        # Realiza inserción
        stringCripto = cripto.Crypt.encrypt(data['password'])
        sql = "INSERT INTO tc_user (name, surname, last_name, email, password, age, birthday) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (data['name'], data['surname'], data['last_name'], data['email'], stringCripto, data['age'], data['bithday'])
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.fetchall()
        return jsonify({'user': {},'token': '', 'message':'Inserción exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'user':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Acceso de usuario **
"""
def get_access(data):
    try:
        cursor = mysql.connection.cursor()
        # Valida que los datos no esten vacios
        if data['email'] == '' or data['password'] == '':
            return jsonify({'user': {}, 'message':'Todos los datos son obligatorios', 'code':400})
        # Valida que el email no este registrado
        sqlGet = "SELECT email,password,name,surname,last_name,age,birthday,id FROM tc_user WHERE email = '{0}'".format(data['email'])
        cursor.execute(sqlGet)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'user': {}, 'message':'Usuario o contraseña incorrectos', 'code':400})
        # Realiza login
        if res[0][1] != cripto.Crypt.encrypt(data['password']):
            return jsonify({'user': {}, 'message':'Usuario o contraseña incorrectos', 'code':400})
        user = {'email':res[0][0],'name': res[0][2],'surname': res[0][3],'last_name': res[0][4],'age': res[0][5],'birthday': res[0][6],'id': res[0][7]}
        return jsonify({'user': user,'token': '', 'message':'Acceso exitoso', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'user':{}, 'message':'Error al realizar la operación', 'code':400})

"""
*** Actualiza un usuario **
"""
def update_user(data):
    try:
        cursor = mysql.connection.cursor()
        # Valida que los datos no esten vacios
        if data['name'] == '' or data['surname'] == '' or data['last_name'] == '' or data['email'] == '' or data['password'] == '' or data['age'] == '' or data['birthday'] == '':
            return jsonify({'user': {}, 'message':'Todos los datos son obligatorios', 'code':400})
        # Valida que el usuario exista
        sqlGet = "SELECT id,email FROM tc_user WHERE id = '{0}'".format(data['id'])
        cursor.execute(sqlGet)
        res = cursor.fetchall()
        if len(res) == 0:
            return jsonify({'receta':{}, 'message':'Usuario no encontrado', 'code':404})
        # Valida que el email no este registrado
        if res[0][1] != data['email']:
            sqlGet = "SELECT email FROM tc_user WHERE email = '{0}'".format(data['email'])
            cursor.execute(sqlGet)
            res = cursor.fetchall()
            if len(res) > 0:
                return jsonify({'user': {}, 'message':'El email ya se encuentra registrado', 'code':400})
        # Realiza actualización
        stringCripto = cripto.Crypt.encrypt(data['password'])
        sql = "UPDATE tc_user SET name = %s, surname = %s, last_name = %s, email = %s, password = %s, age = %s, birthday = %s WHERE id = %s"
        values = (data['name'], data['surname'], data['last_name'], data['email'], stringCripto, data['age'], data['birthday'], data['id'])
        cursor.execute(sql,values)
        mysql.connection.commit()
        cursor.fetchall()
        return jsonify({'user':data, 'message':'Actualización exitosa', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'user':{}, 'message':'Error al realizar la operación', 'code':400})
    
"""
*** Elimina una receta **
"""
def udelete_user(id):
    try:
        # Logica de Operación
        cursor = mysql.connection.cursor()
        sqlGet = "SELECT id FROM tc_user WHERE id = '{0}'".format(id)
        cursor.execute(sqlGet)
        data = cursor.fetchall()
        if len(data) == 0:
            return jsonify({'receta':{}, 'message':'Usuario no encontrado', 'code':404})
        else: 
            sql = "DELETE FROM tc_user WHERE id = {0}".format(id)
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.fetchall()
            return jsonify({'user':{}, 'message':'Borrado exitoso', 'code':200})
    except Exception as ex:
        print(ex)
        return jsonify({'user':{}, 'message':'Error al realizar la operación', 'code':400})
    