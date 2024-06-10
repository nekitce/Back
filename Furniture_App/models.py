#
# from django.db import models
#
# class Furniture(models.Model):
#     id_furniture = models.IntegerField(primary_key=True)
#     furniture_name = models.CharField(max_length=50)
#     count_part = models.IntegerField()
#     material = models.CharField(max_length=50)
#     weight = models.DecimalField(max_digits=10, decimal_places=2)
#     search = models.BooleanField(default=False)
#
# class FurniturePart(models.Model):
#     id_part = models.IntegerField(primary_key=True)
#     part_name = models.CharField(max_length=50)
#     part_weight = models.FloatField(null=True)
#     unique_code = models.TextField()
#     id_furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
#
# class Code(models.Model):
#     id = models.IntegerField(primary_key=True)
#     code = models.TextField()
#     id_part = models.ForeignKey(FurniturePart, on_delete=models.CASCADE)
#
# class Pallets(models.Model):
#     id_pallet = models.IntegerField(primary_key=True)
#
# class Users(models.Model):
#     id_user = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     second_name = models.CharField(max_length=50, null=True)
#     login = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     role = models.CharField(max_length=50)
#
# class CompletePackage(models.Model):
#     id_package = models.IntegerField(primary_key=True)
#     instruction_card = models.TextField(null=True)
#     id_pallet = models.ForeignKey(Pallets, on_delete=models.CASCADE)
#
# class Sborka(models.Model):
#     id_sborka = models.IntegerField(primary_key=True)
#     id_part = models.ForeignKey(FurniturePart, on_delete=models.CASCADE)
#     id_pallet = models.ForeignKey(Pallets, on_delete=models.CASCADE)
#     id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
#
# class Transporter(models.Model):
#     id_delivery = models.IntegerField(primary_key=True)
#     destination_point = models.CharField(max_length=50)
#     delivery_form = models.CharField(max_length=50)
#     id_package = models.ForeignKey(CompletePackage, on_delete=models.CASCADE)
#
