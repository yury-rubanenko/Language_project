from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def user_profile(request):
    user = request.user
    words = user.words.all()  # Отримати всі слова, пов'язані з користувачем

    # Передати дані профілю користувача у шаблон
    return render(request, 'profiles/user_profile.html', {'user': user, 'words': words})
