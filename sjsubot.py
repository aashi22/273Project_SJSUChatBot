import os
import time
from slackclient import SlackClient

# sjsubot's ID as an environment variable
BOT_ID = os.environ.get('BOT_ID')
print BOT_ID
# constants
AT_BOT = "<@" + BOT_ID + ">"

EXAMPLE_COMMAND = "do"

# instantiate Slack
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """



