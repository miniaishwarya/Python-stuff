import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize,sent_tokenize

data = 'Hi there. I am Mini. '
print(word_tokenize(data))
print(sent_tokenize(data))
print(nltk.pos_tag(word_tokenize(data)))


