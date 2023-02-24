from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import django


def get_duration(visit):
    visit_entered_at_local = timezone.localtime(visit.entered_at)
    if visit.leaved_at == None:
        delta = django.utils.timezone.localtime() - visit_entered_at_local
    else:
        visit_leaved_at_local = timezone.localtime(visit.leaved_at)
        delta = visit_leaved_at_local - visit_entered_at_local
    return delta

def format_duration(duration):
    hours = duration//3600
    minutes = (duration%3600)//60
    return f'{hours}ч {minutes}мин'    

def format_entry(time):
    month_litteral = ['Января','Февраля','Марта','Апреля','Мая','Июня','Июля','Августа','Сентября','Октября','Ноября','Декабря']
    if time.hour < 10:
        hour = f'0{time.hour}'
    else:
        hour = time.hour
    if time.minute < 10:
        minute = f'0{time.minute}'
    else:
        minute = time.minute            
    return f'{time.day} {month_litteral[time.month]} {time.year}г {hour}:{minute}'

def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        entered_at_local = timezone.localtime(visit.entered_at)
        delta = get_duration(visit)
        result = format_duration(delta.seconds)
        entry = {'who_entered': f'{visit.passcard}',
            'entered_at': f'{format_entry(entered_at_local)}',
            'duration': f'{result}',
        }        
        non_closed_visits.append(entry)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
