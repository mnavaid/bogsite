from django import forms
from .models import BlogPosts

# Post Form

class postForm(forms.ModelForm):
    
    class Meta:
      model=BlogPosts
      fields = ["title","description"]
      labels = {'title':'Title', 'description':'Description'}
      widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
              'description':forms.Textarea(attrs={'class':'form-control'},)}
