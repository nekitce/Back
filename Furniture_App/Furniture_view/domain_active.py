
from django.db import models

class Furniture(models.Model):
    id_furniture = models.IntegerField(primary_key=True)
    furniture_name = models.CharField(max_length=50, unique=True)
    count_part = models.IntegerField()
    material = models.CharField(max_length=50)
    weight = models.FloatField()

    # Domain Model
    @classmethod
    def get_furniture_all(cls):
        # Используем паттерн domain model для получения всех объектов мебели
        return cls.objects.all()

    @classmethod
    def domain_delete_furniture(cls, furniture_id):
        furniture_obj = cls.objects.get(id_furniture=furniture_id)
        furniture_obj.delete_furniture()

    @staticmethod
    def domain_create_furniture(furniture_name, count_part, material, weight):
        # Вызываем метод active record через метод domain
        furniture = Furniture()
        furniture.create_furniture(furniture_name, count_part, material, weight)

    @classmethod
    def update_furniture_by_id(cls, furniture_id, new_name, new_count_part, new_material, new_weight):
        furniture = cls.objects.get(id_furniture=furniture_id)
        furniture.update_furniture(new_name, new_count_part, new_material, new_weight)

    # Active Record
    # Используем паттерн active record для вывода информации о мебели
    def display_info(self):
        return f"Name: {self.furniture_name}, Count: {self.count_part}, Material: {self.material}, " \
               f"Weight: {self.weight}"

    def delete_furniture(self):
        self.delete()

    def create_furniture(self, furniture_name, count_part, material, weight):
        # Создаем новую запись в базе данных с помощью active record
        self.furniture_name = furniture_name
        self.count_part = count_part
        self.material = material
        self.weight = weight
        self.save()

    def update_furniture(self, new_name, new_count_part, new_material, new_weight):
        self.furniture_name = new_name
        self.count_part = new_count_part
        self.material = new_material
        self.weight = new_weight
        self.save()
