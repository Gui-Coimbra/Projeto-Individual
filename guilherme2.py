from time import sleep
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import mysql.connector
from datetime import date

bdsql = mysql.connector.connect(host="localhost", user="aluno", password="sptech", database="airData", autocommit=True)

mycursor = bdsql.cursor()

while True:

    querry = "SELECT nome, max(porcentagemCpu) FROM processos WHERE DAY(horario) >= DAY(now()) GROUP BY nome ORDER BY max(porcentagemCpu) DESC LIMIT 10;"

    mycursor.execute(querry)

    resposta = mycursor.fetchall()

    processos = []
    for row in resposta:
        for row2 in range(0, int(row[1])):
            processos.append(str(row[0]))


    # print(processos)

    texto = " ".join(processos)

    word_cloud = WordCloud(collocations = False,
                        width=800, height=800,
                        background_color = 'white').generate(texto)

    plt.imshow(word_cloud)
    plt.axis("off")

    fig1 = plt.gcf()
    plt.show()

    fig1.savefig("site_institucional/public/assets/img/" + "wordcloudProcessos.png", dpi=100)

    sleep(1)