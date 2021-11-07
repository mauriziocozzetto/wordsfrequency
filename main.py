import streamlit as st 
import collections
import matplotlib.pyplot as plt
from io import StringIO

st.header("Frequenza delle parole in un testo")

uploaded_file = st.file_uploader("Seleziona un file txt dal disco:", accept_multiple_files=False, type=["txt"])

if uploaded_file is None: 
    #filename = 'divina.txt'
    st.stop()

stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))

# creazione del dizionario vuoto
dct_words = dict() 

# elaborazione del file
for line in stringio:
    line = line.lower().strip()

    # se è vuota la salto
    if line == '':
        continue
    
    words = line.split(' ')

    for word in words:
        if word not in dct_words:
            dct_words[word] = 1
        else:
            dct_words[word] += 1

# creazione di un OrderedDict
dct_freq = collections.OrderedDict(sorted(dct_words.items(), key=lambda t: t[1], reverse=True))

number = st.slider('Quante parole vuoi visualizzare?', 3, 30)

# stampa del diagramma a barre
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.bar(list(dct_freq.keys())[:number],list(dct_freq.values())[:number])
ax.set_xlabel('Parole')
ax.tick_params(axis='x', labelrotation=90)
ax.set_ylabel('Frequenza')
st.pyplot(fig, number)
