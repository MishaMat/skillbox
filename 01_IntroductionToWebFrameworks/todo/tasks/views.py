from django.http import HttpResponse
import random
from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            f'<center><li>{random.randint(0,10)}Установить python</li>'
                            '<li>Установить django</li>'
                            '<li>Запустить сервер</li>'
                            '<li>Порадоваться результату</li>'
                            '<li>fuck  off bitch</li></center>'
                            '</ul>')
