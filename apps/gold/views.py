from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import random

from datetime import datetime

def index(request):

    return render(request, "gold/index.html")

def process(request):
    if request.POST['building'] == 'farm':
        fgold = random.randrange(10, 20)
        now = str(datetime.now())
        if 'activity' in request.session:
            request.session['activity'].append(
                'Earned {} golds from the farm! ({})'.format(fgold, now))
        else:
            request.session['activity'] = [
                'Earned {} golds from the farm! ({})'.format(fgold, now)]
        if 'gold' in request.session:
            request.session['gold'] += fgold
        else:
            request.session['gold'] = fgold
    elif request.POST['building'] == 'cave':
        cgold = random.randrange(5, 10)
        now = str(datetime.now())
        if 'activity' in request.session:
            request.session['activity'].append(
                'Earned {} golds from the cave! ({})'.format(cgold, now))
        else:
            request.session['activity'] = [
                'Earned {} golds from the cave! ({})'.format(cgold, now)]
        if 'gold' in request.session:
            request.session['gold'] += cgold
        else:
            request.session['gold'] = cgold
    elif request.POST['building'] == 'house':
        hgold = random.randrange(2, 5)
        now = str(datetime.now())
        if 'activity' in request.session:
            request.session['activity'].append(
                'Earned {} golds from the house! ({})'.format(hgold, now))
        else:
            request.session['activity'] = [
                'Earned {} golds from the house! ({})'.format(hgold, now)]
        if 'gold' in request.session:
            request.session['gold'] += hgold
        else:
            request.session['gold'] = hgold
    else:
        request.POST['building'] == 'casino'
        cagold = random.randrange(-50, 50)
        now = str(datetime.now())
        if 'activity' in request.session:
            if cagold >= 0:
                request.session['activity'].append(
                    'Entered a casino and gained {} golds! ({})'.format(cagold, now))
            else:
                request.session['activity'].append(
                    'Entered a casino and lost {} golds! ... Ouch.. ({})'.format(cagold, now))
        else:
            if cagold >= 0:
                request.session['activity'].append(
                    'Entered a casino and gained {} golds! ({})'.format(cagold, now))
            else:
                request.session['activity'] = [
                    'Entered a casino and gained {} golds! ({})'.format(cagold, now)]
        if 'gold' in request.session:
            request.session['gold'] += cagold
        else:
            request.session['gold'] = cagold
    print request.session['activity']
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
