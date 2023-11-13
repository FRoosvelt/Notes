from environs import Env

env = Env()
env.read_env()

# Достает из .env BOT_TOKEN
BOT_TOKEN = env.str("BOT_TOKEN")
