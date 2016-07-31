# -*- coding: utf-8 -*-

def remove_empty_values(d):
    removeList = [];
    for key, value in d.items():
        if value == "":
            removeList.append(key)
    for key in removeList:
        del d[key]
    return d

class AirlineBoardingPass(object):
    def __init__(self, intro_message, locale, boarding_pass, theme_color=""):
        self.intro_message = intro_message
        self.locale = locale
        self.boarding_pass = boarding_pass
        self.theme_color = theme_color


    def boarding_pass_item(passenger_name, logo_image_url,pnr_number, qr_code, barcode_image_url, above_bar_code_image_url, travel_class,flight_info,header_image_url="", header_text_field="", seat="", auxiliary_fields="",secondary_fields=""):
        return remove_empty_values({
            "passenger_name": passenger_name,
            "logo_image_url": logo_image_url,
            "pnr_number": pnr_number,
            "qr_code":qr_code,
            "barcode_image_url": barcode_image_url,
            "above_bar_code_image_url": above_bar_code_image_url,
            "flight_info": flight_info,
            "header_image_url":header_image_url,
            "header_text_field":header_text_field,
            "travel_class": travel_class,
            "seat": seat,
            "auxiliary_fields":auxiliary_fields,
            "secondary_fields":secondary_fields
        })

    def flight_schedule(departure_time, arrival_time, boarding_time=""):
         return remove_empty_values({
            "departure_time":departure_time,
            "arrival_time":arrival_time,
            "boarding_time":boarding_time
         })


    def flight_info(flight_number, departure_airport, arrival_airport, flight_schedule, aircraft_type=""):
        return remove_empty_values({
            "flight_number":flight_number,
            "aircraft_type":aircraft_type,
            "departure_airport":departure_airport,
            "arrival_airport":arrival_airport,
            "flight_schedule":flight_schedule
         })


    def airport(airport_code, city, terminal="", gate=""):
         return remove_empty_values({
            "airport_code":airport_code,
            "city":city,
            "terminal":terminal,
            "gate":gate
         })

    def field(label, value):
    # for auxiliary_fields and secondary_fields, they are array of fields
        return remove_empty_values({
            "label":label,
            "value":value
        })


    def get_payload(self):
        return remove_empty_values({
                "template_type":"airline_boardingpass",
                "intro_message":self.intro_message,
                "locale": self.locale,
                "boarding_pass": self.boarding_pass,
                "theme_color":self.theme_color
        })
