# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import time
from datetime import date, datetime

from django.http import HttpResponse

TWENTY_ONE_YEARS_TS = 21 * 365 * 24 * 60 * 60

def index(request):
    birthdate = request.GET.get('birthdate')

    if not birthdate:
        return HttpResponse('Please add your birthdate in the query string as ?birthdate=MM-DD-YYYY')

    message = ' '.join(['Today\'s date:', str(date.today())])

    now = int(time.time())
    birthdate_ts = int(time.mktime(datetime.strptime(birthdate, '%m-%d-%Y').timetuple()))

    if (now - birthdate_ts) >= TWENTY_ONE_YEARS_TS:
        return HttpResponse(' '.join([message, '- Welcome Adult!']))

    else:
        return HttpResponse(' '.join([message, '- GTFO here child.']))
