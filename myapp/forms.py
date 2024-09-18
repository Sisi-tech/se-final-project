from django import forms 
from django.forms import modelformset_factory
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team_name', 'first_name', 'last_name', 'email', 'phone']
    
# Allow up to 5 players, but require at least 1
PlayerFormSet = modelformset_factory(Player, form=PlayerForm, extra=4, min_num=1, validate_min=True)
    
        