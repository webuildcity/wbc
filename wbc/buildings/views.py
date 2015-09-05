# -*- coding: utf-8 -*-
from models import Building
from django.shortcuts import render


def building(request, pk):

    building = Building.objects.get(pk=pk)
    return render(request, 'building/building.html', {'building': building})
