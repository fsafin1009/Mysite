from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = 'title', 'content'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control" , "rows" : 10}
