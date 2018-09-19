from django.shortcuts import render
from .models import DeicideList
from .models import DeicideListArchive
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DeicideListForm
import tweepy
from tweepy.auth import OAuthHandler
from .CredData import *


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def get_deicide(request):
    if request.method == 'POST':
        form = DeicideListForm(request.POST)
        if form.is_valid():
            DeicideList = form.save(commit=False)
            DeicideList.save()
            qs2 = DeicideList.__class__.objects.latest('id')
            api.update_status('Here we are! {}'.format(qs2))
            return HttpResponseRedirect('/')
            

    else:
        form = DeicideListForm()


    qs = DeicideList.objects.all()
    context = {'form': form, 'list_active_gods': qs}
    return render(request, 'DeicideConfirmation.html', context)

def index(request):
    if request.method == 'POST':
        form = DeicideListForm(request.POST)
        if form.is_valid():
            qs = DeicideList.objects.all()
            return HttpResponseRedirect('/new')

    else:
        form = DeicideListForm()


    qs = DeicideList.objects.all()
    context = {'form': form, 'list_active_gods': qs}
    return render(request, 'DeicideConfirmation.html', context)

def about_us(request):
    return render(request, 'aboutus.html')

def history(request):
    qs2 = DeicideListArchive.objects.all()
    context = {'history_active_gods': qs2}
    return render(request, 'history.html', context)

