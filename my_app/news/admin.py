from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import News, Category


# Register your models here.
# View this models in admin Django panel

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ("id", "title", "category", "created_at", "updated_at", "is_published", "get_photo")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "category")
    fields = ("title", "category", "content", "photo", "get_photo", "is_published", "views", "created_at", "updated_at")
    readonly_fields = ("get_photo", "views", "created_at", "updated_at")
    save_on_top = True

    def get_photo(self, photo_obj):
        if photo_obj.photo:
            return mark_safe(f'<img src="{photo_obj.photo.url}" width="125">')
        else:
            return 'Photo is empty'

    get_photo.short_description = 'Photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)

admin.site.site_title = 'Control news'
admin.site.site_header = 'Control news'
