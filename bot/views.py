from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from . api import bitstamp
# Create your views here.

@login_required
def index(request):
    context = {}
    return render(request, 'bot/index.html', context)

