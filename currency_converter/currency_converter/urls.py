"""
URL configuration for currency_converter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from currency_rates.views import fetch_and_save_currency_rates, show_currency_rates, fetch_currency_data, home_page, country_list, currency_, info, maps, CountryDetailView, search_country

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('fetch/', fetch_and_save_currency_rates, name='fetch_and_save_currency_rates'),
    path('rates/', show_currency_rates, name='show_currency_rates'),
    path('data_sheet/', fetch_currency_data, name='fetch_currency_data'),
    path('countries/', country_list, name='country_list'),
    path('cureency/', currency_, name='currency_'),
    path('info/', info, name='info'),
    path('country/<str:country_name>/', CountryDetailView.as_view(), name='country_detail'),
    path('maps/', maps, name='maps'),
    path('search-country/', search_country, name='search_country'),
]