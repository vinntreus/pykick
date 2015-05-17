from django.shortcuts import render
from candidate.models import get_candidates


def home(request):
    context = {
        'candidates': get_candidates()
    }
    return render(request, 'startpage.html', context)
