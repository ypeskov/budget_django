from django.db import models

from budget.models import BaseModel


class Currency(BaseModel):
    code = models.CharField(max_length=3, blank=False, db_comment='3 symbols comments', unique=True)
    numeric_code = models.SmallIntegerField(blank=True, null=True, unique=True)
    name = models.CharField(max_length=50, blank=False, db_comment='English name of the currency')
    symbol = models.CharField(max_length=5, blank=True, db_comment='symbol of currency')

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.code


class ExchangeRateCurrent(BaseModel):
    currency1 = models.ForeignKey(Currency, related_name='sold_currency', on_delete=models.PROTECT)
    currency2 = models.ForeignKey(Currency, related_name='bought_currency', on_delete=models.PROTECT)
    rate_buy = models.DecimalField(max_digits=16, decimal_places=6)
    rate_sell = models.DecimalField(max_digits=16, decimal_places=6)

    def __str__(self):
        return f'{self.currency1}:{self.currency2} {self.rate_buy}:{self.rate_sell}'

    class Meta:
        verbose_name = 'current exchange rates'
        verbose_name_plural = 'current exchange rates'


class ExchangeRateHistory(ExchangeRateCurrent):
    rate_date = models.DateTimeField()

    class Meta:
        verbose_name = 'history of exchange rates'
        verbose_name_plural = 'history of exchange rates'

    def __str__(self):
        return f'{super().__str__()} on {self.rate_date}'
