from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.main),
    path('database_viewer/', views.database_viewer),
    path('database_viewer/text_document/<int:file_id>', views.text_doc_viewer),
    path('admin/', admin.site.urls)
]