from datetime import datetime
from time import sleep
import psutil
import os
from sys import platform
import mysql.connector
import matplotlib.pyplot as plt

bdsql = mysql.connector.connect(host="localhost", user="aluno", password="sptech", database="airData", autocommit=True)

mycursor = bdsql.cursor()

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def matarProcesso(pid):
    if platform == "linux" or platform == "linux2":
        os.system('kill '+str(pid))
    elif platform == "win32":
        os.system('TASKKILL /PID ' + str(pid) + ' /F')

while True:
    lista_processos = []
    for processos in psutil.process_iter():
        # print(processos)
        processos_info = processos.as_dict(['name', 'cpu_percent', 'pid', 'username'])
        if processos_info['cpu_percent'] > 0:
            # print(processos_info)
            lista_processos.append(processos_info)
            pid = processos_info['pid']
            usuario = processos_info['username']
            nome = processos_info['name']
            porcentagemProcesso = processos_info['cpu_percent'] 
            sql = "INSERT INTO processos(nome, porcentagemCpu, pid, usuario, fkServidor, horario) VALUES(%s, %s, %s, %s, %s, now())"
            val = (nome, porcentagemProcesso, pid, usuario, 1)
            mycursor.execute(sql, val)

            bdsql.commit()
            sleep(1)
            print("Executando...")
            
        sql = "select * from deletarPid;"

        mycursor.execute(sql)

        resposta = mycursor.fetchall()

        if(len(resposta) > 0):

            for row in resposta:
                pid = row[1]
                matarProcesso(pid)
                sql = "delete from deletarPid where pid = %s;"
                val = (pid, )
                mycursor.execute(sql,val)
                sql = "delete from processos where pid = %s;"
                val = (pid, )
                mycursor.execute(sql,val)
                bdsql.commit()
                sleep(1)