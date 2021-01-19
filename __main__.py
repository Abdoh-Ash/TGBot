import telebot


TOKEN = "1598166798:AAHB53uMiDjh0LQldlw0m--CsQw6BGWAw-E"

WELCOME = "Hello, {0}!\nI'm Adam, a friendly and funny chatbot.\n\nI also help manage the group Thought Café, most of my functional capabilities are dedicated to that task, pretty mundane, right?\n\nBut no worries, my brother, Abdoh, will make me more fun in the near future."
HELP = "The following commands are supported:\n\nGeneral:\nStart Menu: /start\nHelp Menu: /help\n\nThought Café Specific:\nAbout Thought Café: /about\nThe Guidelines of Thought Café: /guidelines"

ABOUT = "Thought Café is a virtual community of brilliant-minded individuals, with the objective of sharing knowledge, insight, and wisdom\n\nWe discuss countless topics on regular basis, we bring up questions, share opinions and search for answers.\nThere is no end to education. It is not that you read a book, pass an examination, and finish with education. The whole of life, from the moment you are born to the moment you die, is a process of learning. Learning is a lifelong process.\n\nHumans are by nature social creatures, so don't worry, you'll enjoy the ride with us!"
GUIDELINES = """The rules and guidelines for our community are as follows:

1. Be Kind and Courteous
We're all in this together to create a welcoming environment. Let's treat everyone with respect. Healthy debates are natural, but kindness is required.

2. No Promotions or Spam
Give more than you take to this group. Self-promotion, spam and irrelevant links aren't allowed.

3. Respect Other Views
“I am convinced about the veracity of my opinions, but I do consider it likely that they may turn out to be incorrect. Likewise, I am convinced about the incorrectness of the views different from mine, but I do concede the possibility that they may turn out to be correct.” — Imam Shafa’i

And finally, feel at home!
Don't be an observer all the time, get engaged and be active."""


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.send_message(message.chat.id, WELCOME.format(message.chat.first_name))
	bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["help"])
def send_help(message):
	bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["about"])
def send_about(message):
	bot.send_message(message.chat.id, ABOUT)

@bot.message_handler(commands=["guidelines"])
def send_guidelines(message):
	bot.send_message(message.chat.id, GUIDELINES)


bot.polling()