from datetime import datetime
from time import sleep
from dashing import HSplit, VSplit, VGauge, HGauge, Text
import psutil
import os
import mysql.connector
import matplotlib.pyplot as plt

bdsql = mysql.connector.connect(host="localhost", user="root", password="sptech", database="processo", autocommit=True)

mycursor = bdsql.cursor()

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    lista_processos = []
    for processos in psutil.process_iter():
        # print(processos)
        processos_info = processos.as_dict(['name', 'cpu_percent', 'pid', 'username'])
        if processos_info['cpu_percent'] > 0:
            print(processos_info)
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
            
    # sql = "SELECT nome, max(porcentagemCpu) FROM processos WHERE fkServidor = 1 AND DAY(horario) >= DAY(now()) AND MINUTE(horario) >= MINUTE(now()) GROUP BY nome ORDER BY max(porcentagemCpu) DESC LIMIT 5"

    # mycursor.execute(sql)

    # resposta = mycursor.fetchall()
    
    # ordenados = []
    # for row in resposta:
    #     ordenados.append({'name': row[0], 'cpu_percent': row[1]})
        
    #for processos in ordenados:
        #print("-"*30)
        #print(processos)
        #print("-"*30)
        
    #sleep(5)    
    #limpar()
            
    #try:#testar um bloco de codigo
    #    # interface_usuario.display() #mostra a interface
    #    print()
    #    sleep(1) #espera 1 segundo para mostrar a proxima informação
    #except KeyboardInterrupt:
    #    break #encerra o loop ao pressionar Ctrl+C