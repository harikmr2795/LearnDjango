from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3> Music Page</h3")