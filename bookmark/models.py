from django.db import models
from django.urls import reverse
# reverse - URL패턴의 이름과 추가 인자를 전달받아 URL생성하는 메소드
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    def __str__(self):
        return "이름 : "+self.site_name + ", 주소 :" +self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])