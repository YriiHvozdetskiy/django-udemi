from tastypie.resources import ModelResource
from shop.models import Category, Course

"""
моделі в термені api - ресурси
"""


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()  # отримуємо з бази даних
        resource_name = 'categories'  # імя яке буде в маршруті: api/categories
        allowed_methods = ['get']  # які REST методи дозволяємо


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()  # отримуємо з бази даних
        resource_name = 'courses'  # імя яке буде в маршруті: api/courses
        allowed_methods = ['get', 'post', 'delete']  # які REST методи дозволяємо
