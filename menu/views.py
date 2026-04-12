from django.shortcuts import render
from .models import Dish # تأكد إن الاسم Dish أو  حسب ما سميته

def menu_view(request):
    dishes = Dish.objects.all() # هنا نسحب كل الوجبات من المدير
    return render(request, 'menu/menu.html', {'dishes': dishes})