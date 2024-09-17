from django import forms 
from django.forms import modelformset_factory
from .models import TeamRoster 

class TeamRosterForm(forms.ModelForm):
    class Meta:
        model = TeamRoster
        fields = ['team_name', 'player_first_name', 'player_last_name', 'player_email', 'player_phone']
    
# Allow up to 5 players, but require at least 1
TeamRosterFormSet = modelformset_factory(TeamRoster, form=TeamRosterForm, extra=4, min_num=1, validate_min=True)
    
        