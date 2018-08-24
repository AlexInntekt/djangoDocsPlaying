from django import forms

class LoginForm(forms.ModelForm):

    class Meta:
      #  model = Post
        fields = ('username', 'password',)