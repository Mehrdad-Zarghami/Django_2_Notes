from django.shortcuts import render
from .models import Note


def notes_list_view(request):
    notes = Note.objects.all()
    context = {
        'list_of_notes': notes,
    }
    return render(request, 'notes/notes_list.html', context)

