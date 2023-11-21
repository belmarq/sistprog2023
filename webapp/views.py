from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class Home(View):
    def get(self, request):
        cdx = {
            'titulo':'Enlaces',
            'URL':request.build_absolute_uri(),
            'IP':request.META.get('REMOTE_ADDR'),
            'puerto':request.META['SERVER_PORT'],
        }
        return render(request, 'index.html', cdx)