#import sentistrength
from sentistrength import PySentiStr
senti_en = PySentiStr()
senti_en.setSentiStrengthPath('util/jar_datei/SentiStrength.jar') # Note: Provide absolute path instead of relative path
senti_en.setSentiStrengthLanguageFolderPath('util/SentiStrengthData_EN/') # Note: Provide absolute path instead of relative path

senti_de = PySentiStr()
senti_de.setSentiStrengthPath('util/jar_datei/SentiStrength.jar') # Note: Provide absolute path instead of relative path
senti_de.setSentiStrengthLanguageFolderPath('util/SentiStrengthData_DE/') # Note: Provide absolute path instead of relative path

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from util.GerVader.vaderSentimentGER import GerSentimentIntensityAnalyzer

from textblob import TextBlob
from textblob_de import TextBlobDE

import nltk
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet

nltk.download("wordnet")
nltk.download("sentiwordnet")

def get_sentiments_sentistrength(text, lang, mode = 'trinary'): #mode = dual, scale, binary, trinary
    if lang == "en":
        senti_score = senti_en.getSentiment(text, score=mode)
    elif lang == "de":
        senti_score = senti_de.getSentiment(text, score=mode)
    dict_senti_score = {}
    if mode == "dual":
        dict_senti_score["pos"] = senti_score[0][0]
        dict_senti_score["neg"] = senti_score[0][1]
    elif mode == "scale":
        dict_senti_score["compound"] = senti_score[0]
    elif mode == "binary":
        dict_senti_score["binary"] = senti_score[0]
    elif mode == "trinary":
        dict_senti_score["pos"] = senti_score[0][0]
        dict_senti_score["neg"] = senti_score[0][1]
        dict_senti_score["neu"] = senti_score[0][2]
    return dict_senti_score
    # SentiResult(positive=2, negative=-1, neutral=1)

def get_sentiments_vader(text, lang):
    if lang == "en":
        sid_obj = SentimentIntensityAnalyzer()
    elif lang == "de":
        sid_obj = GerSentimentIntensityAnalyzer()
    dict_senti_score = sid_obj.polarity_scores(text)
    return dict_senti_score

def get_sentiments_textblob(text, lang):
    if lang == "en":
        testimonial = TextBlob(text)
    elif lang == "de":
        testimonial = TextBlobDE(text)
    dict_senti_score = {"polarity": testimonial.sentiment.polarity,
                        "subjectivity": testimonial.sentiment.subjectivity
                        }
    return dict_senti_score

def get_sentiments_sentiwordnet(text):
    tokens = nltk.word_tokenize(text)
    postags = nltk.pos_tag(tokens)
    
    for postag in postags:
        wntag = ''
        dict_senti_score = {"pos": 0, "neg": 0}
        if postag[0].startswith('J'):
            wntag = wordnet.ADJ
        elif postag[0].startswith('R'):
            wntag = wordnet.ADV
        elif postag[0].startswith('N'):
            wntag = wordnet.NOUN
        else:
            continue
        print(postags[1], wntag)
        wordSynst = wordnet.synsets(postag[1], pos=wntag)
        print(wordSynst)
        if not wordSynst:
            continue
        else:
            sentiwn = sentiwordnet.senti_synset(wordSynst[0].name())
            dict_senti_score["pos"] += sentiwn.pos_score()
            dict_senti_score["neg"] += sentiwn.neg_score()
    return dict_senti_score

