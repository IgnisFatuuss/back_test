from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import reverse
from nested_admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin
from django.contrib.contenttypes.admin import GenericTabularInline






class ContactsInline(NestedTabularInline):
    model = Contacts
    extra = 1

class PhonesInline(NestedTabularInline):
    model = Phones
    extra = 1

class SocialInline(NestedTabularInline):
    model = Social
    extra = 1

class GeneralSettingsAdmin(admin.ModelAdmin):
    inlines = [ContactsInline, SocialInline, PhonesInline]
    def has_add_permission(self, request):
        # Проверяем, есть ли записи в модели GeneralSettings
        if GeneralSettings.objects.exists():
            return False  # Запрещаем создание новых записей
        return True  # Разрешаем создание первой записи

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('', self.redirect_to_edit),
        ]
        return my_urls + urls

    def redirect_to_edit(self, request):
        # Перенаправляем на страницу редактирования первой записи,
        # если она существует
        if GeneralSettings.objects.exists():
            url = reverse('admin:website_generalsettings_change', args=[1])
        else:
            # Если записей нет, перенаправляем на страницу создания новой записи
            url = reverse('admin:website_generalsettings_add')
        return HttpResponseRedirect(url)


class CommentariesInline(admin.StackedInline):
    model = Commentaries
    def get_extra(self, request, obj=None, **kwargs):
        default_extra = 1
        return default_extra

class BlogsAdminForm(forms.ModelForm):
    content = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Blogs
        fields = '__all__'

class BlogsAdmin(admin.ModelAdmin):
    inlines = [CommentariesInline]
    form = BlogsAdminForm
    prepopulated_fields = {"slug": ('name',), }

class PagesAdminForm(forms.ModelForm):
    content = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Pages
        fields = '__all__'

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    form = PagesAdminForm
    prepopulated_fields = {"slug": ('name',), }


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ["name",]
    prepopulated_fields = {"slug": ('name',), }




admin.site.register(Tags)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Commentaries)
admin.site.register(Regions)
admin.site.register(Contacts)
admin.site.register(Social)
admin.site.register(GeneralSettings, GeneralSettingsAdmin)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ["question",]
    prepopulated_fields = {"slug": ('question',), }