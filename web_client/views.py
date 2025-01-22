from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TextEntry

def main(request: HttpRequest):
  return HttpResponse(render(request, 'main.html', {"username": request.user.get_username()}))

def database_viewer(request: HttpRequest):
  files = TextEntry.objects.all().values()
  return HttpResponse(render(request, 'database_viewer.html', {"data_entries": files}))

def text_doc_viewer(request: HttpRequest, file_id):
  file = TextEntry.objects.get(id = file_id)
  return HttpResponse(render(request, 'text_doc_viewer.html', {"textEntry": file}))