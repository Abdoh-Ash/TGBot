import telebot
import wikipedia
from constants import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.send_message(1369681614, "This user has messaged me:\nName: {0}\nUsername: {1}\nID: {2}".format(str(message.chat.first_name) + " " + str(message.chat.last_name), str(message.chat.username), message.chat.id))
	bot.send_message(message.chat.id, WELCOME.format(message.chat.first_name))
	bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["help", "about", "purpose", "ping"])
def handle_general(message):
	bot.send_message(message.chat.id, eval(message.text.replace('/', "").upper()))

@bot.message_handler(commands=["wikipedia"])
def handle_features(message):
	bot.send_message(message.chat.id, eval(message.text.replace('/', "").upper()))
	bot.register_next_step_handler(message, wiki_summary)

def wiki_summary(message):
	try:
		result = wikipedia.summary(message.text)
	except:
		result = "Sorry, no results were found for that."
	bot.send_message(message.chat.id, result)

@bot.message_handler(func=lambda message: True)
def send_sorry(message):
	bot.send_message(message.chat.id, SORRY)


bot.polling()
