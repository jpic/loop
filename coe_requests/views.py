from django import http
from django import shortcuts
from django.core.urlresolvers import reverse
from django.views.generic import detail

from .models import Offering, Platform, PlatformOffering, Request
from .forms import RequestForm


def request_create(request):
    form_class = RequestForm

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            obj = form.save()
            return http.HttpResponseRedirect(
                reverse('admin:coe_requests_request_change', args=(obj.pk,)),
            )
    else:
        form = form_class()

    context = dict(form=form)

    return shortcuts.render(
        request,
        'coe_requests/request_form.html',
        context
    )


class PlatformConfiguration(detail.BaseDetailView):
    model = Platform

    def get(self, request, *args, **kwargs):
        platform = self.get_object()

        return http.JsonResponse({
            # Return the list of allowed offerings for this platform
            'offerings': list(platform.offerings.values_list('pk', 'name'))
        })


class PlatformOfferingConfiguration(detail.BaseDetailView):
    model = PlatformOffering

    def get(self, request, *args, **kwargs):
        platformoffering = PlatformOffering.objects.filter(
            platform__pk=kwargs['platform_pk'],
            offering__pk=kwargs['offering_pk'],
        ).first()

        return http.JsonResponse({
            # Return the list of fields to hide for this platform offering
            'hide_fields': (
                platformoffering.hide_fields.split(',')
                if platformoffering else []
            ),
        })
