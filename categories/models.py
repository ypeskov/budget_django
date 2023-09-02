from django.contrib.auth.models import User
from django.db import models

from budget.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Category')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children',
                               verbose_name='parent',
                               null=True, blank=True)

    type = models.CharField(max_length=10,
                            choices=[('income', 'Income'), ('expense', 'Expense'), ('transfer', 'Transfer')])

    def __str__(self):
        parent_name = f' ({self.parent})' if self.parent else ''
        return f'{self.name}{parent_name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class UserCategory(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_categories')
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    type = models.CharField(max_length=10,
                            choices=[('income', 'Income'), ('expense', 'Expense'), ('transfer', 'Transfer')])

    def __str__(self):
        parent_name = f' ({self.parent})' if self.parent else ''
        return f'{self.name}{parent_name}'

    class Meta:
        verbose_name = 'user category'
        verbose_name_plural = 'user categories'
