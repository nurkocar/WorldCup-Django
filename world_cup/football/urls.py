from django.urls import path
from .views import home, add_player, CountryView

urlpatterns = [
    path('', home, name='home'),
    path('players/', add_player, name='add_player'),
    path('countries/', CountryView.as_view())
]