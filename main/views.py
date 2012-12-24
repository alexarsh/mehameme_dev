from django.shortcuts import render_to_response, RequestContext

def home(request):
    return render_to_response("main/home.html", {}, context_instance=RequestContext(request))

def popup_test(request):
    return render_to_response("main/popup_test.html", {}, context_instance=RequestContext(request))