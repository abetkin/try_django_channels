from channels.generic.websocket import JsonWebsocketConsumer

import time

from threading import Thread
import random

from app.models import Int

class MyConsumer(JsonWebsocketConsumer):
    
    RATIO = 10

    light = heavy = 0

    def receive(self, text_data=None, bytes_data=None):
        if text_data == 'request':
            if random.randrange(self.RATIO):
                self.send_json([])
                self.__class__.light += 1
            else:
                ids = Int.objects.filter(value__lt=333).values_list('id')
                self.send_json(list(ids))
                self.__class__.heavy += 1
                
        elif text_data == 'stats':
            self.send_json({
                'light': self.light, 'heavy': self.heavy
            })
