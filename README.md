# Messenger SDK for Flask #

[![Python](https://img.shields.io/badge/python-3.4+-green.svg)]()
[![Pypi](https://img.shields.io/badge/pypi-v0.1-blue.svg)]()
[![Status](https://img.shields.io/badge/status-development-red.svg)]()

Facebook Messenger Platform SDK for [Flask](http://flask.pocoo.org/)

## Get started ##

**Note**: You need [Flask](http://flask.pocoo.org/) to be installed

### Installation ###
Easy to Setup via pip
```bash
$ pip install Facebook-Bot-Library
```

Installation via Git
```bash
$ git clone https://github.com/boosted-lab/Facebook-Bot-Library.git
$ python Facebook-Bot-Library/setup.py install
```

### Usage ###
#### Receiving a message and sending a response example ####
```python

from flask import request
from facebook_messaging.fbbot import FBBot
from facebook_messaging.order import FBOrder
from facebook_messaging.attachment import FBAttachment

token = "<your token>"
verify_token = "<your verify_token>"
bot = FBBot(token, verify_token)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return bot.webhook(request, on_message, on_postback)

def on_postback(sender, text, requestInfo):
    # something to do

def on_message(sender, text, requestInfo):
    # something to do

```

## Contents ##
Examples:
* [Get started](#get-started)
* [Built-in methods for sending messages](#built-in-methods-for-sending-messages)
  * [Creating message attachments](#creating-message-attachments)
* [Airline chekin template usage example](#airline-chekin-template)
* [Airline flight update template usage example](#airline-flight-update-template)
* [Airline Boarding Pass template usage example](#airline-boarding-pass-template)
* [Airline Itinerary template usage example](#airline-itinerary-template)
* [Receipt template usage example](#receipt-template)

Reference:
* [AirlineChekin class reference](#airlinechekin-class-reference)
* [AirlineFlightUpdate class reference](#airlineflightupdate-class-reference)
* [AirlineBoardingPass class reference](#airlineboardingpass-class-reference)
* [AirlineItinerary class reference](#airlineitinerary-class-reference)
* [FBBot class reference](#fbbot-class-reference)
* [FBOrder class reference (Receipt template)](#fborder-class-reference-receipt-template)
* [FBAttachment class description](#creating-message-attachments)

## Built-in methods for sending messages ##
[Go to: Contents](#contents)

### Text message ###
```python
FBBot.send_text_message(self, recipient_id, text, quick_replies = []) 
    '''
    @required:
        recipient_id
        text
    @optional:
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply
    @output:
        response_json
    '''

# Example
bot.send_text_message(sender, "Hello, how can I help you?")
```

### Message with attachment ###
 ```python
 FBBot.send_message_file_attachment(self, recipient_id, attachment_type, file_url, quick_replies = [])
    '''
    @required:
        recipient_id
        attachment_type from FBAttachment.File
        file_url
    @optional:
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply
    @output:
        response_json
    '''
# Example (video attachment)
bot.send_message_file_attachment(sender, FBAttachment.File.video, 
    "http://img-9gag-fun.9cache.com/photo/adXLy8N_460sv.mp4")
    
# Example (image attachment)
bot.send_message_file_attachment(sender, FBAttachment.File.image, 
    "http://img-9gag-fun.9cache.com/photo/aEnxQve_460s_v1.jpg")
 ```

### Creating message attachments ###

Use class ```FBAttachment``` for creating attachments to your messages

For creating postback buttons, web url buttons and quick replies there're few methods:

```python
    FBAttachment.button_postback(title, postback)
    FBAttachment.button_web_url(title, url)
    FBAttachment.quick_reply(title)
```


Also, ```FBAttachment``` contents nested class ```File```.

You should use these fieds of the class to obtain ```attachment_type```

```python
FBAttachment.File.image
FBAttachment.File.audio
FBAttachment.File.video
FBAttachment.File.file
```

 
### Generic message ###
Use the Facebook's Generic template to send a message composed of an image attachment, short description and buttons to request input from the user. The buttons can open a URL, or make a callback to your webhook.
 ```python
 FBBot.send_message_generic(self, recipient_id, title, subtitle, image_url, buttons = [], quick_replies = [])
     '''
    @required:
        recipient_id
        title
        subtitle (may be empty string)
        image_url (may be empty string)
    @optional:
        buttons array, up to three buttons, each is FBAttachment.button
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply
    @output:
        response_json
    '''
```

##### Example #####
```python

buttons = [
            {
                "type": "web_url",
                "url": "https://www.google.com",
                "title": "View Google",

            },
            {
                "type": "web_url",
                "url": "https://www.yandex.com",
                "title": "View Yandex",

            },
            {
                "type": "postback",
                "title": "Back",
                "payload": "USER_BACK_PAYLOAD"
            }
        ]
        
bot.send_message_generic(sender, "Search engines' catalogue", "Select any",
                         "https://www.24k.com.sg/images/sem1.png",
                         buttons)
```

[![Generic example](http://ntarasov.ru/files/github/img/sHpOVtcPDCk.jpg)]()

### Other template messages ###
```python
FBBot.send_message_TypeC(self, recipient_id, template, quick_replies = [])
    '''
    @required:
        recipient_id
        template is instance of FBOrder or AirlineChekin, AirlineFlightUpdate, 
            AirlineItinerary or another class representing Messenger template
    @optional:
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply...
    @output:
        response_json
    '''
```

### Note ###

Every message may contain up to ten quick replies passed as last argument
```python
bot.send_text_message(sender, "Pick a color:", [ 
    FBAttachment.quick_reply("Red"), 
    FBAttachment.quick_reply("Blue"),
    FBAttachment.quick_reply("Green")
])
```

### Examples: Sending a template message ###

### Airline Chekin template ###
[Go to: Contents](#contents)

[Description at Facebook Developers](https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-checkin-template)
```python
message = AirlineCheckin(
    "Checkin",
    "en_US",
    "12356",
    [
        AirlineCheckin.make_flight_info(
            "QR142",
            AirlineCheckin.make_airport("SIN", "Singapore"),
            AirlineCheckin.make_airport("DME", "Moscow"),
            AirlineCheckin.make_flight_schedule("2016-01-05T15:05", "2016-01-06T19:05")
        )
    ]
    , "https://google.com")
bot.send_message_TypeC(sender, message)
```
Will result in

[![Airline chekin example](http://ntarasov.ru/files/github/img//MyEgjXXeWZU.jpg)]()

### AirlineChekin class reference ###
[Go to: Contents](#contents) 

Constructor
```python
AirlineChekin.__init__(self, intro_message, locale, pnr_number, flight_info, checkin_url, theme_color="")
    '''
    @required:
        intro_message
        locale
        pnr_number - booking number
        flight_info - Array of flight info objects
        chekin_url
    @optional:
        theme_color -  RGB hexadecimal string (default #009ddc)
    '''
```

Generating payload
```python
AirlineChekin.get_payload(self)
```

Creating "flight info" object
```python
AirlineChekin.make_flight_info(flight_number, departure_airport, arrival_airport, flight_schedule)
    '''
    @required:
        flight_number 
        departure_airport  - airport object
        arrival_airport - -//-
        flight_schedule - flight schedule object
    @output:
        Flight info JSON object
    '''
```

Creating "airport" object
```python
AirlineChekin.make_airport(airport_code, city, terminal="", gate="")
    '''
    @required
        airport_code
        city
    @optional
        terminal
        gate
    @output
        Airport info JSON object
    '''
```

Generating "flight schedule" object
```python
AirlineChekin.make_flight_schedule(departure_time, arrival_time, boarding_time="")
    '''
    @required:
        departure_time - time in 'YYYY-MM-DDThh:mm' format
        arrival_time
    @optional
        boarding_time
    @output:
        Flight schedule JSON object
    '''
```

### Airline flight update template ###
[Go to: Contents](#contents) 

[Description at Facebook Developers](https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-update-template)
```python
message = AirlineFlightUpdate(
    "UPD",
    "delay",
    "en_US",
    "12356",
    AirlineFlightUpdate.make_update_flight_info(
        "QR142",
        AirlineFlightUpdate.make_airport("SIN", "Singapore"),
        AirlineFlightUpdate.make_airport("DME", "Moscow"),
        AirlineFlightUpdate.make_flight_schedule("2016-01-05T15:35", "2016-01-07T19:35")
    )
)
bot.send_message_TypeC(sender, message)
```
[![Airline flight update example](http://ntarasov.ru/files/github/img/Ng6RW9N_JBA.jpg)]()

### AirlineFlightUpdate class reference ###
[Go to: Contents](#contents) 

Constructor
```python
AirlineFlightUpdate.__init__(self, intro_message, update_type, locale, pnr_number, 
                            update_flight_info, theme_color="")
    '''
    @required:
        intro_message
        update_type - must be "delay", "gate_change" or "cancellation"
        locale
        pnr_number - booking number
        update_flight_info
    @optional:
        theme_color -  RGB hexadecimal string (default #009ddc)
    '''
```

Creating updated flight info JSON object

```python
AirlineFlightUpdate.make_update_flight_info(flight_number, departure_airport, arrival_airport, flight_schedule)
    '''
    @required:
        flight_number
        departure_airport
        arrival_airport
        flight_schedule
    @output:
        Flight information JSON object
    '''
```

Generating "airport" object
```python
AirlineFlightUpdate.make_airport(airport_code, city, terminal="", gate="")
    '''
    @required:
        airport_code
        city
    @optional:
        terminal
        gate
    @output:
        Airport info JSON object
    '''
```

Creating "flight schedule" object

```python
AirlineFlightUpdate.make_flight_schedule(departure_time, arrival_time="", boarding_time="")
    '''
    @required
        departure_time
    @optional
        arrival_time
        boarding_time
    @output:
        Flight schedule JSON object
    '''
```

Generating payload

```python
AirlineFlightUpdate.get_payload(self)
    '''
    @output:
        payload
    '''
```

### Airline Boarding Pass template ###
[Go to: Contents](#contents) 

[Description at Facebook Developers](https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-boardingpass-template)
```python
message = AirlineBoardingPass(
            "someticket",
            "en_US",
            [
                AirlineBoardingPass.boarding_pass_item(
                    "Michel",
                    "http://ausbb.com/1/celts049.jpg",
                    "SAV45",
                    "",
                    "http://www.imgonline.com.ua/examples/qr-code.png",
                    "http://www.swissarmylibrarian.net/wp-content/uploads/2011/02/barcodelunch.png",
                    "business",
                    AirlineBoardingPass.flight_info(
                        "QR142",
                        AirlineFlightUpdate.make_airport("SIN","Singapore"),
                        AirlineFlightUpdate.make_airport("DME","Moscow"),
                        AirlineFlightUpdate.make_flight_schedule("2016-01-05T15:35","2016-01-07T19:35")
                    )
                )
            ]
        )

    bot.send_message_TypeC(sender, message)
```
[![Airline boarding pass example](http://ntarasov.ru/files/github/img/G1FcHB1aViU.jpg)]()
[![Airline boarding pass example](http://ntarasov.ru/files/github/img/Umy3_lQKftA.jpg)]()

### AirlineBoardingPass class reference ###
[Go to: Contents](#contents)

Constructor
```python
AirlineBoardingPass.__init__(self, intro_message, locale, boarding_pass, theme_color="")
    '''
    @required:
        intro_message
        locale
        boarding_pass - JSON boarding pass item
    @optional:
        theme_color
    '''
```

Generating boarding pass item

```python
AirlineBoardingPass.boarding_pass_item(passenger_name, 
                    logo_image_url, # URL for the airline logo image
                    pnr_number, # Booking nubmer
                    qr_code, # QR code image URL
                    barcode_image_url, # URL of the barcode image
                    above_bar_code_image_url, # URL of thin image above the barcode
                    travel_class, # Must be 'economy', 'business' or 'first_class'
                    flight_info, # flight info object
                    header_image_url="", # URL for the header image
                    header_text_field="", # Text for the header field
                    seat="", # 	Seat number
                    auxiliary_fields="", # Additional information to display in the auxiliary section
                    secondary_fields="") # Additional information to display in the secondary section
    # @output: boarding_pass JSON item
```

Creating "flight schedule" object

```python
AirlineBoardingPass.make_flight_schedule(departure_time, arrival_time="", boarding_time="")
    '''
    @required
        departure_time
    @optional
        arrival_time
        boarding_time
    @output:
        Flight schedule JSON object
    '''
```

Generating "flight schedule" item

```python
AirlineBoardingPass.flight_schedule(departure_time, arrival_time, boarding_time="")
    '''
    @required:
        departure_time
        arrival_time
    @optional:
        boarding_time
    @output:
        flight schedule JSON object
    '''
```

Creating "flight info" item

```python
AirlineBoardingPass.flight_info(flight_number, departure_airport, arrival_airport, flight_schedule, aircraft_type="")
    '''
    @required:
        flight_number
        departure_airport
        arrival_airport
        flight_schedule - flight schedule JSON object (checkout AirlineBoardingPass.flight_schedule)
    @optional:
        aircraft_type
    @output:
        flight info JSON objet
    '''
```

Creating item with airport details
 ```python
AirlineBoardingPass.airport(airport_code, city, terminal="", gate="")
    '''
    @required:
        airport_code
        city
    @optional:
        terminal
        gate
    @output:
        JSON object with airport details
    '''
 ```

Creating field with label and value

```python
AirlineBoardingPass.field(label, value)
    '''
    @required:
        label
        value
    @output:
        JSON object { "label": label, "value": value }
    '''
```

Generating payload

```python
 AirlineBoardingPass.get_payload(self)
    '''
    @output:
        payload
    '''
```

### Airline Itinerary template ###
[Go to: Contents](#contents) 

[Description at Facebook Developers](https://developers.facebook.com/docs/messenger-platform/send-api-reference/airline-itinerary-template)

```python
message = AirlineItinerary(
    "tickettohell",
    "en_US",
    "EF52A",
    [
        AirlineItinerary.passenger_info_item("Mary","2472784","549"),
        AirlineItinerary.passenger_info_item("John","2472786","550")
    ],
    [
        AirlineItinerary.flight_info_item(
            "cg001",
            "c411",
            "QR142",
            AirlineFlightUpdate.make_airport("SIN","Singapore"),
            AirlineFlightUpdate.make_airport("DME","Moscow"),
            AirlineFlightUpdate.make_flight_schedule("2016-01-05T15:35","2016-01-05T19:35"),
            "econome",
            "Aerobus 500"
        ),
        AirlineItinerary.flight_info_item(
            "cg002",
            "c412",
            "QR142",
            AirlineFlightUpdate.make_airport("DME","Moscow"),
            AirlineFlightUpdate.make_airport("JFK","New York"),
            AirlineFlightUpdate.make_flight_schedule("2016-01-05T20:00","2016-01-06T05:35"),
            "econome",
            "Aerobus 500"
        )

    ],
    [
        AirlineItinerary.passenger_segment_info_item(
            "c411",
            "2472784",
            "D14",
            "Standard",
            [
                AirlineItinerary.product_info_item("Luggage","50kg")
            ]
        ),
        AirlineItinerary.passenger_segment_info_item(
            "c412",
            "2472784",
            "D14",
            "Standard",
            [
                AirlineItinerary.product_info_item("Luggage","30kg")
            ]
        ),
        AirlineItinerary.passenger_segment_info_item(
            "c411",
            "2472786",
            "D16",
            "Standard",
            [
                AirlineItinerary.product_info_item("Luggage","50kg")
            ]
        ),
        AirlineItinerary.passenger_segment_info_item(
            "c412",
            "2472786",
            "D16",
            "Standard",
            [
                AirlineItinerary.product_info_item("Knive-box","3kg")
            ]
        )
    ],
    "500",
    "EUR",
    base_price="430",
    tax="70",
    price_info=[
        AirlineItinerary.price_info_item("Standart price","400","EUR"),
        AirlineItinerary.price_info_item("Service1","15","EUR"),
        AirlineItinerary.price_info_item("Service2","15","EUR")
    ],
)
bot.send_message_TypeC(sender, message)
```
[![Airline itinerary example](http://ntarasov.ru/files/github/img/wDeeKH33UkQ.jpg)]()
[![Airline itinerary example](http://ntarasov.ru/files/github/img/91x-Lecvdhc.jpg)]()

### AirlineItinerary class reference ###
[Go to: Contents](#contents) 

Constructor 

```python
AirlineItinerary.__init__(self, 
            intro_message, 
            locale, # must be a two-letter ISO 639-1 language code and a ISO 3166-1 alpha-2 region code. e.g. en_US, ru_RU
            pnr_number, # Booking number
            passenger_info, # Array of items generated by AirlineItinenrary.passenger_info_item
            flight_info, # Array of items generated by AirlineItinerary.flight_info_item
            passenger_segment_info, #  Array of items generated by AirlineItinerary.passenger_segment_info_item
            total_price, 
            currency, #  Must be a three digit ISO-4217-3 code - 'USD', 'EUR'...
            theme_color="", #  RGB hexadecimal string (default #009ddc)
            price_info="", # Array of items generated by AirlineItinerary.price_info_item
            base_price="", 
            tax="")
```

Passenger info item


```python
AirlineItinenrary.passenger_info_item(name, passenger_id,ticket_number="") 
    '''
    @required:
        name - passenger name
        passenger_id
    @optional:
        ticket_number
    @output:
        passenger info JSON object
    '''
```

Flight info item

```python
AirlineItinerary.flight_info_item(connection_id, 
            segment_id, # 	segment_id of passenger_segment_info object
            flight_number, 
            departure_airport, # airport item
            arrival_airport, # airport item
            flight_schedule, 
            travel_class, # Must be 'economy', 'business' or 'first_class'
            aircraft_type="")
```

Airport item
```python
AirlineFlightUpdate.airport(airport_code, city, terminal="", gate="")
    '''
    @required:
        airport_code
        city
    @optional:
        terminal
        gate
    @output:
        Airport info JSON object
    '''
```

Flight schedule object
```python
AirlineItinerary.make_flight_schedule(departure_time, arrival_time, boarding_time="")
    '''
    @required:
        departure_time
        arrival_time
    @optional
        boarding_time
    @output:
        Flight schedule JSON object
    '''
```

Passenger segment information item

```python
AirlineItinerary.passenger_segment_info_item(segment_id, passenger_id, seat, seat_type, product_info)
    '''
    @required:
        segment_id
        passenger_id
        seat
        seat_type
        product_info
    @output:
        JSON object - passenger segment information
    '''
```

Product information item

```python
AirlineItinerary.product_info_item(title, value)
    '''
    @required:
        label
        value
    @output:
        Product information item - JSON object { "label": label, "value": value }
    '''
```

Price information item

```python
AirlineItinerary.price_info_item(title, amount, currency="")
    '''
    @required:
        title
        amount
    @optional:
        currency - USD by default?
    @output:
        Price information item - JSON object
```

Generating payload

```python
AirlineItinerary.get_payload(self)
```

### Receipt template ###
[Go to: Contents](#contents) 

[Description at Facebook Developers](https://developers.facebook.com/docs/messenger-platform/send-api-reference/receipt-template)

```python
 message = FBOrder(
     "Stephane Crozatier",
     "125352345",
     "USD",
     "Visa",
     [
         FBOrder.one_purchase("T-Shirt", 1,"yellow", 5, "USD", "http://cdn01.shopclues.net/images/detailed/19936/yellowtshirt_1434534567.jpg"),
         FBOrder.one_purchase("Baseball cap", 2,"white",  2, "USD", "http://i01.i.aliimg.com/img/pb/630/860/383/383860630_626.jpg")
     ],
     FBOrder.price_summary(9, 0, 1, 8),
     "http://google.com",
     FBOrder.address("1 Hacker Way", "", "Menlo Park", "94025", "CA", "US"),
     "427561765",
     [
         FBOrder.price_one_adjustment("2$ Off coupon", 2)
     ]
 )
 bot.send_message_TypeC(sender, message)
```

[![FBOrder example pic](http://ntarasov.ru/files/github/img/a3dmQg01DCk.jpg)]()
[![FBOrder example pic](http://ntarasov.ru/files/github/img/xg4hi1FwXDo.jpg)]()


### FBOrder class reference (Receipt template) ###
[Go to: Contents](#contents) 

```python
 
# Constructor  
FBOrder.__init__(self,
                recipient_name,  
                order_number,
                currency,
                payment_method,
                purchases_array,
                price_summary,
                order_url="",
                address="",
                timestamp="",
                price_adjustments_array="",
                **kwargs)
 
# Creates purchase JSON object
FBOrder.one_purchase(title,  price, subtitle="", quantity="",currency="", image_url="")
    '''
    @required:
        title  
        price
    @optional:
        subtitle
        quantity
        currency
        image_url
    '''
 
# Creates adress JSON object
FBOrder.address(street1, street2, city, postal_code, state, country)
    '''
    @required:
        street1
        street2
        city
        postal_code
        state
        country
    '''
 
# Creates summary JSON object
FBOrder.price_summary(subtotal, shipping_cost, total_tax, total_cost)
    '''
    @required:
        subtotal
        shipping_cost
        total_tax
        total_cost
    '''
 
# Creates price JSON object
FBOrder.price_one_adjustment(name, amount)
    '''
    @required:
        name
        amount
    '''
 
# Creates payload JSON object
FBOrder.get_payload(self)
 
 
```


### FBBot class reference ###
[Go to: Contents](#contents)

```python
# Constructor
FBBot.__init__(self, access_token, verify_token, **kwargs)
    '''
    @required:
        access_token
        verify_token
    @optional:
        api_version
        app_secret
    '''

# Receives information about user by id
FBBot.get_userinfo(self, user_id)
    '''
    @required:
        user_id
    '''

# 
FBBot.webhook(self, request, on_message_received, on_postback_received, on_account_linked="", on_account_unlinked="")
    '''
    @required:
        request
        on_message_received(sender_id, message_text, requestInfo)
        on_postback_received(sender_id, postback_text, requestInfo)
    @output:
        htmlView
    '''

# Sets bot greeting text for new users
FBBot.set_greeting_text(self, greeting_text)
    '''
    @required:
        greeting_text
    '''

# Sets the button that will be shown for new users
FBBot.set_get_started_button(self, postback_text)
    '''
    @required:
        postback_text
    @output
        response JSON
    '''

# Deletes "get started" button
FBBot.delete_get_started_button(self)

# Creates persistent menu with buttons
FBBot.set_persistent_menu(self, buttons):
    '''
    @required:
        buttons array, up to 5 buttons, each is FBAttachment.button
    @output:
        response_json
    '''
        
# Deletes persistent menu and returns response JSON
FBBot.delete_persistent_menu(self)

# Sends text message to recipient
FBBot.send_text_message(self, recipient_id, text, quick_replies = []) 
    '''
    @required:
        recipient_id
        text
    @optional:
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply
    @output:
        response_json
    '''

# Sends message with file attachment to recipient
FBBot.send_message_file_attachment(self, recipient_id, attachment_type, file_url, quick_replies = [])
    '''
    @required:
        recipient_id
        attachment_type from FBAttachment.File
        file_url
    @optional:
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply
    @output:
        response_json
    '''

# Sends generic message with image and buttons to recipient 
FBBot.send_message_generic(self, recipient_id, title, subtitle, image_url, buttons = [], quick_replies = [])
    '''
    @required:
        recipient_id
        title
        subtitle (may be empty string)
        image_url (may be empty string)
    @optional:
        buttons array, up to three buttons, each is FBAttachment.button
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply
    @output:
        response_json
    '''
   
# Sends template message to recipient
FBBot.send_message_TypeC(self, recipient_id, template, quick_replies = [])
    '''
    @required:
        recipient_id
        template is instance of FBOrder or AirlineChekin or AirlineFlightUpdate (Facebook templates)
    @optional:
        quick_replies array, up to ten replies, each is FBAttachment.quick_reply
    @output:
        response_json
    '''
```
