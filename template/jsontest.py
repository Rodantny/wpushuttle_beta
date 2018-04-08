import requests
import json
import datetime



from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Greeting


class jsontest(ListView):
    model = Book

    def head(self, *args, **kwargs):
        shuttle_id = '03';

        data = {
            'shuttle_id': shuttle_id,
            'location': 'Finland',
            'is_active': True,
            'count': 28
        }

        return JsonResponse(data)