from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

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

    # {'courses': courses} - контекст потрапляє в templates
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):  # функція виду
    # # OPTION 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'shop/single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()

    # OPTION 2
    course = get_object_or_404(Course, pk=course_id)  # - контекст потрапляє в templates
    return render(request, 'shop/single_course.html', {'course': course})
