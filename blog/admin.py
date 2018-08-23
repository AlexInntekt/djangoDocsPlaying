from django.contrib import admin
from .models import Post, Group

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
	  ('Membership',{'fields':['group']}),
	  ('Basic information',{'fields':['author']}),
      (None,{'fields':['title']}),
      (None,{'fields':['text']}),
      ('Date details',{'fields':['created_date']}),
      (None,{'fields':['published_date']}),
	]

	list_display = ('title', 'author' ,'created_date', 'group')

class GroupAdmin(admin.ModelAdmin):
	fieldsets = [
       ('Basic information',{'fields':['name']}),
	]
	inlines = [PostInline]


admin.site.register(Post,PostAdmin)
admin.site.register(Group, GroupAdmin)