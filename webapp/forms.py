from django import forms


class SearchRepoForm(forms.Form):
    term = forms.CharField(50)
