import plivo
from sqlalchemy import func

def sendTextMessage(auth_id,auth_token,sender_id,destination_number,secretKey):
    client = plivo.RestClient(f'{auth_id}',f'{auth_token}')
    response = client.messages.create(
        src=f'{sender_id}',
        dst=f'{destination_number}',
        text=f'Your key is: {secretKey}',)
    print(response)

# 1-518-635-0270
# 


sendTextMessage("")