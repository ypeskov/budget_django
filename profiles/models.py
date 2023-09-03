from django.db import models
from django.conf import settings

from budget.models import BaseModel
from currencies.models import Currency


class Profile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    base_currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    def __str__(self):
        return f'Profile of {self.user.username}'
