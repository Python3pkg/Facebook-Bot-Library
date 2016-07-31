# -*- coding: utf-8 -*-
class FBOrder(object):
    def __init__(self, recipient_name, order_number, currency, payment_method, purchases_array, price_summary, order_url="", address="", timestamp="", price_adjustments_array="", **kwargs):
        self.recipient_name = recipient_name
        self.order_number = order_number
        self.currency = currency
        self.payment_method = payment_method
        self.order_url = order_url
        self.timestamp = timestamp
        self.purchases = purchases_array
        self.address = address
        self.price_summary = price_summary
        self.price_adjustments = price_adjustments_array

    def one_purchase(title,  price, subtitle="", quantity="",currency="", image_url=""):
        return {
            "title":title,
            "subtitle":subtitle,
            "quantity":quantity,
            "price":price,
            "currency":currency,
            "image_url":image_url
        }

    def address(street1, street2, city, postal_code, state, country):
        return {
            "street_1":street1,
            "street_2":street2,
            "city":city,
            "postal_code":postal_code,
            "state":state,
            "country":country
        }

    def price_summary(subtotal, shipping_cost, total_tax, total_cost):
        return {
            "subtotal":subtotal,
            "shipping_cost":shipping_cost,
            "total_tax":total_tax,
            "total_cost":total_cost
        }

    def price_one_adjustment(name, amount):
        return {
            "name":name,
            "amount":amount
        }

    def get_payload(self):
        return {
            "template_type":"receipt",
            "recipient_name":self.recipient_name,
            "order_number":self.order_number,
            "currency":self.currency,
            "payment_method":self.payment_method,
            "order_url":self.order_url,
            "timestamp":self.timestamp,
            "elements":self.purchases,
                    #{
                    #  "title":"Classic White T-Shirt",
                    #  "subtitle":"100% Soft and Luxurious Cotton",
                    #  "quantity":2,
                    #  "price":50,
                    #  "currency":"USD",
                    #  "image_url":"http://petersapparel.parseapp.com/img/whiteshirt.png"
                    #}
            "address":self.address,
            "summary":self.price_summary,
            "adjustments":self.price_adjustments
        }


