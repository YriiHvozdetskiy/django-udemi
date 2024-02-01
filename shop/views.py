from django.shortcuts import render
from django.http import HttpResponse

# from . import models  # імпортуємо з поточної папки весь модуль "models"
# or
from .models import Course, Category  # Імпортуємо конкретні модулі (. показує що це з поточної папки)

"""
views - це контролер/інтерфейс в патерні MVC
звязує частину яку ми бачимо з models
- виконують прийом запитів від користувача і передачу відповіді користувачу
"""


# Create your views here.
#  опрацьовуєм звернення на головну сторінку(shop)
def index(request):  # функція виду
    courses = Course.objects.all()  # отримання всіх курсів
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))  # виводимо через br один під одним
    # return HttpResponse(courses)
    return render(request, 'courses.html', )
