import gensim
import os


print('vec')
model = gensim.models.KeyedVectors.load_word2vec_format('/home/lucas/Documentos/git/nlptp1/outs/A_Study_in_Scarlet_by_Arthur_Conan_Doyle.txt.txt', binary=False)
print(model.similarity('work', 'stood'))