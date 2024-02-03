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
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category
        return bundle
