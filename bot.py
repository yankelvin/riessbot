import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.DialogFlowService.DialogFlowService import DialogFlowService
from src.RecommenderService.RecommenderService import RecommenderService

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = '1235534923:AAHaeuDNKFQLX3GR5f-eHzRuxzdyFvUzb5M'
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

dialog_flow = DialogFlowService()
recommender = RecommenderService()


def start(update, context):
    message = "Olá, quero te ajudar a passar o tempo melhor nessa quarentena, portanto vou te recomendar vários filmes para que você possa assistir :)"
    message += "\nPara começarmos me diga qual seu filme preferido :P"

    context.bot.send_message(chat_id=update.message.chat_id, text=message)


def echo(update, context):
    msg = update["message"]["text"]

    response = dialog_flow.SendIntent(msg)

    message = response["bot_response"]
    movie = response["movie"]

    if (movie != ""):
        recommender.GetRecommendation(movie)

    context.bot.send_message(chat_id=update.message.chat_id, text=message)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
