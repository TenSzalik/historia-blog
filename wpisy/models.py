from django.db import models
from django.utils import timezone
import uuid
from ckeditor.fields import RichTextField

class Entry(models.Model):
    title = models.CharField(max_length=34)
    subtitle = models.CharField(max_length=156)
    thumbnail = models.ImageField(null=True, blank=True)
    description = RichTextField()
    source = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    heart_count = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    shows = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    #podepnij PostgreSQL!

    @property
    def imageURL(self):
        try:
            img = self.thumbnail.url
        except:
            img = ''
        return img

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down'),
    )

    user = models.CharField(max_length=24, default="Jasiek")
    single_entry = models.ForeignKey(Entry, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True,)
    value = models.CharField(max_length=50, choices=VOTE_TYPE,)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user

class Tag(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=280, default="Domyślny opis")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    left_or_right = models.CharField(max_length=255, default="left")
    when = models.CharField(max_length=280, default="Poza czasem")

    def __str__(self):
        return self.name

class MainPicture(models.Model):
    content = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, default="Główny")