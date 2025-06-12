from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Category
from .models import Question, QuestionRequest

# Anasayfa
def home(request):
    return render(request, 'web/anasayfa.html')

# Kayıt
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt başarılı. Giriş yapabilirsiniz.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'web/register.html', {'form': form})

# Giriş
def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('admin_panel')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış ya da kullanıcı aktif değil.')

    return render(request, 'web/login.html')

# Soru sor (kullanıcı)
@login_required
def ask_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        if question_text:
            QuestionRequest.objects.create(
                question_text=question_text,
                created_by=request.user
            )
            messages.success(request, "Sorunuz yetkiliye iletildi.")
            return render(request, 'web/ask_question.html', {'question_sent': True})
    return render(request, 'web/ask_question.html')

# SSS görüntüle
def sss_view(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')

    questions = Question.objects.all()

    if category_id:
        questions = questions.filter(category_id=category_id)

    if query:
        questions = questions.filter(title__icontains=query)  # Başlıkta arama

    categories = Category.objects.all()

    return render(request, 'web/sss.html', {
        'questions': questions,
        'categories': categories,
        'request': request,
    })
def admin_panel(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        answer = request.POST.get('answer')
        if question_id and answer:
            question_request = get_object_or_404(QuestionRequest, id=question_id)
            # Cevap kaydetme işlemi (örneğin Question modeline kayıt)
            question = Question.objects.create(
                title=question_request.question_text[:200],  # ya uygun başlık
                content=answer,
                category=question_request.category  # eğer varsa
            )
            # Soru cevaplansın diye işaretle
            question_request.is_answered = True
            question_request.save()
            messages.success(request, "Soru cevaplandı ve yayınlandı.")
            return redirect('admin_panel')

    # GET isteğinde soruları çek
    pending_questions = QuestionRequest.objects.filter(is_answered=False)
    return render(request, 'web/admin_panel.html', {'pending_questions': pending_questions})

# Soru cevapla (admin)
@login_required
def answer_question(request, question_request_id):
    if not request.user.is_staff:
        return redirect('home')

    question_request = get_object_or_404(QuestionRequest, id=question_request_id)

    if request.method == 'POST':
        answer_text = request.POST.get('answer')
        if answer_text:
            # Question tablosuna kaydet
            Question.objects.create(
                title=question_request.question_text[:200],
                content=answer_text,
                category=question_request.category
            )
            # Soruyu cevaplandı olarak işaretle
            question_request.is_answered = True
            question_request.save()

            messages.success(request, "Soru cevaplandı ve SSS'ye eklendi.")
            return redirect('sss_view')

    return render(request, 'web/answer_question.html', {'question_request': question_request})


# SSS'den soru sil (admin)
@login_required
def delete_question(request, question_id):
    question = get_object_or_404(QuestionRequest, id=question_id)
    question.delete()
    messages.success(request, "Soru silindi.")
    return redirect('admin_panel')

