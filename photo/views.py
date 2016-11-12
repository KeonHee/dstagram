from django.http import Http404, HttpResponseRedirect
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
        if request.method == 'PUT' or request.method == 'PATCH':
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


def debug_signup(request):
    pass