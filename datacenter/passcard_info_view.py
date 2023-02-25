from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .shared_utils import get_duration
from .shared_utils import is_visit_long

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        is_strange=is_visit_long(visit)
        this_passcard_visit = {
                'entered_at': f'{visit.entered_at}',
                'duration': f'{get_duration(visit)}',
                'is_strange': f'{is_strange(visit)}'
            }
                
        this_passcard_visits.append(this_passcard_visit) 
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }    
    return render(request, 'passcard_info.html', context)