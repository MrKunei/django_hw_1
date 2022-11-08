import json

from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from ads.models import Ad, Category



# Create your views here.

def index(request):
    return JsonResponse({"status": "ok"}, status=200)

@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):

    def get(self, request):
        ads = Ad.objects.all()

        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_publish": ad.is_publish
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        ad = Ad.objects.create(
            name = ads_data['name'],
            author = ads_data['author'],
            description = ads_data['description'],
            price = ads_data['price'],
            address = ads_data['address'],
            is_publish = ads_data['is_publish']
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_publish": ad.is_publish
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):

    def get(self, request):
        cat_s = Category.objects.all()

        response = []
        for cat in cat_s:
            response.append({
                "id": cat.id,
                "name": cat.name
            })

        return JsonResponse(response, safe=False)


    def post(self, request):
        cat_data = json.loads(request.body)

        cat = Category.objects.create(
            name = cat_data['name']
        )

        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_publish": ad.is_publish
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not Found'}, status=404)

        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        })
