import nltk
import pickle
import string

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
remove_stop_words = dict((word, None)
                         for word in stopwords.words('english'))


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict).translate(remove_stop_words)))


tfidf_vectorizer = TfidfVectorizer(
    tokenizer=LemNormalize, stop_words='english')


class RecommenderService:
    def __init__(self):
        self.kmeans = None
        self.animes = []
        self.__Fit()

    def __Fit(self):
        print("Carregando animes...")
        self.animes = pickle.load(
            open('./src/RecommenderService/data-animes.pkl', 'rb'))

        print(f"{len(self.animes)} carregados!")

        synopsis = list()
        for anime in self.animes:
            synopsis.append(anime["synopsis"].replace(
                "ha", "").replace("le", "").replace("wa", ""))

        print("Iniciando o treino!")
        tfidf = tfidf_vectorizer.fit_transform(synopsis)

        self.kmeans = KMeans(n_clusters=250).fit(tfidf)
        print("Treino finalizado.")

        print("Ajustando grupos.")
        for k, v in enumerate(self.kmeans.labels_):
            self.animes[k]['cluster'] = v

        print("Tudo pronto chefe!\n")

    def GetRecommendation(self, query):
        index = self.kmeans.predict(tfidf_vectorizer.transform([query]))
        recommendations = []

        print("")
        for k, anime in enumerate(self.animes):
            if anime['cluster'] == index[0]:
                # print(f"Anime: {anime['name']} - Cluster: {anime['cluster']}")
                recommendations.append(anime)

        # print(self.kmeans.score(tfidf_vectorizer.transform([query])))

        return recommendations

    def GetAnimes(self):
        return self.animes


# recommender = RecommenderService()
# recommender.GetRecommendation(
#     "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc.")
