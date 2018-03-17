from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=150)
    text = models.TextField()
    post_picture = models.FileField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
