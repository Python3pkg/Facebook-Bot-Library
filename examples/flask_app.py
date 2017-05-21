# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
from flask import request
from FBBlib.fbbot import FBBot
from FBBlib.order import FBOrder
from FBBlib.attachment import FBAttachment
from FBBlib.AirlineFlightUpdate import AirlineFlightUpdate
from FBBlib.AirlineCheckin import AirlineCheckin
from FBBlib.AirlineBoardingPass import AirlineBoardingPass
from FBBlib.AirlineItinerary import AirlineItinerary
#import FBBlib

token = ""
verify_token = ""

bot = FBBot(token, verify_token)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    return bot.webhook(request, on_message, on_postback, on_linked, on_unlinked)

def on_linked(sender, login, requestInfo):
    print("link")
    print((sender+" "+ login))

def on_unlinked(sender, requestInfo):
    print("unlink")
    print((sender+" unlink"))

def on_postback(sender, text, requestInfo):
    print("post")
    bot.send_text_message(sender, 'Received postback "{0}"'.format(text))

def on_message(sender, text, requestInfo):
    print("message")
    if(text == "Video"):
        bot.send_message_file_attachment(sender, FBAttachment.File.video, "http://img-9gag-fun.9cache.com/photo/adXLy8N_460sv.mp4")
    elif(text == "Image"):
        bot.send_message_file_attachment(sender, FBAttachment.File.image, "http://img-9gag-fun.9cache.com/photo/aEnxQve_460s_v1.jpg")
    elif(text == "Generic"):
        bot.send_message_generic(sender, "Generic message", "with image and button", "https://scontent.xx.fbcdn.net/t39.3138-6/p128x128/12056981_908479762570256_1493516739_n.jpg", 
                                 [ 
                                     FBAttachment.button_account_unlink()
                                 ])

    elif(text == "Receipt"):
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

    elif(text == "FirstAirline"):
        message = AirlineCheckin(
            "Checkin",
            "ru_RU",
            "12356",
            [
                AirlineCheckin.make_flight_info(
                    "4142",
                    AirlineCheckin.make_airport("SIN","Singapore"),
                    AirlineCheckin.make_airport("DME","Moscow"),
                    AirlineCheckin.make_flight_schedule("2016-01-05T15:05","2016-01-06T15:05")
                )
            ]
            ,"https://google.com")
        bot.send_message_TypeC(sender, message)

    elif(text == "SecondAirline"):
        message = AirlineFlightUpdate(
            "UPD",
            "delay",
            "ru_RU",
            "12356",
            AirlineFlightUpdate.make_update_flight_info(
                "4142",
                AirlineFlightUpdate.make_airport("SIN","Singapore"),
                AirlineFlightUpdate.make_airport("DME","Moscow"),
                AirlineFlightUpdate.make_flight_schedule("2016-01-05T15:05","2016-01-07T15:05")
            )
        )
        bot.send_message_TypeC(sender, message)

    elif(text == "ThirdAirline"):
        message = AirlineBoardingPass(
            "tickettohell",
            "ru_RU",
            [
                AirlineBoardingPass.boarding_pass_item(
                    "Michel",
                    "http://ausbb.com/1/celts049.jpg",
                    "SAV45",
                    "",
                    "http://www.swissarmylibrarian.net/wp-content/uploads/2011/02/barcodelunch.png",
                    "http://www.gettyimages.fr/gi-resources/images/Homepage/Hero/FR/FR_GI_40_Hero_Prestige169983008.jpg",
                    "business",
                    AirlineBoardingPass.flight_info(
                            "S582",
                            AirlineBoardingPass.airport("RER","Reikier"),
                            AirlineBoardingPass.airport("RED","Reifund"),
                            AirlineBoardingPass.flight_schedule("2016-01-05T15:05","2016-01-05T15:09")
                    )
                )
            ]
        )

        bot.send_message_TypeC(sender, message)


    elif(text == "ThirdAirline"):
        message = AirlineBoardingPass(
            "tickettohell",
            "ru_RU",
            [
                AirlineBoardingPass.boarding_pass_item(
                    "Michel",
                    "http://ausbb.com/1/celts049.jpg",
                    "SAV45",
                    "",
                    "http://www.swissarmylibrarian.net/wp-content/uploads/2011/02/barcodelunch.png",
                    "http://www.gettyimages.fr/gi-resources/images/Homepage/Hero/FR/FR_GI_40_Hero_Prestige169983008.jpg",
                    "business",
                    AirlineBoardingPass.flight_info(
                            "S582",
                            AirlineBoardingPass.airport("RER","Reikier"),
                            AirlineBoardingPass.airport("RED","Reifund"),
                            AirlineBoardingPass.flight_schedule("2016-01-05T15:05","2016-01-05T15:09")
                    )
                )
            ]
        )
        bot.send_message_TypeC(sender, message)

    elif(text == "4Airline"):
        message = AirlineItinerary(
            "tickettohell",
            "ru_RU",
            "EF52A",
            [
                AirlineItinerary.passenger_info_item("Mary","2472784","549"),
                AirlineItinerary.passenger_info_item("John","2472786","550")
            ],
            [
                AirlineItinerary.flight_info_item(
                    "cg001",
                    "c411",
                    "s582",
                    AirlineBoardingPass.airport("RER","Reikier"),
                    AirlineBoardingPass.airport("RED","Reifund"),
                    AirlineBoardingPass.flight_schedule("2016-01-05T15:05","2016-01-05T15:55"),
                    "econome",
                    "Aerobus 500"
                ),
                AirlineItinerary.flight_info_item(
                    "cg002",
                    "c412",
                    "s582",
                    AirlineBoardingPass.airport("RER","Reikier"),
                    AirlineBoardingPass.airport("RED","Reifund"),
                    AirlineBoardingPass.flight_schedule("2016-01-05T18:05","2016-01-05T19:55"),
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
    else:
        #bot.send_text_message(sender, str(requestInfo))
        #return 0
        bot.send_text_message(sender, "Hello, What do you want?",[ 
            FBAttachment.quick_reply("ThirdAirline"),
            FBAttachment.quick_reply("SecondAirline"),
            FBAttachment.quick_reply("FirstAirline"),
            FBAttachment.quick_reply("4Airline")
        ])
