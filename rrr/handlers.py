from telegrambot.decorators import command
from telegrambot.handlers import BaseCommandHandler

@command('start')
def start_command(update, context):
    pass
    # Handle start command here

@command('author')
def author_command(update, context):
    pass