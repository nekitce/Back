from django.contrib import admin

from Furniture_App.FurniturePart_view.domain_active import FurniturePart
from Furniture_App.Furniture_view.domain_active import Furniture

admin.site.register(Furniture)
admin.site.register(FurniturePart)

