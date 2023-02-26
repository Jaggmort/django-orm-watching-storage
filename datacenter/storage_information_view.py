from datacenter.models import Visit
from django.utils import timezone
from django.shortcuts import render
from .shared_utils import get_duration
from .shared_utils import format_duration
from .shared_utils import format_entry
from .shared_utils import is_visit_long


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        visitor = visit.passcard
        entered_at = format_entry(timezone.localtime(visit.entered_at))      
        delta = get_duration(visit)
        result = format_duration(delta.total_seconds())
        is_strange = is_visit_long(visit)
        entry = {'who_entered': visitor,
            'entered_at': entered_at,
            'duration': result,
            'is_strage': is_strange
        }        
        non_closed_visits.append(entry)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)