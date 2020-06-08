import nltk
import pickle
import string

from imdb import IMDb
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


class RecommenderService:
    def __init__(self):
        self.ia = IMDb()
        self.clusters = dict()
        self.Fit()

    def Fit(self):
        top = self.ia.get_top250_movies()

        data = pickle.load(
            open('./src/RecommenderService/training_data.pkl', 'rb'))
        tfidf_vectorizer = TfidfVectorizer(
            tokenizer=LemNormalize, stop_words='english')
        tfidf = tfidf_vectorizer.fit_transform(data)

        kmeans = KMeans(n_clusters=25).fit(tfidf)

        for k, movie in enumerate(top):
            self.clusters[movie['title']] = kmeans.labels_[k]

    def GetRecommendation(self, movie):
        search = self.ia.search_movie(movie)
        # filme = search[indice]
        # id = filme.getID()
        # filme = self.ia.get_movie(id)
        print(search)
