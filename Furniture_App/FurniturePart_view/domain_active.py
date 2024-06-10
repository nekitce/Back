from django.db import models

from Furniture_App.Furniture_view.domain_active import Furniture


class FurniturePart(models.Model):
    id_part = models.IntegerField(primary_key=True)
    part_name = models.CharField(max_length=50)
    part_weight = models.FloatField(null=True)
    unique_code = models.TextField()
    furniture_id = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    flag = models.BooleanField(default=False)

    # Domain Model
    @classmethod
    def get_parts_by_furniture_id(cls, id_furniture):
        furniture = Furniture.objects.get(id_furniture=id_furniture)
        parts = cls.objects.filter(furniture_id=furniture)
        return parts

    # Active Record
    # Используем паттерн active record для вывода информации о части мебели
    def display_info(self):
        return f"Name: {self.part_name}, Weight: {self.part_weight}, Unique Code: {self.unique_code}, " \
               f"Furniture ID: {self.furniture_id}, Flag: {self.flag}"
