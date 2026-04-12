from django.db import models

class Dish(models.Model):
    # حقول اللغة العربية
    name_ar = models.CharField(max_length=100, verbose_name="الاسم بالعربي")
    
    name_en = models.CharField(max_length=100, verbose_name="الاسم بالإنجليزي")
    
    description_ar = models.TextField(verbose_name="الوصف بالعربي")
    
    # حقول اللغة الإنجليزية
    name_en = models.CharField(max_length=100, verbose_name="الاسم بالإنجليزي")

    name_ar = models.CharField(max_length=100, verbose_name="الاسم بالعربي")
    description_en = models.TextField(verbose_name="الوصف بالإنجليزي")
    
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='dishes/', verbose_name="الصورة")

    def __str__(self):
        return self.name_ar