import smtplib

from variables import recv_email , sender_email , password

recv_email = recv_email
sender_email = sender_email
password = password
#password = input(str("Please entyer your password :"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, password)
print("login success")
server.sendmail(sender_email, recv_email, "this is from rahul from data sceince , Your model is deployed successfully.................")
print("email has been sent to : " , recv_email)
