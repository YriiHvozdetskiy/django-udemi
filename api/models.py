from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication

"""
моделі в термені api - ресурси

Authentication - вказує що можна робити корисувачу який вже прийшов авторизацію
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
        excludes = ['reviews', 'created_at']  # виключаєм поля які йдуть на клієнт
        authentication = CustomAuthentication()
        authorization = Authorization()

    # hydrate - дані приходять від клієнта і йдуть на сервер
    def hydrate(self, bundle):
        print(f"bundle {bundle}")
        # bundle <Bundle for obj: '<Course:  price None>' and with data: '{'price': 20.0, 'resource_uri': '/api/v1/courses/2/', 'reviews': 10, 'students_qty': 10, 'title': 'Complete Java', 'category_id': 1}'>
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    # dehydrate - дані йдуть від сервера до клієнта
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category
        return bundle

    def dehydrate_title(self, bundle):
        print(f"bundle {bundle}")
        # bundle <Bundle for obj: '<Course: Complete Python price 89.99>' and with data: '{'resource_uri': '/api/v1/courses/1/', 'id': 1, 'title': 'Complete Python'}'>
        return bundle.data['title'].upper()
