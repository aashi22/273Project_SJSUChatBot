# 273Project_SJSUChatBot

## Before you begin:

Create a Bluemix account
Sign up in Bluemix, or use an existing account. Your account must have available space for at least 1 app and 1 service.

### Installation

   $ npm install botkit-middleware-watson --save


## Bot setup:

Step1: 
### Acquire Watson Conversation credentials

The middleware needs you to provide the username, password, and workspace_id of your Watson Conversation chat bot.

Step2:
### Acquire channel credentials
You need a Slack token for your Slack bot to talk to Conversation.


Step 3:
### Create Slack Controller using Botkit: 

In your app, add the following lines to create your Slack controller using Botkit:
var slackController = Botkit.slackbot();

Spawn a Slack bot using the controller:
var slackBot = slackController.spawn({
    token: YOUR_SLACK_TOKEN
});

Create the middleware object which you'll use to connect to the Conversation service:

var watsonMiddleware = require('botkit-middleware-watson')({
  username: YOUR_CONVERSATION_USERNAME,
  password: YOUR_CONVERSATION_PASSWORD,
  workspace_id: YOUR_WORKSPACE_ID,
  version_date: '2016-09-20',
  minimum_confidence: 0.50, // (Optional) Default is 0.75
});

Tell your Slackbot to use the watsonMiddleware for incoming messages:

slackController.middleware.receive.use(watsonMiddleware.receive);
slackBot.startRTM();


Finally, make your bot listen to incoming messages and respond with Watson Conversation:

slackController.hears(['.*'], ['direct_message', 'direct_mention', 'mention'], function(bot, message) 
{
    bot.reply(message, message.watsonData.output.text.join('\n'));
});

The middleware attaches the watsonData object to message. This contains the text response from Conversation.

## Middleware Functions
The watsonMiddleware object provides some useful functions which can be used for customizing the question-answering pipeline.

### interpret

The interpret() function works very similarly to the receive function but unlike the receive function,

it is not mapped to a Botkit function so doesn't need to be added as a middleware to Botkit
doesn't get triggered on all events
The interpret function only gets triggered when an event is heard by the controller. For example, one might want your bot to only respond to direct messages using Conversation. In such scenarios, one would use the interpret function as follows:

slackController.hears(['.*'], ['direct_message'], function(bot, message) 
{
  middleware.interpret(bot, message, function(err) 
  {
    if (!err)
      bot.reply(message, message.watsonData.output.text.join('\n'));
  });
});

### hear

The Watson middleware also includes a hear() function which provides a mechanism to developers to fire handler functions based on the most likely intent of the user. This allows a developer to create handler functions for specific intents in addition to using the data provided by Watson to power the conversation.

The hear() function can be used on individual handler functions, or can be used globally.

Used on an individual handler:

slackController.hears(['hello'], ['direct_message', 'direct_mention', 'mention'], watsonMiddleware.hear, function(bot, message) 
{

   bot.reply(message, message.watsonData.output.text.join('\n'));

    // now do something special related to the hello intent

});

Used globally:

slackController.changeEars(watsonMiddleware.hear);

slackController.hears(['hello'], ['direct_message', 'direct_mention', 'mention'], function(bot, message) 
{

   bot.reply(message, message.watsonData.output.text.join('\n'));

    // now do something special related to the hello intent
});
