# PyConversation

Zero-dependency library for chat-bot creators with deadlines.

It allows you to describe a conversation, talk with user according to your schema and restore it, if something went wrong.

### Table of contents

-   <a href="#quickstart">Quickstart</a>
-   <a href="#messages">Messages</a>
    -   <a href="#text">Text</a>
    -   <a href="#group">Group</a>
    -   <a href="#ask">Ask</a>
    -   <a href="#switch">Switch</a>
    -   <a href="#list-ask">ListAsk</a>
    -   <a href="#terminate-group">TerminateGroup</a>
    -   <a href="#own-messages">Creating Own Messages</a>
-   <a href="#loggers">Loggers</a>
    -   <a href="#dict-logger">DictLogger</a>
    -   <a href="#json-file-logger">JsonFileLogger</a>
    -   <a href="#own-loggers">Create Own Loggers</a>
-   <a href="#sender">Message Sender</a>

## <a id="quickstart"></a>Quickstart

### First we need to create a message schema, which consists of messages.

Messages describe chat-bot's actions. For instance, send a text message, which doesn't need any feedback or ask a question. Each message has a unique id. Most common messages are `Group`, `Text` and `Ask`.

For full details about different message types <a href="#messages">see Messages</a>

`Group` is a kind of container, that holds list of other messages.

`Text` sends a text message, which doesn't require feedback.

`Ask` sends a text message and waits for answer

Enough theory, let's see an example!

```python
from pyconversation import Group, Text, Ask

fruit_bot_conversation = Group(
    id="root",
    children=[
        Text(id="root.hello", text="Hello!"),
        Ask(id="root.fruits", text="What fruits do you like?"),
        Text(id="root.bye", text="Bye"),
    ],
)
```

In this example, we create a schema for simple bot, who asks what fruits does user like. Root message is a `Group`. It holds a block of messages. First of them is a `Text` which send user a greeting message. Second one (`Ask`) asks about user's favorite fruit and waits for answer. And finally third `Text` message send `Bye` to user.

### Second step - we need a logger

Logger is an object, which stores user's answers and message history. This library exposes 2 loggers:

-   `DictLogger` - stores data in a dictionary
-   `JsonFileLogger` - takes file path as a parameter and stores json data in this file

If you need something different, <a href="#own-loggers">see Creating Own Loggers</a>

But now let's use `DictLogger`

```python
from pyconversation import DictLogger

logger = DictLogger()
```

That's all!

For full loggers documentation <a href="#loggers">see Loggers</a>

### But how to send those messages?

The answer's simple - using a `MessageSender`!

Example code:

```python
from pyconversation import Group, Text, Ask, MessageSender

# Conversation from step 1
fruit_bot_conversation = Group(
    id="root",
    children=[
        Text(id="root.hello", text="Hello!"),
        Ask(id="root.fruits", text="What fruits do you like?"),
        Text(id="root.bye", text="Bye"),
    ],
)

# Logger from step 2
logger = DictLogger()

# Initialize a message sender
sender = MessageSender(
    root=fruit_bot_conversation, # Our conversation
    logger=logger, # Our logger
    send=print # A send function, which takes a string and send the message. In this case, we use print to log messages to console
)

# Answer to the question before the first one is always empty
answer = None

# Send messages!
while True:
    # Send messages one by one, until we run into a message, which requires an answer
    # This function takes answer to previous question as a parameter
	sender.send_all_skippable(answer)

    # If all messages sent
	if sender.finished:
        # Dispose of sender's resources (like open files) and get the result!
		print("\nResult:", sender.finalize())
		break

    # If not all messages have been sent and we still need an answer, ask!
	answer = input()
```

Done! If you run this, you'll get the following in the console:

```
Hello!
What fruits do you like?
<your answer'll be here>
Bye

Result: {'root.fruits': '<your answer>'}
```

And one more example with decorated function (like in real chat-bots):

```python
bot = ... # Initilaize chat bot

sender = None

@bot.connection
def on_connection(user_id):
    sender = MessageSender(
        root=conversation, # Our conversation
        logger=logger, # Our logger
        send=lambda text: bot.send(user_id, text)
    )

    sender.send_all_skippable(None)

@bot.message
def on_message(user_id, message):
    sender.send_all_skippable(answer)

    if sender.finished:
        print("\nResult:", sender.finalize())
        sender = None
```

For full message sender documentation <a href="#sender">see Message Sender</a>

### You've created your first chat-bot with clever conversation! Here quick tutorial ends.
