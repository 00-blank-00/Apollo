from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('database_viewer/', views.database_viewer),
    path('database_viewer/text_document/<int:file_id>', views.text_doc_viewer)
]