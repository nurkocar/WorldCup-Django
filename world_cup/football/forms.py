from django import forms
from .models import Player, Country

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [ 'player_name', 'player_team', 'age' ]
        # widgets = {
        #     'player_team': forms.TextInput(attrs={'placeholder': 'Name'}),
        # }