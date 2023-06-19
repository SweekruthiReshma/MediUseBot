!pip install transformers
!pip install openai
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
model = AutoModel.from_pretrained("dmis-lab/biobert-v1.1")
!pip install pyTelegramBotAPI requests
import telebot
import openai

# Set up your Telegram bot token
BOT_TOKEN = 'Your Bot API Token '

# Set up your OpenAI API credentials
openai.api_key = '*******************************************YOUR OPEN AI API*********************************'

# Initialize the Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)

# Generate medicine usage description using OpenAI ChatGPT
def generate_medicine_description(medicine_name):
    prompt = f"What is the usage of {medicine_name}?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    description = response.choices[0].text.strip()
    return description

# Handle the '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Welcome to the MediUse Bot! Send me the name of a medicine, and I will provide its usage description.")

# Handle the '/hello' command
@bot.message_handler(commands=['hello'])
def handle_hello(message):
    bot.reply_to(message, "Hello! How can I assist you today?")

# Handle the '/bye' command
@bot.message_handler(commands=['bye'])
def handle_bye(message):
    bot.reply_to(message, "Goodbye! Feel free to reach out if you have more questions.")

# Define the handler for processing incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    medicine_name = message.text
    medicine_description = generate_medicine_description(medicine_name)
    response = f"Medicine: {medicine_name}\n\nDescription: {medicine_description}"
    bot.reply_to(message, response)

# Start the Telegram bot
bot.polling()
