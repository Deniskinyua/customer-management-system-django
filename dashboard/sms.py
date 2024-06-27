# works with both python 2 and 3
from __future__ import print_function
import africastalking
from django.conf import settings


class SMS:
    def __init__(self):
        # Set your app credentials
        user_name=  "sandbox"
        apiKey="atsk_e80d6ed142d643723aae5a75efa39b7035bd25f9cf27e44318b4bec6bca8b2a406be8705"

        self.username=  user_name#settings.USER_NAME
        self.api_key= apiKey #settings.API_KEY

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
            # Set the numbers you want to send to in international format
            recipients = ["+254724254505"]

            # Set your message
            message = "Your order has been placed";

            # Set your shortCode or senderId
            sender = "13842"
            try:
				# Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()
