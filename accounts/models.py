from django.db import models

from currencies.models import Currency


class AccountType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    balance = models.DecimalField(max_digits=12, decimal_places=2)

    type = models.ForeignKey('AccountType', on_delete=models.CASCADE)

    open_date = models.DateField(blank=True, null=True)
    valid_till = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.currency.code}'


class CreditCard(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='credit_card')
    limit = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.account.name}, limit: {self.limit}'
