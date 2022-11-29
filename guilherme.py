from random import sample
import matplotlib.pyplot as plt
from wordcloud import WordCloud

ocorrencias = ["dashboard_não_aparece"] * 60 + ["dashboard_travado "] * 160 + ["temperatura_elevada"] * 120 + ["cpu_consumo_elevado"] * 80 + ["aplicação_lenta"] * 100 + ["upload_lento"] * 60 + ["download_lento"] * 20 + ["memoria_cheia"] * 20 + ["alerta_dispara"] * 20 + ["dados_incorretos"] * 20 + ["disco_consumo_elevado"] * 20 + ["usuario_não_pode_ser_cadastrado"] * 40 + ["maquina_não_pode_ser_cadastrada"] * 20 + ["login_não_funciona"] * 20

print(ocorrencias)

# amostra = sample(ocorrencias, 300)

# texto = " ".join(amostra)

# word_cloud = WordCloud(collocations = False, background_color = 'white').generate(texto)

# plt.imshow(word_cloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()