import os
from twilio.rest import Client

from variables import account_sid, auth_token , my_phone_num

Client = Client(account_sid, auth_token)
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:' + my_phone_num

Client.messages.create(
    body='this is from rahul from data sceince , Your model is deployed successfully.................',
    from_ = from_whatsapp_number,
    to = to_whatsapp_number
)