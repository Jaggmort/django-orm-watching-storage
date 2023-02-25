from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import django
from django.shortcuts import get_object_or_404

def get_duration(visit):
    visit_entered_at_local = timezone.localtime(visit.entered_at)
    if visit.leaved_at == None:
        delta = django.utils.timezone.localtime() - visit_entered_at_local
    else:
        visit_leaved_at_local = timezone.localtime(visit.leaved_at)
        delta = visit_leaved_at_local - visit_entered_at_local
    return delta

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    time_difference = 3600
    this_passcard_visits = []
    for visit in visits:
        if visit.leaved_at!=None:
            is_strange = False
            if (visit.leaved_at-visit.entered_at).seconds >= time_difference:
                is_strange = True
        this_passcard_visit = {
                'entered_at': f'{visit.entered_at}',
                'duration': f'{get_duration(visit)}',
                'is_strange': f'{is_strange}'
            }
                
        this_passcard_visits.append(this_passcard_visit) 
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }    
    return render(request, 'passcard_info.html', context)