from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core.serializers import serialize
from django.db.models import Avg
from rest_framework import generics

from .forms import AddPlayerForm
from .models import Player, Country
from .serializers import CountrySerializer

# Create your views here.
def home(request):
    return render(request, '../templates/home.html')

def add_player(request):
    form = AddPlayerForm()
    players = Player.objects.all()
    if request.method == "POST":
        form = AddPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/players")
    context = {
        'form': form,
        'players': players
    }
    return render(request, "../templates/add_player.html", context)

class CountryView(generics.ListAPIView):

   queryset = Country.objects.all()
   serializer_class = CountrySerializer


# Just leaving for future reference
# def countries(request):
#     countries = Country.objects.all()
    

#     for country in countries:
#         average_age = Player.objects.filter(player_team=country).aggregate(Avg('age'))
#         country.average_age = average_age
    
#     data = serialize("json", countries, fields=('country_name', 'fifa_ranking', 'average_age'))
    
#     return HttpResponse(data, content_type="application/json")

