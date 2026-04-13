from django.contrib import admin
from .models import Staff #1 убираем функцию admin.site.register(Staff) и добавляем класс StaffAdmin
from django.utils.safestring import mark_safe


# Register your models here.
#1 admin.site.register(Staff)

@admin.register(Staff) #2 добавляем декоратор для регистрации модели Staff с помощью класса StaffAdmin
class StaffAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'photo_tag', 'name', 'position', 'is_visible') 
    list_filter = ('is_visible',)
    search_fields = ('name', 'position')
    list_editable = ('name', 'position', 'is_visible') 
    
    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />') #return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />'
        
    photo_tag.short_description = 'Photo'
    
    #list_per_page = 10
    #fields = ('name', 'position', 'photo', 'is_visible', 'sort', 'facebook', 'instagram', 'twitter', 'linkedin')
    #ordering = ('sort',)
    