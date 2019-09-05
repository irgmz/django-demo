# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import time
from datetime import datetime

from django.http import HttpResponse, HttpResponseBadRequest

TWENTY_ONE_YEARS_TS = 21 * 365 * 24 * 60 * 60

def index(request):
    birthdate = request.GET.get('birthdate')

    if not birthdate:
        return HttpResponse(
            'Please add your birthdate in the query string.'
        )

    try:
        birthdate_ts = int(time.mktime(datetime.strptime(birthdate, 'YYYY-MM-DD').timetuple()))
    except ValueError:
        return HttpResponseBadRequest(
            'Please format the birthdate in ISOFORMAT'
        )

    now = int(time.time())
    if (now - birthdate_ts) >= TWENTY_ONE_YEARS_TS:
        return HttpResponse(
            '<h1 style="background-color:lightgreen;">Welcome Adult!</h1>'
        )

    else:
        return HttpResponse(
            '<h1 style="background-color:red; color:white">redirect <a href=https://google.com/>away</a></h1>'
        )
