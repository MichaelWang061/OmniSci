from Project.models import *
from django.shortcuts import render
from django.db.models import F

import datetime


def search(request):
    if request.method == "GET":
        query = True
        key = request.GET.get('q')

        results = ProjectInfo.objects.filter(projection_name__icontains=key)
        for result in results:
            weight = F('participants_num') + F('views') * 0.4 + elapsedtime(F('publish_time')) * (-0.01)
            result.weight = weight
            result.save(update_fields=['weight'])
        results = results.order_by('weight')
        results = results.reverse()
        return render(request, "search.html", {"object_list": results, "query": query})
    else:
        return render(request, "search.html", {})


def elapsedtime(time):
    timediff = datetime.datetime.utcnow() - time
    return timediff
