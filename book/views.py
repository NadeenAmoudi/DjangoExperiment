from django.shortcuts import render, redirect
from .models import Chapter
from .forms import ChapterForm


def chapters_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'chapters.html', {'chapters': chapters})

def create_chapter(request):
    form = ChapterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book:chapters_list')

    return render(request, 'add-chapter.html', {'form': form})

def update_chapter(request, id):
    chapter = Chapter.objects.get(id=id)
    form = ChapterForm(request.POST or None, instance=chapter)

    if form.is_valid():
        form.save()
        return redirect('book:chapters_list')

    return render(request, 'edit-chapter.html', {'form': form, 'chapter': chapter})

def delete_chapter(request, id):
    chapter = Chapter.objects.get(id=id)

    if request.method == 'POST':
        chapter.delete()
        return redirect('book:chapters_list')

    return render(request, 'delete-confirm.html', {'chapter': chapter})