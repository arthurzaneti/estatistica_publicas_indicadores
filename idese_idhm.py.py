import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#data organizing
data = {"Municípios": ["Tavares", "São Jerônimo", "Derrubadas", "Arroio Grande",
                       "Rio Pardo", "Salvador das Missões", "Encruzilhada do Sul", "Barra do Rio Azul",
                       "Coronel Bicaco", "Travesseiro", "Espumoso", "Arroio do Tigre", "Barracão", "Feliz",
                       "Faxinalzinho", "Nova Palma", "Casca", "São José do Hortêncio", "Novo Machado", "Panambi",
                       "Tupananci do Sul", "Salto do Jacuí", "Monte Alegre dos Campos", "Novo Tiradentes",
                       "Cachoeirinha","Linha Nova", "Ciriáco", "Três Arroios", "Pinheiro Machado", "São Sebastião do Caí",
                       "Barra Funda", "Entre Rios do Sul", "Nova Prata", "Paraíso do Sul", "Lajeado do Bugre"],
        "Idese": [0.613,0.658,0.654,0.612,0.635,0.774,0.621,0.730,0.638,0.772,0.729,0.663,0.711,
                  0.734,0.596,0.714,0.785,0.697,0.651,0.764,0.689,0.690,0.601,0.664,0.722,0.748,
                  0.686,0.799,0.596,0.679,0.786,0.780,0.788,0.589,0.596],
        "IDHM": [0.656,0.696,0.707,0.657,0.693,0.753, 0.657, 0.723, 0.665, 0.701, 0.765, 0.707, 0.710,
                 0.750, 0.666, 0.744, 0.785, 0.707, 0.663, 0.761, 0.694, 0.687, 0.650, 0.676,
                 0.757, 0.749, 0.719, 0.791, 0.661, 0.739, 0.763, 0.703, 0.766, 0.676, 0.613]}

df = pd.DataFrame(data)
df["Ranking Idese"] = df["Idese"].rank(method="dense", ascending=False).astype(int)
df["Ranking IDHM"] = df["IDHM"].rank(method="dense", ascending=False).astype(int)


#plotting
sns.set_theme(style = "ticks")

f,ax = plt.subplots(2,figsize = (8,6))
sns.despine(f)
plt.subplots_adjust(hspace = 0.8)
ticks_idese = np.linspace(df["Idese"].max(),df["Idese"].min(),8)
ticks_IDHM = np.linspace(df["IDHM"].max(),df["IDHM"].min(),8)

idese_histogram = sns.histplot(df, x="Idese",color = "#f6546a",edgecolor=".3",linewidth=.5,ax=ax[0],kde=True)
ax[0].set_xticks(np.linspace(df["Idese"].max(),df["Idese"].min(),8))
ax[0].set_yticks(range(2,11,2))
idese_std_dev = df["Idese"].std()

ax[0].axvline(df["Idese"].mean(), color="red", linestyle="-", linewidth=2)
ax[0].axvline(df["Idese"].mean() - idese_std_dev, color = "#590042",linestyle = "--", linewidth=2)
ax[0].axvline(df["Idese"].mean() + idese_std_dev, color = "#590042",linestyle = "--", linewidth=2)

sns.histplot(df, x="IDHM",color = "#6d1464",edgecolor=".3",linewidth=.5,ax=ax[1],kde=True)
ax[1].set_xticks(np.linspace(df["IDHM"].max(),df["IDHM"].min(),8))
ax[1].set_yticks(range(2,11,2))
IDHM_std_dev = df["IDHM"].std()

ax[1].axvline(df["IDHM"].mean(), color="red", linestyle="-", linewidth=2)
ax[1].axvline(df["IDHM"].mean() - IDHM_std_dev, color = "#590042",linestyle = "--", linewidth=2)
ax[1].axvline(df["IDHM"].mean() + IDHM_std_dev, color = "#590042",linestyle = "--", linewidth=2)
plt.show()

