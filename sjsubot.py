import os
import time
from slackclient import SlackClient


# sjsubot's ID as an environment variable
BOT_ID = os.getenv('BOT_ID', 'U52M881PB')
#BOT_ID = os.environ.get('BOT_ID')
print BOT_ID
# constants
AT_BOT = "<@" + BOT_ID + ">"
