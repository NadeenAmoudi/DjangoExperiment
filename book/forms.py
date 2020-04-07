from django import forms
from .models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name', 'description', 'chapterNum', 'pageNum']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'chapterNum': 'Chapter Number',
            'pageNum': 'Page Number',
        }
