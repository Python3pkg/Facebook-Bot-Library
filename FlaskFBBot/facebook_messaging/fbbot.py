import json
import hashlib
import hmac
import requests

#https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions

class FBBot(object):
    def __init__(self, access_token, verify_token, **kwargs):
        '''
            @required:
                access_token
                verify_token
            @optional:
                api_version
                app_secret
        '''
        self.access_token = access_token
        self.verify_token = verify_token

        self.api_version = kwargs.get('api_version') or 2.6
        self.app_secret = kwargs.get('app_secret')

        self.graph_url = 'https://graph.facebook.com/v{0}'.format(self.api_version)
        self.request_endpoint = '{0}/me/messages'.format(self.graph_url)
        
    @property
    def auth_args(self):
        if not hasattr(self, '_auth_args'):
            auth = {
                'access_token': self.access_token
            }
            if self.app_secret is not None:
                auth['appsecret_proof'] = self.appsecret_proof
            self._auth_args = auth
        return self._auth_args

    @property
    def appsecret_proof(self):
        '''
            @output:
                appsecret_proof: HMAC-SHA256 hash of page access token using app_secret as the key
        '''
        hmac_object = hmac.new(str(self.app_secret), unicode(self.access_token), hashlib.sha256)
        generated_hash = hmac_object.hexdigest()
        return generated_hash

    def webhook(self, request, on_message_received, on_postback_received):
        '''
            @required:
                request
                on_message_received(sender_id, message_text, requestInfo)
                on_postback_received(sender_id, postback_text, requestInfo)
            @output:
                htmlView
        '''
        if request.method == 'GET':
            if (request.args.get("hub.verify_token") == self.verify_token):
                    return request.args.get("hub.challenge")
            return "wrong verify_token in GET request"

        if request.method == 'POST':
            output = request.json
            event = output['entry'][0]['messaging']
            for x in event:
                sender_id = x['sender']['id']
                if (x.get('message') and x['message'].get('text')):
                    message = 'empty' if (not ('message' in x) or not ('text' in x['message'])) else x['message']['text']
                    on_message_received(sender_id, message, x)
                elif (x.get('postback') and x['postback'].get('payload')):
                    on_postback_received(sender_id, x['postback']['payload'], x)

            return "success"

    def send_text_message(self, recipient_id, text, quick_replies = []):
        '''
            @required:
                recipient_id
                text
            @optional:
                quick_replies array, up to ten replies, each is FBAttachment.quick_reply...
            @output:
                response_json
        '''
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': text
            } if not quick_replies else {
                'text': text,
                'quick_replies': quick_replies
            }
        }
        return self._send_payload(payload)

    def send_message_file_attachment(self, recipient_id, attachment_type, file_url, quick_replies = []):
        '''
            @required:
                recipient_id
                attachment_type from FBAttachment.File
                file_url
            @optional:
                quick_replies array, up to ten replies, each is FBAttachment.quick_reply...
            @output:
                response_json
        '''
        attachment = {
            "type": attachment_type,
            "payload": {
              "url": file_url
            }
        }
        return self._send_message(recipient_id, attachment, quick_replies)
        
    def send_message_generic(self, recipient_id, title, subtitle, image_url, buttons = [], quick_replies = []):
        '''
            @required:
                recipient_id
                title
                subtitle (may be empty string)
                image_url (may be empty string)
            @optional:
                buttons array, up to three buttons, each is FBAttachment.button...
                quick_replies array, up to ten replies, each is FBAttachment.quick_reply...
            @output:
                response_json
        '''
        attachment = {
            "type": "template",
            "payload": {
            "template_type": "generic",
            "elements": [ 
                {
                    "title": title,
                    "image_url": image_url,
                    "subtitle": subtitle
                } if not buttons else {
                    "title": title,
                    "image_url": image_url,
                    "subtitle": subtitle,
                    "buttons": buttons
                } 
            ]
            }
        }
        return self._send_message(recipient_id, attachment, quick_replies)

    def send_message_buttons(self, recipient_id, text, buttons, quick_replies = []):
        '''
            @required:
                recipient_id
                text
                buttons array, up to three buttons, each is FBAttachment.button...
            @optional:
                quick_replies array, up to ten replies, each is FBAttachment.quick_reply...
            @output:
                response_json
        '''
        attachment = {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": text,
                "buttons": buttons
            }
        }
        return self._send_message(recipient_id, attachment, quick_replies)

    def send_message_receipt(self, recipient_id, fborder, quick_replies = []):
        '''
            @required:
                recipient_id
                fborder is instance of FBOrder
            @optional:
                quick_replies array, up to ten replies, each is FBAttachment.quick_reply...
            @output:
                response_json
        '''
        attachment = {
            "type":"template",
            "payload":fborder.get_payload()
        }
        return self._send_message(recipient_id, attachment, quick_replies)

    def _send_message(self, recipient_id, attachment, quick_replies = []):
        '''
            @required:
                recipient_id
                attachment
            @optional:
                quick_replies array, up to ten replies, each is FBAttachment.quick_reply...
            @output:
                response_json
        '''
        payload = {
                'recipient': {
                    'id': recipient_id
                },
                'message': {
                    'attachment': attachment
                } if not quick_replies else {
                    'attachment': attachment,
                    'quick_replies': quick_replies
                }
            }
        return self._send_payload(payload)
    
    def _send_payload(self, payload):
        '''
            @required:
                payload
        '''
        response = requests.post(
            self.request_endpoint,
            params=self.auth_args,
            json=payload
        )
        #print ('Response result: '+str(response.json()))
        return response.json()