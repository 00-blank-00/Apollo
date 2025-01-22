from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def main(request: HttpRequest):
  return HttpResponse(render(request, 'main.html'))
   