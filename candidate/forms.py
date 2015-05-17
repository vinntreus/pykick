from django import forms


class CandidateForm(forms.Form):
    name = forms.CharField(max_length=400,
                           widget=forms.TextInput(attrs={'autofocus': ''}))


class EmailForm(forms.Form):
    email = forms.CharField(max_length=400, required=False,
                            widget=forms.TextInput(attrs={'autofocus': ''}))
