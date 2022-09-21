from urllib import response
import mysql.connector
from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

mydb = mysql.connector.connect(
 host="192.168.0.177",
 user="root",
 password="123456",
 database="testepython"
)


def error_error():       
    return jsonify({"mensagem": "Não foi possível concluir a ação!"})



@app.route("/get", methods=["GET"])
def get():
  try: 
    sql="SELECT * FROM usuarios"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())



@app.route("/getOne/<id>", methods=["GET"])
def one(id):
  try:
    sql="SELECT * FROM usuarios WHERE id =" + id
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())



@app.route("/delete", methods=["DELETE"])
def delete():
  try:
    data = request.get_json()
    sql=f"DELETE FROM usuarios WHERE id ={data['id']}"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return ("Usuário Deletado com sucesso!")
  except Exception as ex:
    return (error_error()) 



@app.route("/create", methods=["POST"])
def create():
  try:
    data = request.get_json()
    sql=f"INSERT INTO usuarios (nome, email, senha, profissao) VALUES ('{data['nome']}', '{data['email']}','{data['senha']}', '{data['profissao']}')"
    mycursor = mydb.cursor().execute(sql)
    return ("Usuário criado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())



@app.route("/update", methods=["PUT"])
def update():
  try:
    data = request.get_json()
    sql=f"UPDATE usuarios SET nome='{data['nome']}', email='{data['email']}', senha='{data['senha']}', profissao='{data['profissao']}' WHERE id={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    return ("Usuário editado com sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


if __name__ == '__main__':
    app.run(DEBUG=True)
