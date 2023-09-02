from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, blank=False, db_comment='3 symbols comments', unique=True)
    numeric_code = models.SmallIntegerField(blank=True, null=True, unique=True)
    name = models.CharField(max_length=50, blank=False, db_comment='English name of the currency')
    symbol = models.CharField(max_length=5, blank=True, db_comment='symbol of currency')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.code
