from django import forms
from django.contrib.auth.models import User

class QuestionForm(forms.Form):
    title = forms.CharField(label='Soru Başlığı', max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ChoiceField(
        label='Kategori',
        choices=[('genel', 'Genel'), ('akademik', 'Akademik'), ('idari', 'İdari')],
        widget=forms.Select(attrs={'class':'form-control'}),
        required=False
    )
    content = forms.CharField(label='Sorunuz', widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']