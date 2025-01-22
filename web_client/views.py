from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TextEntry
from .forms import TextEntryForm

def main(request: HttpRequest):
  return HttpResponse(render(request, 'main.html', {"username": request.user.get_username()}))

def database_viewer(request: HttpRequest):
  files = TextEntry.objects.all().values()
  return HttpResponse(render(request, 'database_viewer.html', {"data_entries": files}))

def text_doc_viewer(request: HttpRequest, file_id):
  file = TextEntry.objects.get(id = file_id)
  return HttpResponse(render(request, 'text_doc_viewer.html', {"textEntry": file}))

def text_doc_editor(request: HttpRequest, file_id):
  #gets a file instance depending on the request id
  file = TextEntry.objects.get(id = file_id)
  
  #if form is posting then validate and save it
  if request.method == "POST":
    form = TextEntryForm(request.POST, instance = file)
    if form.is_valid():
      file = form.save(commit=False)
      file.save()
      return redirect(f'../text_document/{file_id}')
  #If not posting then create a new form from that file entry
  else:
    form = TextEntryForm(instance=file)

  #And return the page
  return render(request, 'text_doc_editor.html', {'form': form})