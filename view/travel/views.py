from django.shortcuts import render, redirect
from django.views import View

from travel.models import Travel


class TravelWriteView(View):
    def get(self, request):
        return render(request, 'travel/write.html')

    def post(self, request):
        data = request.POST
        data = {
            'travel_budget' : data['travel-budget'],
            'travel_destination' : data['travel-destination'],
            'travel_date' : data['travel-date'],
            'travel_hotel_reservation' : data['travel-hotel-reservation']
        }

        travel = Travel.objects.create(**data)

        return redirect(travel.get_absolute_url())

class TravelDetailView(View):
    def get(self, request):
        print("들어옴")
        travel = Travel.objects.get(id=request.GET['id'])
        context = {
            'travel': travel
        }

        return render(request, 'travel/detail.html', context)
