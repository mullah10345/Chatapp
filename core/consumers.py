import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.story_id = self.scope['url_route']['kwargs']['story_id']
        self.story_group_name = f'story_{self.story_id}'

        # Join the story group
        await self.channel_layer.group_add(
            self.story_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the story group
        await self.channel_layer.group_discard(
            self.story_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send the message to the story group
        await self.channel_layer.group_send(
            self.story_group_name,
            {
                'type': 'story_message',
                'message': message
            }
        )

    async def story_message(self, event):
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
