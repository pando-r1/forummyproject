from django import forms
from django.urls.base import reverse

from home.models import Post, Category


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),}
    # title = forms.CharField(max_length=255, label="Заголовок")
    # description = forms.CharField(widget=forms.Textarea, label="Описание")
    # image = forms.ImageField(upload_to="post_images/%Y/%m/%d/", blank=True)
    # category = forms.ModelChoiceField(querset=Category.objects.filter(name=name))
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    # moderation = forms.BooleanField(default=True)