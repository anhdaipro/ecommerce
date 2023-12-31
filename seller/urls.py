from django.urls import path
from . import views
from .views import (DashboardBundleAPI,DashboardVoucherAPI,DashboardAddonAPI,
DashboardFlashsaleAPI,DashboardDiscountAPI,DataBundleAPI,
DataVoucherAPI,
DataDiscountAPI,
DataFlashsaleAPI,
MyDashboard,
DataAddonAPI,
DataFollowerAPI,
DataShopAwardAPI,
DashboardAwardAPI,
DashboardOfferAPI)
urlpatterns = [
    path("dashboard", MyDashboard.as_view()),
    path("dashboard/voucher", DashboardVoucherAPI.as_view()),
    path("dashboard/addon", DashboardAddonAPI.as_view()),
    path('dashboard/bundle',DashboardBundleAPI.as_view()),
    path('dashboard/flash',DashboardFlashsaleAPI.as_view()),
    path('dashboard/discount',DashboardDiscountAPI.as_view()),
    path('dashboard/game',DashboardAwardAPI.as_view()),
    path('dashboard/prize',DashboardOfferAPI.as_view()),
    path('data/bundle',DataBundleAPI.as_view()),
    path('data/voucher',DataVoucherAPI.as_view()),
    path('data/discount',DataDiscountAPI.as_view()),
    path('data/flash',DataFlashsaleAPI.as_view()),
    path('data/addon',DataAddonAPI.as_view()),
    path('data/game',DataShopAwardAPI.as_view()),
    path('data/prize',DataFollowerAPI.as_view()),
]