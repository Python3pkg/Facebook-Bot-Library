# -*- coding: utf-8 -*-

def remove_empty_values(d):
    removeList = [];
    for key, value in d.items():
        if value == "":
            removeList.append(key)
    for key in removeList:
        del d[key]
    return d

class AirlineCheckin(object):
    def __init__(self, intro_message, locale, pnr_number, flight_info, checkin_url, theme_color=""):
        self.intro_message = intro_message
        self.locale = locale
        self.pnr_number = pnr_number
        self.flight_info = flight_info
        self.checkin_url = checkin_url
        self.theme_color = theme_color



    def make_flight_info(flight_number, departure_airport, arrival_airport, flight_schedule):
        return remove_empty_values({
            "flight_number":flight_number,
            "departure_airport":departure_airport,
            "arrival_airport":arrival_airport,
            "flight_schedule":flight_schedule
         })


    def make_flight_info_item(flight_number, departure_airport, arrival_airport, flight_schedule):
         return remove_empty_values({
            "flight_number":flight_number,
            "departure_airport":departure_airport,
            "arrival_airport":arrival_airport,
            "flight_schedule":flight_schedule
         })



    def make_airport( airport_code, city, terminal="", gate=""):
         return remove_empty_values({
            "airport_code":airport_code,
            "city":city,
            "terminal":terminal,
            "gate":gate
         })


    def make_flight_schedule(departure_time, arrival_time, boarding_time=""):
         return remove_empty_values({
            "departure_time":departure_time,
            "arrival_time":arrival_time,
            "boarding_time":boarding_time
         })


    def get_payload(self):
        return remove_empty_values({
                "template_type":"airline_checkin",
                "intro_message":self.intro_message,
                "locale": self.locale,
                "pnr_number": self.pnr_number,
                "flight_info": self.flight_info,
                "checkin_url": self.checkin_url,
                "theme_color":self.theme_color
        })
