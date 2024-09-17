from django.shortcuts import render
from .forms import TeamRosterFormSet

def add_team_roster(request):
    if request.method == 'POST':
        formset = TeamRosterFormSet(request.POST)
        if formset.is_valid():
            formset.save()  # Saves the formset
            return redirect('success_page')
    else:
        formset = TeamRosterFormSet()
    return render(request, 'add_team_roster.html', {'formset': formset})
