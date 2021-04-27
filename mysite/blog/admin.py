from django.contrib import admin
from .models import Post

from django.contrib import admin
from .models import Post, Comment



# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    



