from django.utils import timezone

def get_duration(visit):
    visit_entered_at_local = timezone.localtime(visit.entered_at)
    if visit.leaved_at == None:
        delta = timezone.localtime() - visit_entered_at_local
    else:
        visit_leaved_at_local = timezone.localtime(visit.leaved_at)
        delta = visit_leaved_at_local - visit_entered_at_local
    return delta

def format_duration(duration):
    hours = int(duration//3600)
    minutes = int((duration%3600)//60)
    seconds = int((duration%3600)%60)
    total_result = f'{hours} ч {minutes} мин {seconds} сек'
    return total_result    

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

def is_visit_long(visit):
    time_difference = 3600
    is_strange = False
    if int(get_duration(visit).total_seconds()) >= time_difference:
        is_strange = True
    return(is_strange)    