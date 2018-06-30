import requests
import json
import datetime




from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def build_json(current_time, current_time_min, weekday, location_main,location_valley, location_safe,location_sunday,):
        data = {
            'Weekday': weekday,
            'current_time': current_time,
            'min time': current_time_min,
            'location_main': location_main,
            'location_valley': location_valley,
            'location_safe': location_safe,
            'location_sunday': location_sunday,
        }
        return data

def get_location_main(current_time,current_time_min):

    if current_time < 730 or current_time > 2300:
        return 'Sorry! This Shuttle is not running at this time.'
    elif (00 <= current_time_min < 5 or 30 <= current_time_min < 35):
        return 'This Shuttle is at Lot 6.'
    elif (5 <= current_time_min < 10 or 35 <= current_time_min < 40):
        return 'This Shuttle is on its way to Heritage.'
    elif (10 <= current_time_min < 11 or 40 <= current_time_min < 41):
        return 'This Shuttle is at Heritage.'
    elif (11 <= current_time_min < 13 or 41 <= current_time_min < 43):
        return 'This Shuttle is at Pioneer.'
    elif (13 <= current_time_min < 15 or 41 <= current_time_min < 45):
        return 'This Shuttle is on its way to Ben Shahn/Garage.'
    elif (15 <= current_time_min < 19 or 45 <= current_time_min < 49):
        return 'This Shuttle is at Ben Shahn/Garage.'
    elif (19 <= current_time_min < 25 or 49 <= current_time_min < 55):
        return 'This Shuttle is on its way to Lot 5.'
    elif (25 <= current_time_min < 27 or 55 <= current_time_min < 57):
        return 'This Shuttle is at  Lot 5.'
    elif (27 <= current_time_min < 30 or 57 <= current_time_min <= 60):
        return 'This Shuttle is on its way to Lot 6.'
    else:
        return 'ERROR'

def get_location_valley(current_time,current_time_min):

    if current_time < 730 or current_time > 2300:
        return 'Sorry! This Shuttle is not running at this time.'
    elif (00 <= current_time_min < 9 or 30 <= current_time_min < 39):
        return 'This Shuttle is at Lot 5.'
    elif (9 <= current_time_min < 15 or 39 <= current_time_min < 45):
        return 'This Shuttle is on its way to 1600 Valley Road.'
    elif (15 <= current_time_min < 18 or 45 <= current_time_min < 48):
        return 'This Shuttle is at 1600 Valley Road.'
    elif (18 <= current_time_min < 20 or 48 <= current_time_min < 50):
        return 'This Shuttle is on its way to Power Arts.'
    elif (20 <= current_time_min < 23 or 50 <= current_time_min < 53):
        return 'This Shuttle is at Power Arts.'
    elif (23 <= current_time_min < 25 or 53 <= current_time_min < 55):
        return 'This Shuttle is on its way to College Hall.'
    elif (25 <= current_time_min < 27 or 55 <= current_time_min < 57):
        return 'This Shuttle is at College Hall.'
    elif (27 <= current_time_min < 30 or 55 <= current_time_min < 60):
        return 'This Shuttle on its way to college Hall.'
    else:
        return 'ERROR'

def get_location_safe(current_time,current_time_min):

    if current_time > 300 and current_time < 2300:
        return 'Sorry! This Shuttle is not running at this time.'
    elif (00 <= current_time_min < 5 ):
        return 'This Shuttle is at Lot 5.'
    elif (5 <= current_time_min < 10 ):
        return 'This Shuttle is on its way to Power Arts.'
    elif (10 <= current_time_min < 15 ):
        return 'This Shuttle is at Power Arts'
    elif (15 <= current_time_min < 20 ):
        return 'This Shuttle is on its way to Overlook.'
    elif (20 <= current_time_min < 22 ):
        return 'This Shuttle is at Overlook.'
    elif (22 <= current_time_min < 25 ):
        return 'This Shuttle is on its way to Lot 6 / Bus Stop.'
    elif (25 <= current_time_min < 27 ):
        return 'This Shuttle is at Lot 6 / Bus Stop.'
    elif (27 <= current_time_min < 30 ):
        return 'This Shuttle is at Rec Center / Top Row.'
    elif (30 <= current_time_min < 33 ):
        return 'This Shuttle is at Lot 6'
    elif (33 <= current_time_min < 35 ):
        return 'This Shuttle is on its way to Heritage & Pioneer'
    elif (35 <= current_time_min < 37 ):
        return 'This Shuttle is at Heritage & Pioneer'
    elif (37 <= current_time_min < 40 ):
        return 'This Shuttle is on its way to Lot 1'
    elif (40 <= current_time_min < 43 ):
        return 'This Shuttle is on is at Lot 1'
    elif (43 <= current_time_min < 45 ):
        return 'This Shuttle is on its way to Heritage & Pioneer'
    elif (45 <= current_time_min < 48 ):
        return 'This Shuttle is at Heritage & Pioneer'
    elif (48 <= current_time_min < 50 ):
        return 'This Shuttle is on its way to Overlook'
    elif (50 <= current_time_min < 55 ):
        return 'This Shuttle is at Overlook'
    elif (55 <= current_time_min < 60 ):
        return 'This Shuttle is on its wat to Lot 5'
    else:
        return 'ERROR'

def get_location_sunday(current_time,current_time_min):

    if current_time < 1600  or current_time > 2000:
        return 'Sorry! This Shuttle is not running at this time.'
    elif (00 <= current_time_min < 5 ):
        return 'This Shuttle is at Lot 5.'
    elif (5 <= current_time_min < 10 ):
        return 'This Shuttle is on its way to Heritage & Pioneer.'
    elif (10 <= current_time_min < 15 ):
        return 'This Shuttle is at Heritage & Pioneer.'
    elif (15 <= current_time_min < 20 ):
        return 'This shuttle is on its way to Shop Rite'
    elif (20 <= current_time_min < 25 ):
        return 'This shuttle is at Shop Rite'
    elif (25 <= current_time_min < 45 ):
        return 'This shuttle is on its way to Paterson NJ Transit'
    elif (45 <= current_time_min < 47 ):
        return 'This shuttle is at Paterson NJ Transit'
    elif (45 <= current_time_min < 47 ):
        return 'This shuttle is on its way to Lot 5.'
    else:
        return 'ERROR'

def jsontest(request):
    t = (datetime.datetime.utcnow() - datetime.timedelta(hours=4))

    current_time_string = t.strftime('%H%M')
    current_time = int(current_time_string) #convert string into int

    current_time_string = t.strftime('%M')
    current_time_min = int(current_time_string)#convert string into int

    weekday = t.strftime('%A')  #get day of the week

    location_safe = get_location_safe(current_time, current_time_min)

    if weekday == 'Sunday':
        location_sunday = get_location_sunday(current_time, current_time_min)
    else:
        location_sunday = 'Sorry! This Shuttle is not running at this time.'

    if weekday == ('Saturday' or 'Sunday'):
        location_main = 'Sorry! This Shuttle is not running at this time.1'
        location_valley = 'Sorry! This Shuttle is not running at this time.1'
    else:
        location_main = get_location_main(current_time,current_time_min)
        location_valley = get_location_valley(current_time,current_time_min)

    shuttle_json_data = build_json(current_time,current_time_min,weekday,location_main,location_valley,location_safe,location_sunday)
    return JsonResponse(shuttle_json_data,safe=False)



