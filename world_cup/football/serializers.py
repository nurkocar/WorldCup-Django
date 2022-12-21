from django.db.models import Avg

from .models import Country, Player
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):

    average_age =  serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ('country_name', 'fifa_ranking', 'average_age')

    
    def get_average_age(self, obj):
        return Player.objects.filter(player_team = obj).aggregate(Avg('age'))