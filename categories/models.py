from django.contrib.auth.models import User
from django.db import models

from budget.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=10,
                            choices=[('income', 'Income'), ('expense', 'Expense'), ('transfer', 'Transfer')])


class UserCategory(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_categories')
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('UserCategory', on_delete=models.SET_NULL, related_name='children', null=True)
    type = models.CharField(max_length=10,
                            choices=[('income', 'Income'), ('expense', 'Expense'), ('transfer', 'Transfer')])
