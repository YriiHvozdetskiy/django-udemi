from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # course_id - називаєм як хочем параметр маршрута, берем ід з url в браузері
    path('<int:course_id>', views.single_course, name='single_course'),
]
