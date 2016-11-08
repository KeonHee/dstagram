from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.contrib.auth.decorators import login_required




# template 디버깅용임 건들지마셈
def debug_login(request):
    return render(
        request,
        'login.html'
    )
def debug_main(request):
    return render(
        request,
        'main.html'
    )
def debug_signup(request):
    return redirect('/debug/login')