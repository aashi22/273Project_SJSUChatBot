import os
from slackclient import SlackClient


BOT_NAME = 'sjsubot'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")

