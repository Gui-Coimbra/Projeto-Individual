from datetime import datetime
from time import sleep
from dashing import HSplit, VSplit, VGauge, HGauge, Text
import psutil
import os
import mysql.connector
import matplotlib.pyplot as plt

bdsql = mysql.connector.connect(host="localhost", user="root", password="sptech", database="teste")

mycursor = bdsql.cursor()

interface_usuario = HSplit(  # Aqui tem a interface do usuario onde HSPLIT é a divisão horizontal e VSPLIT é a divisão vertical
    VSplit( # interface_usuario.items[0]
        Text( # interface_usuario.items[0].items[0]
            ' ',
            border_color=9, # cor da borda
            color=4, # cor do texto
            title='Processos' # titulo
        ),
        HSplit(  # interface_usuario.items[0].items[1]
            VGauge(title='RAM'),  # interface_usuario.items[0].items[0] - RAM - VGauge é um medidor vertical
            VGauge(title='SWAP'),  # interface_usuario.items[0].items[1], Onde items[0] é o primeiro item e items[1] é o segundo item da divisão horizontal
            title='Memória',
            border_color=3
        ),
    ),
    VSplit(  # interface_usuario.items[1]
        HGauge(title='CPU %'),
        HGauge(title='CPU_0'),
        HGauge(title='CPU_1'),
        HGauge(title='CPU_2'),
        HGauge(title='CPU_3'),
        HGauge(title='CPU_4'),
        HGauge(title='CPU_5'),
        HGauge(title='CPU_6'),
        HGauge(title='CPU_7'),
        title='CPU',
        color=4,
        border_color=5,
    ),
    VSplit(  # interface_usuario.items[2]
        Text(
            ' ',
            title='Outros',
            color=4,
            border_color=4
        ),
        Text(
            ' ',
            title='Disco',
            color=4,
            border_color=6
        ),
        Text(
            ' ',
            title='Rede',
            color=4,
            border_color=7
        ),
    ),
)

while True:
    #processos_tui = interface_usuario.items[0].items[0] # tui é terminal user interface
    lista_processos = []
    for processos in psutil.process_iter():
        processos_info = processos.as_dict(['name', 'cpu_percent'])
        if processos_info['cpu_percent'] > 0:
            lista_processos.append(processos_info)
            nome = processos_info['name']
            porcentagemProcesso = processos_info['cpu_percent'] 
            sql = "INSERT INTO processos(nome, porcentagemCpu, fkServidor, horario) VALUES(%s, %s, %s, now())"
            val = (nome, porcentagemProcesso, 1, )
            mycursor.execute(sql, val)

            bdsql.commit()
            
    try:#testar um bloco de codigo
        interface_usuario.display() #mostra a interface
        sleep(1) #espera 1 segundo para mostrar a proxima informação
    except KeyboardInterrupt:
        break #encerra o loop ao pressionar Ctrl+C