from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
	  ('Membership',{'fields':['group']}),
	  ('Basic information',{'fields':['author']}),
      (None,{'fields':['title']}),
      (None,{'fields':['text']}),
      ('Date details',{'fields':['created_date']}),
      (None,{'fields':['published_date']}),
	]

class GroupAdmin(admin.ModelAdmin):
	fieldsets = [
       ('Basic information',{'fields':['name']}),
	]

admin.site.register(Post,PostAdmin)
admin.site.register(Group, GroupAdmin)