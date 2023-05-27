from django.db import models

class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()

    def __str__(self):
        return f"{self.currency_code} - {self.exchange_rate} ({self.date})"
