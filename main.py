import streamlit as st 
import collections
import matplotlib.pyplot as plt

st.header("Frequenza delle parole in un testo")

uploaded_file = st.file_uploader("Seleziona un file di testo dal disco (Divina Commedia per default): ", accept_multiple_files=False, type=["txt", "py"])

if uploaded_file is None: 
    filename = 'divina.txt'
else: 
    filename = uploaded_file.name

# creazione del dizionario vuoto
dct_words = dict() 

# elaborazione del file
for line in open(filename, 'r'):
    line = line.lower().strip()
    
    # se la linea è vuota la salto
    if line == '':
        continue
    
    # trovo le parole
    words = line.split(' ')

    # per ogni parola
    # se la parola non è nel dizionario allora la inserisco col valore 1
    # altrimenti incremento il contatore
    for word in words:
        if word not in dct_words:
            dct_words[word] = 1
        else:
            dct_words[word] += 1

# creazione di un OrderedDict
dct_freq = collections.OrderedDict(sorted(dct_words.items(), key=lambda t: t[1], reverse=True))

number = st.slider('Quante parole vuoi visualizzare?', 3, 30)

# codice di Federico adattato per il mio caso, thanks Federico Barbieri!
# stampa del diagramma a barre
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.bar(list(dct_freq.keys())[:number],list(dct_freq.values())[:number])
ax.set_xlabel('Parole')
ax.tick_params(axis='x', labelrotation=90)
ax.set_ylabel('Frequenza')
st.pyplot(fig, number)
