import logging
from time import sleep
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.DialogFlowService.DialogFlowService import DialogFlowService

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = '1235534923:AAHaeuDNKFQLX3GR5f-eHzRuxzdyFvUzb5M'
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

dialog_flow = DialogFlowService()


def start(update, context):
    message = "Olá, seja bem vindo!"
    context.bot.send_message(chat_id=update.message.chat_id, text=message)


def echo(update, context):
    msg = update["message"]["text"]

    message = dialog_flow.SendIntent(msg)

    context.bot.send_message(chat_id=update.message.chat_id, text=message)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
