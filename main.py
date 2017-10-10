import gensim
import os


print("Starting...")

class MySentences(object):
    def __init__(self, dirname, name):
        self.dirname = dirname
        self.name = name
 
    def __iter__(self):
        for line in open(os.path.join(self.dirname, self.name)):
            yield line.split()
 
sentences = MySentences('~/Documents/git/nlptp1/docs', 'Candide by Voltaire.txt') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences, iter=15)
model.wv.save_word2vec_format('~/Documents/git/nlptp1/outs/voltaire', binary=False)