from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))