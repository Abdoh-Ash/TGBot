import telebot
import wikipedia
import googlesearch
import youtubesearchpython
from constants import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
	if message.chat.first_name == None:
		first_name = "fellow human"
	else:
		first_name = message.chat.first_name
	bot.send_message(1369681614, "This user has messaged me:\nName: {0}\nUsername: {1}\nID: {2}".format(str(message.chat.first_name) + " " + str(message.chat.last_name), str(message.chat.username), message.chat.id))
	bot.send_message(message.chat.id, WELCOME.format(first_name))
	bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["help", "about", "purpose", "ping"])
def handle_general(message):
	try:
		text = message.text[:message.text.index('@')]
	except:
		text = message.text

	if message.chat.type == "private":
		bot.send_message(message.chat.id, eval(text.replace('/', "").upper()))
	else:
		bot.reply_to(message, eval(text.replace('/', "").upper()))

@bot.message_handler(commands=["google", "youtube", "wikipedia"])
def handle_features(message):
	try:
		text = message.text[:message.text.index('@')]
	except:
		text = message.text
	
	if message.chat.type == "private":
		bot.send_message(message.chat.id, eval(text.replace('/', "").upper()))
	else:
		bot.reply_to(message, eval(text.replace('/', "").upper()))

	if text == "/google":
		bot.register_next_step_handler(message, google_search)
	elif text == "/youtube":
		bot.register_next_step_handler(message, youtube_search)
	elif text == "/wikipedia":
		bot.register_next_step_handler(message, wiki_summary)

def wiki_summary(message):
	try:
		result = wikipedia.summary(message.text)
	except:
		result = "Sorry, no results were found for that."
	bot.send_message(message.chat.id, result)

def google_search(message):
	try:
		results = googlesearch.search(message.text, num_results=3)[:-1]
	except:
		results = ["Sorry, no results were found for that."]
	
	for result in results:
		bot.send_message(message.chat.id, result)

def youtube_search(message):
	try:
		results = youtubesearchpython.VideosSearch(message.text, limit=3).result()["result"]
		results = [video["link"] for video in results]
	except:
		results = ["Sorry, no results were found for that."]
	
	for result in results:
		bot.send_message(message.chat.id, result)

@bot.message_handler(func=lambda message: True)
def send_sorry(message):
	if message.chat.type == "private":
		bot.send_message(message.chat.id, SORRY)
	else:
		bot.reply_to(message, SORRY)


bot.polling()
