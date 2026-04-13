from django.contrib import admin
from .models import Category, Dish
from django.utils.safestring import mark_safe


# Register your models here.

#admin.site.register(Category) 
#admin.site.register(Dish)

class DishInLine(admin.TabularInline):
    
    model = Dish
    fields = ('name', 'price', 'is_visible', 'sort')
 
@admin.register(Category) # второй способ регистрации модели Category с помощью декоратора    
class CategoryAdmin(admin.ModelAdmin):
    
    inlines = (DishInLine, )
    list_display = ('name', 'is_vsible', 'sort')

#@admin.register(Category) # первый способ регистрации модели Category с помощью декоратора
#class CategoryAdmin(admin.ModelAdmin):
    
    #list_display = ('id', 'name', 'is_vsible') 
    #list_filter = ('is_vsible',)
    #search_fields = ('name',)
    #list_editable = ('name', 'is_vsible') 
    
    
    #list_per_page = 10
    #fields = ('name', 'is_visible')
    #ordering = ('id',)
    
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    
    list_display = ('photo_src_tag', 'name', 'price', 'is_visible', 'sort', 'category') 
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'category__name')
    list_editable = ('price', 'is_visible', 'sort') 
    

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />') #return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />'
        
    photo_src_tag.short_description = 'Dish Photo' 
    
    #list_per_page = 10
    #fields = ('name', 'category', 'description', 'price', 'photo', 'is_visible')
    #ordering = ('id',)  