from django.contrib import admin

from .models import Post, Comment
# Register your models here.

class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 2

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title' ,'image']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [CommentsInline]
    list_display = ('title', 'reacts', 'pub_date',)
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
