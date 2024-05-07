from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Resource_view, resLink_view, Event_view, eventLink_view
from django.core import serializers
from django.http import HttpResponse


# def res_json(request):
#     res_objects = [*Resource.objects.all(), *resLink.objects.all()]
#     resources = serializers.serialize('json', res_objects)
#     return HttpResponse(resources, content_type='application/json')

def res_json(request):
    res_objects = Resource_view.objects.all()
    resLink_objects = resLink_view.objects.all()

    ctx = {}
    url_parameter = request.GET.get("q")
    print(url_parameter)

    if url_parameter:
        res_json = res_objects.filter(name__icontains=url_parameter)
    else:
        res_json = res_objects

    ctx["res_json"] = res_json
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:
        html = render_to_string(
            template_name="test.html",
            context={'res_objects': res_json, 'resLink_objects': resLink_objects}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "resource.html", context=ctx)


def ev_json(request):
    ev_objects = Event_view.objects.all()
    evLink_objects = eventLink_view.objects.all()

    ctx = {}
    url_parameter = request.GET.get("q")
    print(url_parameter)

    if url_parameter:
        ev_json = ev_objects.filter(name__icontains=url_parameter)
    else:
        ev_json = ev_objects

    ctx["ev_json"] = ev_json
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:
        html = render_to_string(
            template_name="evfltr.html",
            context={'ev_objects': ev_json, 'evLink_objects': evLink_objects}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "events.html", context=ctx)


def members(request):
    return HttpResponse("Hello world!")
