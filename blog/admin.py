from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from .models import Category, Post, Project, Technology
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', )
    list_display = ('id', 'slug', 'title', )
    list_display_links = ('slug', 'title', )
    prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm
    list_display = ('id', 'title', 'category_id', 'slug', 'views', 'get_miniature')
    fields = ('title', 'slug', 'content', 'get_miniature', 'photo', 'views', 'created_at', 'category_id', )
    readonly_fields = ('created_at', 'views', 'get_miniature')
    list_display_links = ('slug', 'title', )
    prepopulated_fields = {"slug": ("title",)}

    def get_miniature(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="60">')
        return '-'

    get_miniature.short_description = 'Miniature'


class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm
    fields = ('title', 'slug', 'content', 'get_miniature', 'photo', 'views' 'technology_id', )
    list_display = ('id', 'title', 'slug', 'get_miniature', 'views', )
    list_display_links = ('id', 'title', )
    readonly_fields = ('get_miniature', 'views', )
    prepopulated_fields = {"slug": ("title",)}

    get_miniature = PostAdmin.get_miniature
    get_miniature.short_description = 'Miniature'


class TechnologyAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', )
    list_display = ('id', 'name', 'slug', )
    list_display_links = ('id', 'name', )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
