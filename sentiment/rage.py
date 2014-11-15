import nltk
import nltk.classify.util

from nltk import tokenize
from nltk import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from collections import defaultdict

documents = defaultdict(list)


def word_feats(words):
    return dict([(word,True) for word in words])

neg_ids = movie_reviews.fileids('neg')
pos_ids = movie_reviews.fileids('pos')

neg_feats = [(word_feats(movie_reviews.words(fileids=[f])),'neg') for f in neg_ids]
pos_feats = [(word_feats(movie_reviews.words(fileids=[f])),'pos') for f in pos_ids]

#neg_feats.append(({'toxic':True, 'TOXIC':True},'neg'))


#neg_split = len(neg_feats)*9//10
#pos_split = len(pos_feats)*9//10

neg_split = len(neg_feats)
pos_split = len(pos_feats)

train_feats = neg_feats[:neg_split] + pos_feats[:pos_split]
test_feats = neg_feats[neg_split:] + pos_feats[pos_split:]
print ('train on %d instances, test on %d instances' % (len(train_feats), len(test_feats)))
 
classifier = NaiveBayesClassifier.train(train_feats)
print ('accuracy:', nltk.classify.util.accuracy(classifier, test_feats))
classifier.show_most_informative_features()
            


def getRage(string):
    result = classifier.prob_classify(word_feats(word_tokenize(string)))
    return result.prob('pos')

def getRageList(paragraph):
    sentences = tokenize.sent_tokenize(paragraph)

    sentences = [string.strip() for string in sentences if len(string.strip()) > 2]
    sentiments = []

    for sentence in sentences:
        sentiments.append(getRage(sentence))

    return (sentiments, sentences)

