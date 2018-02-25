from django import forms


class SearchRepoForm(forms.Form):
    term = forms.CharField(50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Repository name'}))
