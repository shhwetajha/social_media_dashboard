from django.contrib import admin
from .models import *

# Register your models here.
class postAdmin(admin.ModelAdmin):
    class Meta:
        model=post
        fields='__all__'

class LikePostAdmin(admin.ModelAdmin):
    class Meta:
        model=LikePost
        fields='__all__'

class CommentPostAdmin(admin.ModelAdmin):
    class Meta:
        model=CommentPost
        fields='__all__'

admin.site.register(post,postAdmin)
admin.site.register(LikePost,LikePostAdmin)
admin.site.register(CommentPost,CommentPostAdmin)
