# -*- coding: utf-8 -*-

def remove_empty_values(d):
    removeList = [];
    for key, value in d.items():
        if value == "":
            removeList.append(key)
    for key in removeList:
        del d[key]
    return d

class AirlineItinerary(object):
    def __init__(self, intro_message, locale, pnr_number, passenger_info, flight_info, passenger_segment_info, total_price, currency, theme_color="", price_info="", base_price="", tax=""):
        self.intro_message = intro_message
        self.locale = locale
        self.pnr_number = pnr_number
        self.passenger_info = passenger_info
        self.flight_info = flight_info
        self.passenger_segment_info = passenger_segment_info
        self.total_price = total_price
        self.currency = currency
        self.theme_color = theme_color
        self.price_info = price_info
        self.base_price = base_price
        self.tax = tax


    def passanger_info_item(name, passenger_id,ticket_number=""): #!!!
        return remove_empty_values({
            "name": name,
            "ticket_number": ticket_number,
            "passenger_id": passenger_id
        })


    def flight_info_item(connection_id, segment_id, flight_number, departure_airport, arrival_airport, flight_schedule, travel_class, aircraft_type=""): #!!!!
        return remove_empty_values({
            "connection_id":connection_id,
            "segment_id":segment_id,
            "flight_number":flight_number,
            "aircraft_type":aircraft_type,
            "departure_airport":departure_airport,
            "arrival_airport":arrival_airport,
            "flight_schedule":flight_schedule,
            "travel_class":travel_class
         })


    def airport(airport_code, city, terminal="", gate=""):
         return remove_empty_values({
            "airport_code":airport_code,
            "city":city,
            "terminal":terminal,
            "gate":gate
         })


    def flight_schedule(departure_time, arrival_time, boarding_time=""):
         return remove_empty_values({
            "departure_time":departure_time,
            "arrival_time":arrival_time,
             "boarding_time":boarding_time
         })


    def passenger_segment_info_item(segment_id, passenger_id, seat, seat_type, product_info):
        return remove_empty_values({
            "segment_id":segment_id,
            "passenger_id":passenger_id,
            "seat":seat,
            "seat_type":seat_type,
            "product_info":product_info
        })

    def product_info_item(title, value):
        return remove_empty_values({
            "title":title,
            "value":value
        })


    def price_info_item(title, amount, currency=""):
        return remove_empty_values({
            "title":title,
            "amount":amount,
            "currency":currency
        })

    def get_payload(self):
        return remove_empty_values({
                "template_type":"airline_itinerary",
                "intro_message":self.intro_message,
                "locale": self.locale,
                "pnr_number": self.pnr_number,
                "passenger_info":self.passenger_info,
                "flight_info": self.flight_info,
                "passenger_segment_info":self.passenger_segment_info,
                "price_info":self.price_info,
                "base_price":self.base_price,
                "tax":self.tax,
                "total_price":self.total_price,
                "currency": self.currency,
                "theme_color":self.theme_color
        })
