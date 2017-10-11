import gensim
import os
import time
import numpy as np
from numpy import random


# lista de documentos
docs = [
'A-Christmas-Carol-in-Prose--Being-a-Ghost-Story-of-Christmas-by-Charles Dickens.txt',
'A-Doll-s-House---a-play-by-Henrik Ibsen.txt',
'Adventures of Huckleberry Finn by Mark Twain.txt',
'Alice-s Adventures in Wonderland by Lewis Carroll.txt',
'An Inquiry into the Nature and Causes of the Wealth of Nations by Adam Smith.txt',
'Anna Karenina by graf Leo Tolstoy.txt',
'Anne of Green Gables by L. M. Montgomery.txt',
'Around the World in Eighty Days by Jules Verne.txt',
'A_Study_in_Scarlet_by_Arthur_Conan_Doyle.txt',
'A-Tale-of-Two-Cities-by-Charles-Dickens.txt',
'Autobiography of Benjamin Franklin by Benjamin Franklin.txt',
'Beyond Good and Evil by Friedrich Wilhelm Nietzsche.txt',
'Candide by Voltaire.txt',
'Common Sense by Thomas Paine.txt',
'Crime and Punishment by Fyodor Dostoyevsky.txt',
'David Copperfield by Charles Dickens.txt',
'Don Quixote by Miguel de Cervantes Saavedra.txt',
'Dracula by Bram Stoker.txt',
'Emma by Jane Austen.txt',
'Frankenstein- Or, The Modern Prometheus by Mary Wollstonecraft Shelley.txt',
'Great Expectations by Charles Dickens.txt',
'Gulliver-s Travels into Several Remote Nations of the World by Jonathan Swift.txt',
'Jane Eyre- An Autobiography by Charlotte Bronte.txt',
'Les Miserables by Victor Hugo.txt',
'Leviathan by Thomas Hobbes.txt',
'Metamorphosis by Franz Kafka.txt',
'Moby Dick Or, The Whale by Herman Melville.txt',
'Oliver Twist by Charles Dickens.txt',
'Paradise Lost by John Milton.txt',
'Peter Pan by J. M. Barrie.txt',
'Pride and Prejudice by Jane Austen.txt',
'Pygmalion by Bernard Shaw.txt',
'Second Treatise of Government by John Locke.txt',
'Sense and Sensibility by Jane Austen.txt',
'Songs of Innocence, and Songs of Experience by William Blake.txt',
'The Adventures of Sherlock Holmes by Arthur Conan Doyle.txt',
'The Adventures of Tom Sawyer by Mark Twain.txt',
'The Brothers Karamazov by Fyodor Dostoyevsky.txt',
'The Complete Works of William Shakespeare by William Shakespeare.txt',
'The Count of Monte Cristo, Illustrated by Alexandre Dumas.txt',
'The Divine Comedy by Dante, Illustrated by Dante Alighieri.txt',
'The Hound of the Baskervilles by Arthur Conan Doyle.txt',
'The Iliad by Homer.txt',
'The Importance of Being Earnest- A Trivial Comedy for Serious People by Oscar Wilde.txt',
'The Jungle Book by Rudyard Kipling.txt',
'The King James Version of the Bible.txt',
'The Life and Adventures of Robinson Crusoe by Daniel Defoe.txt',
'The Mysterious Affair at Styles by Agatha Christie.txt',
'The Picture of Dorian Gray by Oscar Wilde.txt',
'The Prince by Niccolo Machiavelli.txt',
'The Republic by Plato.txt',
'The Return of Sherlock Holmes by Arthur Conan Doyle.txt',
'The Scarlet Letter by Nathaniel Hawthorne.txt',
'The Secret Adversary by Agatha Christie.txt',
'The Sign of the Four by Arthur Conan Doyle.txt',
'The Strange Case of Dr. Jekyll and Mr. Hyde by Robert Louis Stevenson.txt',
'The Time Machine by H. G. Wells.txt',
'The Tragedy of Romeo and Juliet by William Shakespeare.txt',
'The War of the Worlds by H. G. Wells.txt',
'The Wonderful Wizard of Oz by L. Frank Baum.txt',
'The Works of Edgar Allan Poe - Volume 1 by Edgar Allan Poe.txt',
'The Works of Edgar Allan Poe - Volume 2 by Edgar Allan Poe.txt',
'Three Men in a Boat by Jerome K. Jerome.txt',
'Through the Looking-Glass by Lewis Carroll.txt',
'Treasure Island by Robert Louis Stevenson.txt',
'Ulysses by James Joyce.txt',
'Utopia by Saint Thomas More.txt',
'Walden, and On The Duty Of Civil Disobedience by Henry David Thoreau.txt',
'War and Peace by graf Leo Tolstoy.txt',
'Wuthering Heights by Emily Bronte.txt']


print('Vec starting')

n = 0
for d in range(0, len(docs)):
    model = gensim.models.KeyedVectors.load_word2vec_format('/home/lucas/Documentos/git/nlptp1/outs/' + docs[d], binary=False)

    vocabs = []
    for item in model.wv.vocab.keys():
        vocabs.append(item)
        #print(vocabs)

    print(str(n) + " " + docs[d])
    n += 1
    #print(model.similarity('work', 'stood'))
    print(len(vocabs))
    #print(vocabs)
    random.seed(int(time.time()))
    rand = random.choice(vocabs, 300)
    #print(rand)
    #print(type(rand))
    #print(random.choice(docs, 3))

    for i in range(0, len(rand)):
        rand[i].encode("utf-8", 'ignore')

    #inicializa matriz
    mat_dist = [[0] * len(rand) for i in range(len(rand))]

    for i in range(0, len(rand)):
        for j in range(0, len(rand)):
            mat_dist[i][j] = model.similarity(rand[i], rand[j])
            #print('mat_dist[' + rand[i] + '][' + rand[j] + '] - ' + str(mat_dist[i][j]))
            #print(mat_dist[i][j])
            #print('{:4}'.format(mat_dist[i][j]))

    # Exibe a matriz
    #print(np.matrix(mat_dist))
    file = open('/home/lucas/Documentos/git/nlptp1/vecs/' + docs[d], 'w')
    #for item in vocabs:
    file.write(str(np.matrix(mat_dist)))
    file.close()

    np.savetxt('/home/lucas/Documentos/git/nlptp1/vecs/' + docs[d], mat_dist, fmt="%1.8f")

    #np.savetxt('/home/lucas/Documentos/git/nlptp1/minivoc/' + docs[d], rand, fmt=u"%s")
    file = open('/home/lucas/Documentos/git/nlptp1/minivoc/' + docs[d], 'w')
    for item in rand:
        file.write(item + '\n')
    file.close()


print("Ended")