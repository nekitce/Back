import json

from rest_framework.decorators import api_view

from Furniture_App.FurniturePart_view.domain_active import FurniturePart
from Furniture_App.Furniture_view.domain_active import Furniture
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse


@api_view(['GET'])
def show_furniture_info(request):


    furniture_list = Furniture.get_furniture_all()
    data = list(furniture_list.values())
    for i in data:
        parts = FurniturePart.get_parts_by_furniture_id(i["id_furniture"])
        print(parts.values())
        i["parts"] = list(parts.values())
    print(data)
    return JsonResponse(data, safe=False)


def parts_by_furniture_id(request, furniture_id):
    parts = FurniturePart.get_parts_by_furniture_id(furniture_id)
    data = {'parts': list(parts.values())}
    return JsonResponse(data)


def part_info(request, part_id):
    part = FurniturePart.objects.get(id_part=part_id)
    info = part.display_info()
    return JsonResponse(info, safe=False)


@csrf_exempt
def delete_furniture(request, furniture_id):
    if request.method == 'DELETE':
        try:
            Furniture.domain_delete_furniture(furniture_id)
            return HttpResponse("Furniture deleted successfully")
        except Furniture.DoesNotExist:
            return HttpResponse("Furniture not found", status=404)
    else:
        return HttpResponse("Method not allowed", status=405)


@csrf_exempt
def create_furniture(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Furniture(furniture_name=data["furniture_name"], count_part=data["count_part"], material=data["material"], weight=data["weight"]).save()
        return JsonResponse({'message': 'Furniture created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


@csrf_exempt
def update_furniture(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        furniture_id = data['id_furniture']
        new_name = data['furniture_name']
        new_count_part = data['count_part']
        new_material = data['material']
        new_weight = data['weight']
        Furniture.update_furniture_by_id(furniture_id, new_name, new_count_part, new_material, new_weight)
        return JsonResponse({'message': 'Furniture updated successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
