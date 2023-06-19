from django.db import models

class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()

    def __str__(self):
        return f"{self.currency_code} - {self.exchange_rate} ({self.date})"

from django.db import models

class Country(models.Model):
    v_code = models.CharField(max_length=6, primary_key=True)
    v_country = models.CharField(max_length=64)
    v_currency = models.CharField(max_length=64)
    v_capitol = models.CharField(max_length=64)
    v_language = models.CharField(max_length=32)
    v_main_religion = models.CharField(max_length=32)
    v_currency_obj = models.ForeignKey('Currency', on_delete=models.CASCADE)
    v_main_religion_obj = models.ForeignKey('Religion', on_delete=models.CASCADE)

class Currency(models.Model):
    v_currency = models.CharField(max_length=64, primary_key=True)
    v_countries = models.CharField(max_length=64)
    v_code = models.CharField(max_length=8)

class Map(models.Model):
    v_country = models.ForeignKey('Country', on_delete=models.CASCADE)
    v_map = models.CharField(max_length=128)

class Religion(models.Model):
    v_religion = models.CharField(max_length=32, primary_key=True)

class CurrencyRateNBP(models.Model):
    v_date = models.DateField()
    v_currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    v_currency_rate = models.DecimalField(max_digits=10, decimal_places=2)


