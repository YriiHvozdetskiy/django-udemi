from django.shortcuts import render
from django.http import HttpResponse

"""
views - це контролер в патерні MVC
звязує частину яку ми бачимо з models
- виконують прийом запитів від користувача і передачу відповіді користувачу
"""


# Create your views here.
#  опрацьовуєм звернення на головну сторінку(shop)
def index(request):  # функція виду
    return HttpResponse('Hello from the Shop app')
