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

    birthdate_ts = int(time.mktime(datetime.strptime(birthdate, 'YYYY-MM-DD').timetuple()))

    now = int(time.time())
    if (now - birthdate_ts) >= TWENTY_ONE_YEARS_TS:
        # do something
        pass
    else:
        # do something else
        pass
