from django.contrib import admin
from .models import Information, Profile
from django.utils.html import format_html


# Register your models here.
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lname", "email", "click_me")
    def lname(self, obj):
        return format_html(f'<span style="color:red;">{ obj.lastname }</span>')

    def click_me(self, obj):
        return format_html(f'<a href="/admin/crud1/information/{ obj.id }" class="default"> View <a>')

# admin.site.register(Information)


admin.site.register(Profile)