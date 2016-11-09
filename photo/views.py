from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from datetime import datetime
from django.contrib.auth.decorators import login_required




# template 디버깅용임 건들지마셈
photo_list = [{'title':'title입니다', 'contents':'contents입니다'},{'title':'title입니다', 'contents':'contents입니다'},
              {'title': 'title입니다', 'contents': 'contents입니다'},{'title':'title입니다', 'contents':'contents입니다'}]
date=datetime.today().strftime("%Y/%m/%d %H:%M")

def debug_login(request):
    return render(
        request,
        'login.html'
    )
def debug_main(request):
    return render(
        request,
        'main.html',
        {
            'photo_list': photo_list,
            'date' : date,
        }
    )
def debug_signup(request):
    return redirect('/debug/login')
def debug_insert(request):
    return redirect('/debug/main')