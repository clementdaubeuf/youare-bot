import discord
from discord.ext import commands
import random
from random import randint
import os
from dotenv import load_dotenv
from unidecode import unidecode

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

def generate_message():
    translations = {
        'fr': 'Tu es ?',      # Français
        'en': 'Are you?',     # Anglais
        'es': '¿Eres?',       # Espagnol
        'ja': 'あなたは？',     # Japonais
        'de': 'Bist du?',     # Allemand
        'it': 'Sei?',         # Italien
        'pt': 'Você é?',      # Portugais
        'ru': 'Ты есть?',     # Russe
        'ko': '넌 누구니?',     # Coréen
        'zh': '你是？',        # Chinois (simplifié)
        'ar': 'أنت؟',         # Arabe
        'hi': 'तुम हो?',        # Hindi
        'nl': 'Ben jij?',     # Néerlandais
        'tr': 'Sen misin?',   # Turc
        'sv': 'Är du?',       # Suédois
        'pl': 'Jesteś?',      # Polonais
        'fi': 'Oletko?',      # Finnois
        'no': 'Er du?',       # Norvégien
        'el': 'Είσαι;',       # Grec
        'hu': 'Te vagy?',     # Hongrois
    }

    selected_language = random.choice(list(translations.keys()))
    message_content = unidecode(translations[selected_language])

    return message_content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if randint(1, 100) == 1:
        await message.channel.send(generate_message())

# don't forget to add your bot token in the .env file
bot.run(BOT_TOKEN)