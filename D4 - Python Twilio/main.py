from twilio.rest import Client 
 
account_sid = 'AC39e53d8e3c849c100e8b3b288d29cfbc' 
auth_token = 'ea0ed3081eb5a25b376b158ea7dfb634' 
client = Client(account_sid, auth_token) 

def send_msg():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Hello?',      
                                to='whatsapp:+918699541332' 
                            ) 
    
    print(message.sid)
