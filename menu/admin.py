from django.contrib import admin
from django.utils.html import format_html
from .models import Dish  # الاستيراد لازم يكون فوق أول شيء

class DishAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en','price', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "لا توجد صورة"
    
    display_image.short_description = 'صورة الوجبة'

# التسجيل لازم يكون آخر سطر في الملف
admin.site.register(Dish, DishAdmin)