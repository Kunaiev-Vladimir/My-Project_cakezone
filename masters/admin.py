from django.contrib import admin
from .models import Staff #1 убираем функцию admin.site.register(Staff) и добавляем класс StaffAdmin


# Register your models here.
#1 admin.site.register(Staff)

@admin.register(Staff) #2 добавляем декоратор для регистрации модели Staff с помощью класса StaffAdmin
class StaffAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'photo', 'position', 'is_visible') 
    list_filter = ('is_visible',)
    search_fields = ('name', 'position')
    list_editable = ('is_visible',) 
    list_per_page = 10
    fields = ('name', 'position', 'photo', 'is_visible', 'sort', 'facebook', 'instagram', 'twitter', 'linkedin')
    ordering = ('sort',)
    