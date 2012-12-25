from django.shortcuts import render_to_response, RequestContext
from main.forms import MemeForm

def home(request):
    meme_form = MemeForm(request.POST)
    return render_to_response("main/home.html",
        {"form": meme_form}, context_instance=RequestContext(request))

def popup_test(request):
    meme_form = MemeForm(request.POST)
    return render_to_response("main/popup_test.html",
        {"form": meme_form}, context_instance=RequestContext(request))