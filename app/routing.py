from django.urls import path
from . import consumers

websocketurl_patterns = [
    path('ws/chat/<str:room_name>/',consumers.ChatConsumer.as_asgi()),

]