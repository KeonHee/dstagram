from django.db import models
from django.conf import settings
import os


class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, help_text='회원')
    image_file = models.ImageField(
        upload_to='./uploaded_image',
        default='/uploaded_image/default_image.PNG',
        null=True,
        blank=True,
        help_text='사진'
    )
    title = models.TextField(max_length=100, null=True, blank=True, help_text='제목')
    contents = models.TextField(max_length=500, null=True, blank=True, help_text='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk', '-created_at')

    def delete(self, *args, **kwargs):
        if not (self.image_file.url == '/uploads/uploaded_image/default_image.PNG'): # default image 삭제 방지
            self.image_file.delete()
        super(Photo, self).delete(*args, **kwargs)

    def __str__(self):
        return 'photo_' + str(self.id)
