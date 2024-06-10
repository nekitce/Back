# from Furniture_App.FurniturePart_view.domain_active import FurniturePart
# from Furniture_App.Furniture_view.domain_active import Furniture
# from django.http import HttpResponse
#
# from django.http import JsonResponse
#
#
# def show_furniture_info(request):
#     furniture_list = Furniture.get_furniture_all()
#     data = {'furniture_list': list(furniture_list.values())}
#     return JsonResponse(data)
#
#
# def parts_by_furniture_id(request, furniture_id):
#     parts = FurniturePart.get_parts_by_furniture_id(furniture_id)
#     data = {'parts': list(parts.values())}
#     return JsonResponse(data)
#
#
# def part_info(request, part_id):
#     part = FurniturePart.objects.get(id_part=part_id)
#     info = part.display_info()
#     return JsonResponse(info, safe=False)
#
#
# def delete_furniture(request, furniture_id):
#     try:
#         Furniture.domain_delete_furniture(furniture_id)
#         return HttpResponse("Furniture deleted successfully")
#     except Furniture.DoesNotExist:
#         return HttpResponse("Furniture not found", status=404)
