from twilio.rest import Client 
from variables import my_phone_num, account_sid , auth_token
 
account_sid = account_sid
auth_token = auth_token
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  

    from_ = "(312) 624-6948" , 
    body  = "hello, this is from rahul from data sceince , Your model is deployed successfully................."  , 
    to= my_phone_num 
      ) 
 
print(message.sid)