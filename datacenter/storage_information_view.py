from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from .shared_utils import get_duration
from .shared_utils import format_duration
from .shared_utils import format_entry


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        entered_at_local = timezone.localtime(visit.entered_at)
        delta = get_duration(visit)
        result = format_duration(delta.total_seconds())
        entry = {'who_entered': f'{visit.passcard}',
            'entered_at': f'{format_entry(entered_at_local)}',
            'duration': f'{result}',
        }        
        non_closed_visits.append(entry)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)