
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index2(request):
    return HttpResponse(loader.get_template('index.html').render())