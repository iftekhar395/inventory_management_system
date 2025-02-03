from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render


def homepage(request):
  template = loader.get_template('homepage.html')

  return HttpResponse(template.render())
