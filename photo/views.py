from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

import logging

from .models import Photo


from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from datetime import datetime
from django.contrib.auth.decorators import login_required

date=datetime.today().strftime("%Y/%m/%d %H:%M")


# https://docs.djangoproject.com/en/1.10/intro/tutorial03/
def main(request):
    if request.method == 'GET':
        # 사진 글이 없을 경우 예외 처리
        try:
            photo_list = Photo.objects.all()
        except Photo.DoesNotExist:
            raise Http404('Photo does not exist')

        context = {
            'photo_list': photo_list,
            'date': ' ', # 이 부분 처리 안해도 템플릿에서 알아서 처리함
            }
        return render(request, 'main.html', context)


# https://docs.djangoproject.com/en/1.10/intro/tutorial04/
# http://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it
def insert(request):
    # warning 으로 request 에서 제대로 값이 넘어왔는지 확인해보자
    if request.method == 'POST':
        title = request.POST['title']
        # contents_ = request.POST['contents']
        contents = request.POST.get('contents', False) # 두번째인자 디폴트값
        # image_file = request.POST['uploadImage']
        image_file = request.POST.get('uploadImage', False)

        logging.warning(request.POST)
        # logging.warning('title_', title, ' contents', contents)
        # logging.warning('image_file', image_file)

        Photo.objects.create(title=title, contents=contents, image_file=image_file)
        return HttpResponseRedirect('/main')


# template 디버깅용임 건들지마셈
photo_list = [{'id': 0, 'title': 'title0입니다', 'contents': 'contents0입니다'},
              {'id': 1, 'title': 'title1입니다', 'contents': 'contents1입니다'},
              {'id': 2, 'title': 'title2입니다', 'contents': 'contents2입니다'},
              {'id': 3, 'title': 'title3입니다', 'contents': 'contents3입니다'}]

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