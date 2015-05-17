from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CandidateForm, EmailForm
from .models import create_candidate, get_candidate


def index(request, candidate_id):
    candidate = get_candidate(candidate_id)
    events = candidate.load_events()
    context = {
     'c': candidate,
     'events': events
     }
    return render(request, 'candidate.html', context)


def create(request):
    form = CandidateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        c = create_candidate(form.cleaned_data)
        messages.success(request, 'Added candidate: {}'.format(c))
        return HttpResponseRedirect('/')

    context = {
        'form': form
    }
    return render(request, 'create_candidate.html', context)


def update(request, candidate_id, field):
    candidate = get_candidate(candidate_id)
    form = form_by_fields[field]
    return update_field(request, form, candidate, field)


form_by_fields = {
    'name': CandidateForm,
    'email': EmailForm
}


def update_field(request, Form, candidate, field):
    current_value = getattr(candidate, field)
    form = Form(request.POST or {field: current_value})
    if request.method == 'POST' and form.is_valid():
        update_func = getattr(candidate, 'update_{}'.format(field))
        update_func(form.cleaned_data[field])
        candidate.save()
        messages.success(request, 'Updated candidate')
        return HttpResponseRedirect('/candidate/{}/'.format(candidate.id))
    else:
        context = {
            'form': form,
            'c': candidate,
            'title': 'Update {}'.format(field),
            'current_value': current_value
        }
        return render(request, 'update_candidate.html', context)
