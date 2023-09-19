from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        
    

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print("disconnected  ",code)
    
    async def receive(self, text_data):
        print(text_data)
        print(type(text_data))
        new = {'message':text_data}
        print(type(new))
        str_data = json.dumps(new)
        print(type(str_data))
        data = json.loads(str_data)
        message = data['message']

        await self.send_message(message)
        print("data: ",text_data)


    async def chat_message(self,event):

        message = event['message']
        print(message)
        print("chat message")
        await self.send(text_data=json.dump({
            'message':message
        }))

    async def send_message(self,message):
        user = self.scope['user']
        print("send message")
        await self.channel_layer.group_send(
            
            {
                'type':'chat_message',
                'message':message
            }
        )
