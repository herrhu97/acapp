from django.http import HttpResponse

# Create your views here.

def index(request):
    line1 = '<h1 style="text-align: center">Dinner chicken</h1>'
    # return HttpResponse("My first web page!")
    return HttpResponse(line1)
