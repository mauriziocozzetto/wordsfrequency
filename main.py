
import streamlit as st 
import collections
import matplotlib.pyplot as plt
from pathlib import Path
from textblob import TextBlob
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd

number = 3

st.header("Frequenza delle parole in un testo")

# file da caricare
uploaded_file = st.file_uploader("Seleziona un file txt dal disco:", accept_multiple_files=False, type=["txt"])
# tipo UploadedFile

# l'utente sceglie il numero
number = st.slider('Quante parole vuoi visualizzare?', number, 30)

if not uploaded_file: 
    st.stop()

# creo il blob
blob = TextBlob(Path(uploaded_file.name).read_text())

# scelgo le stopwords della lingua inglese
stop_words = stopwords.words('english')

# conto le parole
items = blob.word_counts.items()

# tolgo le stopwords
items = [item for item in items if item[0] not in stop_words] # items senza le stop words

# ordino la lista
sorted_items = sorted(items, key=itemgetter(1), reverse=True) # (__,__) il primo elemento è la parola, il secondo elemento è la frequennza: itemgetter(1)
print(sorted_items)


#if not number:
#    st.stop() 

# st.write(number)
top = sorted_items[1:number + 1]

# dataframe
df = pd.DataFrame(top, columns=['Words', 'Frequencies'])  
print('df=', df)
print('df words =', list(df['Words']))
print('df frequencies =', list(df['Frequencies']))

# disegno il diagramma
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.bar(list(df['Words'])[:number],df['Frequencies'][:number])
ax.set_xlabel('Parole')
ax.tick_params(axis='x', labelrotation=90)
ax.set_ylabel('Frequenze')
st.pyplot(fig, number)


