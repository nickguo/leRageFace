import nltk
import nltk.classify.util

from nltk.corpus import names

from nltk import tokenize
from nltk import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from collections import defaultdict
import random



# POS / NEG STUFF
def word_feats(words):
    return dict([(word,True) for word in words])

neg_ids = movie_reviews.fileids('neg')
pos_ids = movie_reviews.fileids('pos')

neg_feats = [(word_feats(movie_reviews.words(fileids=[f])),'neg') for f in neg_ids]
pos_feats = [(word_feats(movie_reviews.words(fileids=[f])),'pos') for f in pos_ids]

neg_split = len(neg_feats)
pos_split = len(pos_feats)

train_feats = neg_feats[:neg_split] + pos_feats[:pos_split]
test_feats = neg_feats[neg_split:] + pos_feats[pos_split:]
print ('train on %d instances, test on %d instances' % (len(train_feats), len(test_feats)))
 
classifier = NaiveBayesClassifier.train(train_feats)
print ('accuracy:', nltk.classify.util.accuracy(classifier, test_feats))
classifier.show_most_informative_features()


# NAME STUFF
def gender_features(word):
    return {'last_letter':word[-1]}

labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')])

train_set = [(gender_features(n), gender) for (n,gender) in labeled_names]
print ("training sex")
sex_classifier = nltk.NaiveBayesClassifier.train(train_set)
print ("done training sex")


all_names = [name.lower() for name in names.words('male.txt')]
all_names.extend([name.lower() for name in names.words('female.txt')])
all_names.extend([name for name in names.words('female.txt')])
all_names.extend([name for name in names.words('male.txt')])

try:
    all_names.remove("doe")
except:
    pass
try:
    all_names.remove("Doe")
except:
    pass


def is_name(word):
    return word in all_names


# BEGIN THE TROLLING
def trollifyWord(word):
    prob = random.randint(0,101)
    postfix = ""
    postpostfix = ""
    while word.endswith("."):
        postpostfix = postpostfix + "."
        word = word[:-1]

    if word.endswith("\'s"):
        postfix = word[-2:]
        word = word[:-2]
    elif word.endswith("s\'"):
        postfix = word[-1:]
        word = word[:-1]

    if word in all_names:
        gender = sex_classifier.classify(gender_features(word))
        if gender == "male":
            word = "Derp"
        elif gender == "female":
            word = "Derpina"
        if postfix:
            postfix = "\'s"
    else:
        if word == "the" and prob > 50:
            word = "le"
        if word == "The" and prob > 50:
            word = "Le"
        if word == "why" and prob > 50:
            word = "y"
        if word == "Why" and prob > 50:
            word = "Y"
        if word == "you're" and prob < 80:
            word = "your"
        if word == "You're" and prob < 80:
            word = "Your"
        if word == "what" and prob > 50:
            word = "wat"
        if word == "What" and prob > 50:
            word = "Wat"

    word = word + postfix + postpostfix
    return word

def trollifySentence(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)):
        print ("word: ", sentence[i])
        sentence[i] = trollifyWord(sentence[i])
    return " ".join(sentence)

def getRage(string):
    result = classifier.prob_classify(word_feats(word_tokenize(string)))
    return result.prob('pos')

def getRageList(paragraph):
    sentences = tokenize.sent_tokenize(paragraph)

    sentences = [string.strip() for string in sentences if len(string.strip()) > 0]
    sentiments = []

    # generate the predictions on original text
    for sentence in sentences:
        sentiments.append(getRage(sentence))

    # reddit-fy the text
    for i in range(len(sentences)):
        print ("trollifying: ",sentences[i])
        sentences[i] = trollifySentence(sentences[i])

    return (sentiments, sentences)


