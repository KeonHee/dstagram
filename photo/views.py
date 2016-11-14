from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.contrib.auth.decorators import login_required
from .models import Photo
import logging


def photo_list(request):
    if request.method == 'GET':
        try:
            photos = Photo.objects.all()  # get_object_or_404 함수 대체 가능
        except Photo.DoesNotExist:
            raise Http404('Photo does not exist')
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
        return HttpResponseRedirect('/photos')


def photo_detail(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        raise Http404('Photo does not exist')

    if request.method == 'GET':
        return render(
            request,
            'update.html',
            {
                'photo': photo,
            }
        )
    else:
        if request.method == 'POST':
            try:
                if request.POST['method_type'] == 'PUT':
                    if request.POST['title']:
                        photo.title = request.POST['title']
                    if request.POST['contents']:
                        photo.contents = request.POST['contents']
                    if 'file' in request.FILES:
                        photo.image_file = request.FILES['file']
                    photo.save()
                if request.POST['method_type'] == 'DELETE':
                    photo.delete()
                return HttpResponseRedirect('/photos')
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/photos')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if username and password and email:
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                user = User.objects.create_user(username, email, password)
            else:
                pass
                # 예외 2 : username 이 중복되는 기존 사용자가 있음
        else:
            pass
            # 예외 1 : request 로 username, password, email 중 하나도 안넘어옴
        return HttpResponseRedirect('/accounts/login')

