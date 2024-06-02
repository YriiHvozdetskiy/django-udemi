from django.urls import path
from . import views

app_name = 'shop'  # назва приложенія(використовується в навігації в templates)

urlpatterns = [
    path('', views.index, name='index'),  # name=* - назва ф-ції виду в views.py
    # course_id - називаєм як хочем параметр маршрута, берем ід з url в браузері
    path('<int:course_id>', views.single_course, name='single_course'),  # name=* - назва ф-ції виду в views.py
]
