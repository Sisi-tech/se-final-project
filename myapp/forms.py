from django import forms 
from django.forms import modelformset_factory
from .models import TeamInfo, User, Player, Waiver

class TeamForm(forms.ModelForm):
    class Meta:
        model = TeamInfo 
        fields = ['team_name', 'division', 'preferred_game_time', 't_shirts']

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = '__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team_name', 'first_name', 'last_name', 'email', 'phone']
    
# Allow up to 5 players, but require at least 1
PlayerFormSet = modelformset_factory(Player, form=PlayerForm, extra=4, min_num=1, validate_min=True)

class WaiverForm(forms.ModelForm):
    class Meta:
        model = Waiver 
        fields = '__all__'
        
    
        