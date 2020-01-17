import nltk
#from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
 
document = open("sampletext.txt","r")
data=document.read()
sentences = nltk.sent_tokenize(data)   
 
data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))
 
for word in data: 
    if 'NNP' in word[1]: 
        print(word)