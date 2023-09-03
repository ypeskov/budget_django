from django.contrib.auth.models import User
from django.db import models

from budget.models import BaseModel
from categories.models import UserCategory
from currencies.models import Currency
from accounts.models import Account


class Operation(BaseModel):
    EXPENSE = 'EXPENSE'
    INCOME = 'INCOME'
    TRANSFER = 'TRANSFER'
    OPERATION_TYPES = (
        (EXPENSE, 'expense'),
        (INCOME, 'income'),
        (TRANSFER, 'transfer')
    )

    label = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, choices=OPERATION_TYPES, default=EXPENSE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operations')
    category = models.ForeignKey(UserCategory, on_delete=models.CASCADE, related_name='operations')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='amount')
    op_date = models.DateTimeField(auto_now_add=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    source_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='source_accounts')
    destination_account = models.ForeignKey(Account, on_delete=models.CASCADE,
                                            related_name='destination_accounts', blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}:{self.label}, {self.amount}{self.currency}, from {self.source_account.name}'

    class Meta:
        verbose_name = 'Operation'
        verbose_name_plural = 'Operations'
