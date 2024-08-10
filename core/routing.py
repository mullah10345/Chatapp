from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/story/<int:story_id>/', consumers.StoryConsumer.as_asgi()),
]
