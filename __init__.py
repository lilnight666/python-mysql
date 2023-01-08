from datetime import datetime
import _mysql_connector
import mysql.connector

db_connection = mysql.connector.Connect(host="localhost", user="root", passwd="", database="cadastrotrabaia")
cursor = db_connection.cursor()
dados = dict()
dados['nome'] = str(input("digite o nome do funcionario "))
nasc = int(input("ano de nascimento"))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("caterira de trabalho(digite 0 se não tiver:"))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contaratação'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

sql = (f"""INSERT INTO pessoas(nome,idade,ctps,aposentadoria,contratação) 
VALUES ('{dados['nome']}','{dados['idade']}','{dados['ctps']}','{dados['aposentadoria']}','{dados['contratação']}')""")
cursor.execute(sql)
cursor.close()
db_connection.commit()
db_connection.close()
