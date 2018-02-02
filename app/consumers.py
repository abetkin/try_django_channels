from channels.generic.websocket import JsonWebsocketConsumer

import time
from threading import Thread
import random

from app.models import Int

class MyConsumer(JsonWebsocketConsumer):
    
    def receive(self, text_data=None, bytes_data=None):
        if text_data == 'request':
            if random.randrange(5):
                self.send_json([])
            else:
                ids = Int.objects.filter(value__gt=333).values_list('id')
                self.send_json(list(ids))
        
