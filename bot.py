import logging
from googletrans import Translator
from random import shuffle
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.HangmanGame.HangmanGame import HangmanGame
from src.DialogFlowService.DialogFlowService import DialogFlowService
from src.RecommenderService.RecommenderService import RecommenderService

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = '1235534923:AAHaeuDNKFQLX3GR5f-eHzRuxzdyFvUzb5M'
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

translator = Translator()
dialog_flow = DialogFlowService()
recommender = RecommenderService()

animes = recommender.GetAnimes()


def start(update, context):
    message = "Olá, eu sou a Ries e eu fui programada com 2 funcionalidades :P"
    message += "\n - Posso te recomendar animes, basta me dizer o nome de um dos seus preferidos,"
    message += " minhas recomendações são baseadas no top 1200 animes do MyAnimeList."
    message += "\n - Podemos jogar o jogo da forca, onde você me diz um nome de um anime e eu utilizo um algoritmo genético para chegar a esse nome"
    message += "\n - Para jogar o jogo da forca basta digitar: Jogo {Nome do Anime} | Forca {Nome do Anime}"

    context.bot.send_message(chat_id=update.message.chat_id, text=message)


def echo(update, context):
    result = []
    msg = update["message"]["text"]

    response = dialog_flow.SendIntent(msg)

    message = response["bot_response"]
    anime = response["anime"]
    intent = response["intent"]

    if intent == "Forca" and anime != "":
        game = HangmanGame.Start(anime)
        generations = game["generations"]

        start = 0
        if len(generations) > 5:
            start = 5
        else:
            start = len(generations)

        for i in range(len(generations) - start, len(generations), 1):
            message = f"Generation: {generations[i]['generation']}\tString: {generations[i]['string']}\tFitness: {generations[i]['fitness']}"
            context.bot.send_message(
                chat_id=update.message.chat_id, text=message)

        message = f"Após {game['generation']} gerações consegui chegar ao nome do anime, ufa!"
        message += f"\nEsse é o seu anime: {anime}"

        context.bot.send_message(
            chat_id=update.message.chat_id, text=message)
    elif (anime != ""):
        synopsis = ""
        for _anime in animes:
            if anime in _anime["name"]:
                synopsis = _anime["synopsis"]

                message = f"O anime utilizado como base foi: {_anime['name']}"
                context.bot.send_message(
                    chat_id=update.message.chat_id, text=message)

                message = f"Sua sinopse: {translator.translate(synopsis, dest='pt').text}"
                context.bot.send_message(
                    chat_id=update.message.chat_id, text=message)
                break

        if (synopsis != ""):
            result = recommender.GetRecommendation(synopsis)

            context.bot.send_message(
                chat_id=update.message.chat_id, text="\nMinhas recomendações:")

            if len(result) > 5:
                shuffle(result)

            for i, anime in enumerate(result):
                if len(result) <= 5 or (len(result) > 5 and i < 5):
                    message = f"Anime: {anime['name']}"
                    context.bot.send_message(
                        chat_id=update.message.chat_id, text=message)
        else:
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Desculpe, não tenho esse anime na minha base :C")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text=message)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
