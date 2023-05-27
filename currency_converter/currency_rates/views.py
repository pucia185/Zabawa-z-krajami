from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import CurrencyRate
from .utils import fetch_currency_rates, fetch_time_currency_rates


def fetch_and_save_currency_rates(request):
    data = fetch_currency_rates()
    if data:
        CurrencyRate.objects.all().delete()

        for currency in data[0]['rates']:
            currency_rate = CurrencyRate(
                currency_code=currency['code'],
                exchange_rate=currency['mid'],
                date=data[0]['effectiveDate']
            )
            currency_rate.save()
    return TemplateResponse(request, 'currency_rates/fetch.html')

def show_currency_rates(request):
    currency_rates = CurrencyRate.objects.all()
    return TemplateResponse(request, 'currency_rates/rates.html', {'currency_rates': currency_rates})

def fetch_currency_data(request):
    if request.method == 'GET':
        currency_rates = CurrencyRate.objects.all()
        return TemplateResponse(request, 'currency_rates/data_sheet.html', {'currency_rates': currency_rates})
    elif request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        currency = request.POST.get('currency')

        data = fetch_time_currency_rates(start_date, end_date)
        filtered_data = []

        if data:
            for currency_data in data:
                for rate in currency_data['rates']:
                    if currency == 'all' or rate.get('code') == currency:
                        currency_rate = CurrencyRate(
                            currency_code=rate.get('code'),
                            exchange_rate=rate.get('mid'),
                            date=currency_data['effectiveDate']
                        )
                        filtered_data.append(currency_rate)

        currency_rates = CurrencyRate.objects.all()
        return TemplateResponse(request, 'currency_rates/data_sheet.html',
                      {'currency_rates': currency_rates, 'filtered_data': filtered_data})
    return TemplateResponse(request, 'currency_rates/data_sheet.html')

def fetch_currency(request):
    return TemplateResponse(request, 'currency_rates/data_sheet.html')


def home_page(request):
    return TemplateResponse(request, 'currency_rates/homepage.html')