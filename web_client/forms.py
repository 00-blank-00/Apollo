from django.forms import ModelForm
from .models import TextEntry

class TextEntryForm(ModelForm):
    class Meta:
        model = TextEntry
        fields = ['title', 'description', 'content']