from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import TextEntry

def main(request: HttpRequest):
  return HttpResponse(render(request, 'main.html'))

def database_viewer(request: HttpRequest):
  files = TextEntry.objects.all().values()
  return HttpResponse(render(request, 'database_viewer.html', {"data_entries": files}))

def text_doc_viewer(request: HttpRequest, file_id):
  file = TextEntry.objects.get(id = file_id)
  return HttpResponse(render(request, 'text_doc_viewer.html', {"textEntry": file}))