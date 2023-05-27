from django.test import TestCase
from django.http import HttpRequest
from django.template.response import TemplateResponse
from unittest.mock import patch
from datetime import date, datetime
from currency_rates.models import CurrencyRate
from currency_rates.views import fetch_and_save_currency_rates, show_currency_rates, fetch_currency_data, fetch_currency, home_page



class CurrencyRatesTestCase(TestCase):
    @patch('currency_rates.views.fetch_currency_rates')
    def test_fetch_and_save_currency_rates(self, mock_fetch_currency_rates):
        mock_data = [
            {
                'rates': [
                    {'code': 'THB', 'mid': 1.0},
                    {'code': 'USD', 'mid': 1.0},
                    {'code': 'AUD', 'mid': 1.0},
                    {'code': 'HKD', 'mid': 1.0},
                    {'code': 'CAD', 'mid': 1.0},
                    {'code': 'NZD', 'mid': 1.0},
                    {'code': 'SGD', 'mid': 1.0},
                    {'code': 'EUR', 'mid': 1.0},
                    {'code': 'HUF', 'mid': 1.0},
                    {'code': 'CHF', 'mid': 1.0},
                    {'code': 'GBP', 'mid': 1.0},
                    {'code': 'UAH', 'mid': 1.0},
                    {'code': 'JPY', 'mid': 1.0},
                    {'code': 'CZK', 'mid': 1.0},
                    {'code': 'DKK', 'mid': 1.0},
                    {'code': 'ISK', 'mid': 1.0},
                    {'code': 'NOK', 'mid': 1.0},
                    {'code': 'SEK', 'mid': 1.0},
                    {'code': 'RON', 'mid': 1.0},
                    {'code': 'BGN', 'mid': 1.0},
                    {'code': 'TRY', 'mid': 1.0},
                    {'code': 'ILS', 'mid': 1.0},
                    {'code': 'CLP', 'mid': 1.0},
                    {'code': 'PHP', 'mid': 1.0},
                    {'code': 'MXN', 'mid': 1.0},
                    {'code': 'ZAR', 'mid': 1.0},
                    {'code': 'BRL', 'mid': 1.0},
                    {'code': 'MYR', 'mid': 1.0},
                    {'code': 'IDR', 'mid': 1.0},
                    {'code': 'INR', 'mid': 1.0},
                    {'code': 'KRW', 'mid': 1.0},
                    {'code': 'CNY', 'mid': 1.0},
                    {'code': 'XDR', 'mid': 1.0},

                ],
                'effectiveDate': date.today().isoformat()
            }
        ]
        mock_fetch_currency_rates.return_value = mock_data

        request = HttpRequest()
        response = fetch_and_save_currency_rates(request)

        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'currency_rates/fetch.html')

        saved_currency_rates = CurrencyRate.objects.all()
        self.assertEqual(saved_currency_rates.count(), len(mock_data[0]['rates']))

        for i, currency in enumerate(mock_data[0]['rates']):
            saved_currency_rate = saved_currency_rates[i]
            self.assertEqual(saved_currency_rate.currency_code, currency['code'])
            self.assertEqual(saved_currency_rate.exchange_rate, currency['mid'])
            self.assertEqual(saved_currency_rate.date.isoformat(), mock_data[0]['effectiveDate'])

    def setUp(self):
        CurrencyRate.objects.create(currency_code='USD', exchange_rate=1.0, date=date.today())
        CurrencyRate.objects.create(currency_code='EUR', exchange_rate=1.0, date=date.today())

    def test_show_currency_rates(self):
        request = HttpRequest()
        response = show_currency_rates(request)

        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'currency_rates/rates.html')

        currency_rates = response.context_data['currency_rates']
        self.assertEqual(currency_rates.count(), 2)

    @patch('currency_rates.views.fetch_time_currency_rates')
    def test_fetch_currency_data_get(self, mock_fetch_time_currency_rates):
        request = HttpRequest()
        request.method = 'GET'
        response = fetch_currency_data(request)

        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'currency_rates/data_sheet.html')

        currency_rates = response.context_data['currency_rates']
        self.assertEqual(currency_rates.count(), 2)

    @patch('currency_rates.views.fetch_time_currency_rates')
    def test_fetch_currency_data_post(self, mock_fetch_time_currency_rates):
        mock_data = [
            {
                'rates': [
                    {'code': 'THB', 'mid': 1.0},
                    {'code': 'USD', 'mid': 1.0},
                    {'code': 'AUD', 'mid': 1.0},
                    {'code': 'HKD', 'mid': 1.0},
                    {'code': 'CAD', 'mid': 1.0},
                    {'code': 'NZD', 'mid': 1.0},
                    {'code': 'SGD', 'mid': 1.0},
                    {'code': 'EUR', 'mid': 1.0},
                    {'code': 'HUF', 'mid': 1.0},
                    {'code': 'CHF', 'mid': 1.0},
                    {'code': 'GBP', 'mid': 1.0},
                    {'code': 'UAH', 'mid': 1.0},
                    {'code': 'JPY', 'mid': 1.0},
                    {'code': 'CZK', 'mid': 1.0},
                    {'code': 'DKK', 'mid': 1.0},
                    {'code': 'ISK', 'mid': 1.0},
                    {'code': 'NOK', 'mid': 1.0},
                    {'code': 'SEK', 'mid': 1.0},
                    {'code': 'RON', 'mid': 1.0},
                    {'code': 'BGN', 'mid': 1.0},
                    {'code': 'TRY', 'mid': 1.0},
                    {'code': 'ILS', 'mid': 1.0},
                    {'code': 'CLP', 'mid': 1.0},
                    {'code': 'PHP', 'mid': 1.0},
                    {'code': 'MXN', 'mid': 1.0},
                    {'code': 'ZAR', 'mid': 1.0},
                    {'code': 'BRL', 'mid': 1.0},
                    {'code': 'MYR', 'mid': 1.0},
                    {'code': 'IDR', 'mid': 1.0},
                    {'code': 'INR', 'mid': 1.0},
                    {'code': 'KRW', 'mid': 1.0},
                    {'code': 'CNY', 'mid': 1.0},
                    {'code': 'XDR', 'mid': 1.0},
                ],
                'effectiveDate': date.today().isoformat()
            }
        ]
        mock_fetch_time_currency_rates.return_value = mock_data

        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'start_date': '2023-01-01',
            'end_date': '2023-01-31',
            'currency': 'USD'
        }
        response = fetch_currency_data(request)

        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'currency_rates/data_sheet.html')

        currency_rates = response.context_data['currency_rates']
        filtered_data = response.context_data['filtered_data']
        self.assertEqual(currency_rates.count(), 2)
        self.assertEqual(len(filtered_data), 1)
        self.assertEqual(filtered_data[0].currency_code, 'USD')
        self.assertEqual(filtered_data[0].exchange_rate, 1.0)
        self.assertEqual(filtered_data[0].date, mock_data[0]['effectiveDate'])

    def test_fetch_currency(self):
        request = HttpRequest()
        response = fetch_currency(request)

        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'currency_rates/data_sheet.html')

    def test_home_page(self):
        request = HttpRequest()
        response = home_page(request)

        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'currency_rates/homepage.html')
