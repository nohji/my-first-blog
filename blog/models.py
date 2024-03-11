from django.conf import settings
from django.db import models
from django.utils import timezone

# class는 객체를 정의한다는 것을 알려 줌.
# Post는 모델의 이름. 항상 클래스 이름의 첫 글자는 대문자로
# models 는 Post가 장고 모델임을 의미. 이 코드때문에 Post가 DB에 저장되어야 한다고 알게 됨.
class Post(models.Model): 
    # CASCADE : ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text