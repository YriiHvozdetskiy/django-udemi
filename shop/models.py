from django.db import models
from django.utils import timezone

"""
моделі для взаємодії з базою
"""


# наслідуємося від models.Model для роботи з базою даних
class Category(models.Model):
    # вказуєм які поля будуть в базі даних
    title = models.CharField(max_length=255)  # текстове(str) поле
    created_at = models.DateTimeField(default=timezone.now)  # дата буде створюватися автоматично

    # для відображення заголовка в адмінці
    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews = models.IntegerField()
    # ForeignKey ключ з другої таблиці, on_delete=models.CASCADE - при видалені певної категорії,
    # автоматично будуть видалені всі курси в цій категорії. Так звязали курс з категоріями
    categoty = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  # дата буде створюватися автоматично

    # для відображення заголовка в адмінці
    def __str__(self):
        return f"{self.title} price {self.price}"
