from django import forms

class QuestionForm(forms.Form):
    title = forms.CharField(label='Soru Başlığı', max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ChoiceField(
        label='Kategori',
        choices=[('genel', 'Genel'), ('akademik', 'Akademik'), ('idari', 'İdari')],
        widget=forms.Select(attrs={'class':'form-control'}),
        required=False
    )
    content = forms.CharField(label='Sorunuz', widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
