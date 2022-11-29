from random import sample
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import mysql.connector
import psutil

bdsql = mysql.connector.connect(host="localhost", user="root", password="sptech", database="airData", autocommit=True)

mycursor = bdsql.cursor()

querry = "SELECT nome, max(porcentagemCpu) FROM processos WHERE DAY(horario) >= DAY(now()) GROUP BY nome, pid, usuario ORDER BY max(porcentagemCpu) DESC LIMIT 10;"

mycursor.execute(querry)

resposta = mycursor.fetchall()

ocorrencias = []
for row in resposta:
    ocorrencias.append([str(row[0])] * int(row[1]))

# ocorrencias = ["dashboard_não_aparece"] * 60 + ["dashboard_travado "] * 160 + ["temperatura_elevada"] * 120 + ["cpu_consumo_elevado"] * 80 + ["aplicação_lenta"] * 100 + ["upload_lento"] * 60 + ["download_lento"] * 20 + ["memoria_cheia"] * 20 + ["alerta_dispara"] * 20 + ["dados_incorretos"] * 20 + ["disco_consumo_elevado"] * 20 + ["usuario_não_pode_ser_cadastrado"] * 40 + ["maquina_não_pode_ser_cadastrada"] * 20 + ["login_não_funciona"] * 20

print(ocorrencias)

# amostra = sample(ocorrencias, 300)

texto = " ".join(ocorrencias)

# mask = np.array(Image.open("cloud.png"))
# word_cloud = WordCloud(collocations = False, background_color = 'black', mask=mask, contour_color='white', contour_width=3).generate(texto)


# plt.imshow(word_cloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

word_cloud = WordCloud(collocations = False, background_color = 'black').generate(texto)

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()