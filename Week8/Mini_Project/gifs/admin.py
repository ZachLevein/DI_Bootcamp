from django.contrib import admin
from gifs.models import Gif_Model, Category
from gifs.forms import Gif_Form



admin.site.register(Category)


# class CommentInline(admin.StackedInline):
#         model = Comment
#         extra = 4

class Gif_ModelAdmin(admin.ModelAdmin):
      
        fieldsets = [
            ('Personal Info', {'fields': ['uploader_name','title']}),
            ('User Preference', {'fields': ['url_link']}),
        ]
        # inlines = [CommentInline]

admin.site.register(Gif_Model, Gif_ModelAdmin)

