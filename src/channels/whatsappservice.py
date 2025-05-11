from twilio.rest import Client
from src.config import AppConfig

class WhatsAppService:
    def __init__(self):
        """
        Initializes the Twilio client for sending WhatsApp messages.

        :param account_sid: Your Twilio account SID.
        :param auth_token: Your Twilio auth token.
        :param twilio_whatsapp_number: Your Twilio sandbox WhatsApp number in the format 'whatsapp:+<Twilio-Number>'.
        """
        
        self.appConfig = AppConfig()
        
        account_sid = self.appConfig.twillio_account_number
        auth_token = self.appConfig.twillio_auth_token
        self.client = Client(account_sid, auth_token)
        

    def send_whatsapp_message(self, to_whatsapp_number, message_body):
        """
        Sends a WhatsApp message using Twilio.

        :param to_whatsapp_number: The recipient's WhatsApp number in the format 'whatsapp:+<Recipient-Number>'.
        :param message_body: The message content to be sent.
        """
        try:
            message = self.client.messages.create(
                body=message_body,
                from_=self.appConfig.twillio_whatsapp_number,
                to=to_whatsapp_number
            )

            print(f"Message sent successfully with SID: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")
