from django import forms
from urllib.parse import urlencode

class CoverForm(forms.Form):
    title = forms.CharField()
    top_text = forms.CharField()
    author = forms.CharField()

    @property
    def get_params(self):
        if hasattr(self, 'cleaned_data'):
            return urlencode(self.cleaned_data)
            return None