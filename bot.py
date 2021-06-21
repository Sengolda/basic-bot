from utils.Bot import Bot
from config.bot import C as bot_config

run_bot = True
if run_bot:
        bot = Bot()
        try:
                bot.run(bot_config.token)
        finally:
                print("Bot closing!")