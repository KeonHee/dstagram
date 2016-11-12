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


def photo_list(request):
    if request.method == 'GET':
        try:
            photos = Photo.objects.all()
        except Photo.DoesNotExist:
            return Http404('Photo does not exist')
        return render(
            request,
            'main.html',
            {
                'photos': photos,
             }
        )
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST.get('contents')
        if 'file' in request.FILES:
            image_file = request.FILES['file']
        else:
            image_file = False
        Photo.objects.create(user=request.user, title=title, contents=contents, image_file=image_file)
        return HttpResponseRedirect('/main')


# 업데이트, 삭제 구현
def photo_detail(request, photo_id):

    photo = Photo.objects.get(id=photo_id)

    if photo.DoesNotExist:
        return Http404('Photo does not exist') # get_object_or_404 함수도 있다.

    else:
        # /photos -> /update 로 이동
        if request.method == 'GET':
            return render(
                request,
                'update.html',
                {
                    'photo': photo,
                }
            )

        # /update 에서
        else:

            if request.method == 'PUT' or request.method == 'PATCH':
                # logging.warning('photo : ', photo)
                logging.warning('request : ', request)

                updated_fields = []
                if request.PUT['title']:
                    photo.title = request.PUT['title']
                    updated_fields.append('title')
                if request.PUT.get('contents'):
                    photo.contents = request.PUT.get('contents')
                    updated_fields.append('contents')
                if 'file' in request.FILES:
                    photo.image_file = request.FILES['file']
                    updated_fields.append('image_file')

                photo.save(updated_fields)

            if request.method == 'DELETE':
                Photo.delete(id=photo_id)

            return HttpResponseRedirect('/photos')

# template 디버깅용임 건들지마셈
photos = [{'id': 0, 'title': 'title0입니다', 'contents': 'contents0입니다'},
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
            'photos': photos,
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