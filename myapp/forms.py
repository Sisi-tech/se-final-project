from django import forms 
from .models import TeamRoster 

class TeamRosterForm(forms.ModelForm):
    class Meta:
        model = TeamRoster
        fields = ['team_name', 'player_first_name', 'player_last_name', 'player_email', 'player_phone']
    
    def clean(self):
        cleaned_data = super().clean()
        team_name = cleaned_data.get("team_name")
        roster_count = TeamRoster.objects.filter(team_name=team_name).count()
        if roster_count >= 5:
            raise forms.ValidationError("A team can only have up to 5 players.")
        