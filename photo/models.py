from django.db import models
from django.conf import settings


# 사진 업로드 경로 리턴
def image_file_path(instance, filename):
    return 'user_{0}_{1}'.format(instance.user.id, filename)


# 사진
class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, help_text='회원')
    image_file = models.ImageField(upload_to='/uploaded_image', null=True, blank=True, help_text='사진')
    title = models.TextField(max_length=100, null=True, blank=True, help_text='제목')
    contents = models.TextField(max_length=500, null=True, blank=True, help_text='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 사진 게시글의 정렬 순서 결정(id 역순으로, 최근 추가된 순서대로)
        ordering = ('-pk', '-created_at')

    def __str__(self):
        # 사진 게시글의 정보 출력(id)
        return 'photo_' + str(self.id)