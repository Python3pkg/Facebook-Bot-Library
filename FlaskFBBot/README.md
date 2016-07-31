# README #

### This is a facebook messaging SDK for Flask ###

### Usage ###
* There should be a file "config.json" containing your token
```
#!json

{ "token" : "<your token>" }
```
```
#!python

from flask import request
from facebook_messaging.fbbot import FBBot
from facebook_messaging.order import FBOrder
from facebook_messaging.attachment import FBAttachment

import json
with open('config.json') as data_file:    
    data = json.load(data_file)

token = data["token"]
verify_token = "<your verify_token>"
bot = FBBot(token, verify_token)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return bot.webhook(request, on_message, on_postback)

def on_postback(sender, text, requestInfo):
    #something to do

def on_message(sender, text, requestInfo):
    #something to do

```

### Message attachments ###
```
#!python

class FBAttachment():
    class File():
        image
        audio
        video
        file

    def button_postback(title, postback):
        return ...

    def button_web_url(title, url):
        return ...

    def quick_reply(title):
        return ...
```

### Sending a message examples ###
```
#!python

#Simple text message
bot.send_text_message(sender, "Hello, What do you want?")
```
```
#!python

#Video message
bot.send_message_file_attachment(sender, FBAttachment.File.video, "http://img-9gag-fun.9cache.com/photo/adXLy8N_460sv.mp4")
```
```
#!python

#Image message
bot.send_message_file_attachment(sender, FBAttachment.File.image, "http://img-9gag-fun.9cache.com/photo/aEnxQve_460s_v1.jpg")
```
```
#!python

#Generic message
bot.send_message_generic(sender, "Generic message", "with image and button", "https://scontent.xx.fbcdn.net/t39.3138-6/p128x128/12056981_908479762570256_1493516739_n.jpg", 
    [ 
        FBAttachment.button_web_url("Google", "http://google.com/?q=facebook"),
        FBAttachment.button_postback("Button title","Button postback")
    ])
```
```
#!python

#Receipt message
order = FBOrder(
    "Stephane Crozatier", 
    "125352345", 
    "USD", 
    "Visa", 
    "http://google.com", 
    "1273246346", 
    [
        FBOrder.one_purchase("T-Shirt", "yellow", 1, 5, "USD", "http://cdn01.shopclues.net/images/detailed/19936/yellowtshirt_1434534567.jpg"),
        FBOrder.one_purchase("Baseball cap", "white", 2, 2, "USD", "http://i01.i.aliimg.com/img/pb/630/860/383/383860630_626.jpg")
    ],
    FBOrder.address("1 Hacker Way", "", "Menlo Park", "94025", "CA", "US"),
    FBOrder.price_summary(9, 0, 1, 8),
    [  
        FBOrder.price_one_adjustment("2$ Off coupon", 2)
    ]
)
bot.send_message_receipt(sender, order)
```
```
#!python

#Every message may contain up to ten quick replies passed as last argument
bot.send_text_message(sender, "Hello, What do you want?", [ 
    FBAttachment.quick_reply("Something"), 
    FBAttachment.quick_reply("Nothing"),
    FBAttachment.quick_reply("I don't know")
])
```