from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from datetime import datetime
from django.contrib.auth.decorators import login_required




# template 디버깅용임 건들지마셈
photo_list = [{'id': 0, 'title': 'title0입니다', 'contents': 'contents0입니다'},
              {'id': 1, 'title': 'title1입니다', 'contents': 'contents1입니다'},
              {'id': 2, 'title': 'title2입니다', 'contents': 'contents2입니다'},
              {'id': 3, 'title': 'title3입니다', 'contents': 'contents3입니다'}]
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

def debug_update_page(request):
    import logging
    logging.warning(request.POST)
    id=int(request.POST.get('id')[0])
    logging.warning(id)
    return render(
        request,
        'update.html',
        {
            'photo': photo_list[id],
            'date': date,
        }
    )

def debug_update(request):
    return redirect('/debug/main')