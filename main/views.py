from django.shortcuts import render_to_response, RequestContext
from main.forms import MemeForm
from main.models import Meme

def home(request):
    meme_form = MemeForm()
    my_meme = request.user.memes
    if request.method == "POST":
        meme_form = MemeForm(request.POST)
        if meme_form.is_valid():
            Meme(user=request.user, picture=meme_form.cleaned_data["picture"]).save()
    return render_to_response("main/home.html",
        {"form": meme_form, "my_meme": my_meme}, context_instance=RequestContext(request))

def popup_test(request):
    meme_form = MemeForm(request.POST)
    return render_to_response("main/popup_test.html",
        {"form": meme_form}, context_instance=RequestContext(request))