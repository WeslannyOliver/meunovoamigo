from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    context = {
        "total_usuarios": 10,
        "total_pets": 25,
        "total_consultas": 5,
    }
    return render(request, "dashboard.html", context)

from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')
