from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()  # Cevap metni
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class QuestionRequest(models.Model):
    question_text = models.TextField(verbose_name="Soru")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Soran Kullanıcı")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Eğer kategori varsa
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text[:50]
