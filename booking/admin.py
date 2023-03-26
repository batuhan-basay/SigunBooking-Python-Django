from collections import UserString
from django.contrib import admin

from booking.models import Cities,Categories, Comments,Menu, Menu_Category, Place_Img, Places, Places_Features, Rezervation, Roles, Table_Layout, User

# Register your models here.
admin.site.register(Places)
admin.site.register(Categories)
admin.site.register(Comments)
admin.site.register(Places_Features)
admin.site.register(Place_Img)
admin.site.register(Menu)
admin.site.register(Menu_Category)
admin.site.register(Table_Layout)
admin.site.register(Rezervation)
admin.site.register(User)
admin.site.register(Roles)
admin.site.register(Cities)