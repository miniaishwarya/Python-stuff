import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize,sent_tokenize
from collections import Counter

with open("sampletext.txt","r") as file:          # easy way to open a file. no close statement required
    data_file=file.read()

#print(data_file)

data_file_sentences = sent_tokenize(data_file) #creates a list of sentences separated by '\n'
#print(data_file_sentences)
#print(len(data_file_sentences))

data_file_single_sentence=[]

for line in data_file_sentences:      # for each sentence, create another list consisting of only words.
    #processed_line = line             # creates a 2 dimensional list
    data_file_single_sentence.append(word_tokenize(line))

#print(data_file_single_sentence)

postaggedlines=[]
l=len(data_file_single_sentence)

for i in range(0,l-1):
    postaggedlines.append(nltk.pos_tag(data_file_single_sentence[i]))   

#print(postaggedlines) 
#print(postaggedlines[1][1][1])
#le=len(postaggedlines[])

parts_of_speech={
    'NN':[],
    'NNS':[],
    'NNP':[],
    'NNPS':[]
}

count=0

for i in range(0,l-1):
    for j in range(0,len(postaggedlines[i])-1):
        tuples= tuple(postaggedlines[i][j])
        if tuples[1] == 'NN':
            parts_of_speech['NN'].append(tuples[0])
        elif tuples[1] == 'NNS':
            parts_of_speech['NNS'].append(tuples[0])
        elif tuples[1] == 'NNP':
            parts_of_speech['NNP'].append(tuples[0])
        elif tuples[1] == 'NNPS':
            parts_of_speech['NNPS'].append(tuples[0])
        else:
            pass

all_list=[]

for values in parts_of_speech.values():
    all_list = all_list + values

#print(all_list)                            # list of all nouns
print('Top 5 frequently used nouns are: ')
print(Counter(all_list).most_common(5))











