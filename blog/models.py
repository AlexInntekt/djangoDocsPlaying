
from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

 #you can reversely access the model with: Group.objects.all().first().post_set.all().first().title

class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

       
class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE,)
    followers  = models.ManyToManyField(User, related_name='followers', blank=True)
    following  = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username