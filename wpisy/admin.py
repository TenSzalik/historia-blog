from django.contrib import admin
from .models import Entry, Review, Tag, MainPicture

admin.site.register(Entry)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(MainPicture)
