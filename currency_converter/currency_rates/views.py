from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .models import CurrencyRate
from .utils import fetch_currency_rates, fetch_time_currency_rates
from .models import Country, Map
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


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
        currencyx = request.POST.get('currency')

        data = fetch_time_currency_rates(start_date, end_date)
        filtered_data = []

        if data:
            for currency_data in data:
                for rate in currency_data['rates']:
                    if currencyx == 'all' or rate.get('code') == currencyx:
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

def country_list(request):
    countries = Country.objects.values('v_country')
    return render(request, 'currency_rates/country_list.html', {'countries': countries})

def currency_(request):
    return TemplateResponse(request, 'currency_rates/currency.html')


def info(request):
    countries = Country.objects.all()
    return render(request, 'currency_rates/info_country.html', {'countries': countries})


class CountryDetailView(DetailView):
    model = Country
    template_name = 'currency_rates/info_country.html'
    context_object_name = 'country'

    def get_object(self, queryset=None):
        country_name = self.kwargs.get('country_name')
        country = get_object_or_404(Country, v_country=country_name)
        return country
def maps(request):
    countries = Map.objects.all()
    return render(request, 'currency_rates/maps.html', {'countries': countries})


def search_country(request):
    if 'country_name' in request.GET:
        country_name = request.GET['country_name']
        try:
            country = Country.objects.get(Q(v_country__iexact=country_name))
            return redirect('country_detail', country_name=country.v_country)
        except ObjectDoesNotExist:
            message = "Kraj o nazwie {} nie istnieje lub nie ma go w bazie danych.".format(country_name)
            return render(request, 'currency_rates/homepage.html', {'message': message})
    return redirect('home_page')
