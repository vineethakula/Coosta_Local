import cStringIO as StringIO
import csv

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

from properties.models import Property
from flags.models import FlaggedProperty


@csrf_exempt
@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/')
def dashboard_admin(request, value=None):
    if request.method == "POST":
        if "download" in request.POST:
            rows = Property.objects.all().order_by('id').values_list(
                "property_title", "address", "city", "state",
                 "zip_code", "home_type", "beds", "property_value",
                 "baths", "rooms", "property_size", "floors",
                 "roof", "basement", "year_built",
                 "other_features", "status", "year_renovated",
                 "car_park"
            )

            def data():
                for i in xrange(0, len(rows)+1):
                    csvfile = StringIO.StringIO()
                    csvwriter = csv.writer(csvfile)
                    if i == 0:
                        header = ["Sl No", "Property Title", "Address", "City",
                                  "State", "Zip Code", "Home Type",
                                  "Beds", "Property Value", "Baths", "Rooms",
                                  "Property Size", "Floors", "Roof",
                                  "Basement", "Year Built", "Other Features",
                                  "Status", "Year Renovated", "Car Park"]
                        csvwriter.writerow(header)
                    else:
                        row_data = [i]
                        for p in rows[i-1]:
                            if p:
                                try:
                                    row_data.append(
                                        str(p.encode('utf-8').strip())
                                    )
                                except:
                                    row_data.append(str(p))
                            else:
                                row_data.append("")
                        csvwriter.writerow(row_data)
                    yield csvfile.getvalue()
                pass
            response = HttpResponse(data(), content_type="text/csv")
            response[
                "Content-Disposition"] = "attachment; filename=coosta_listings.csv"
            return response

    # TODO may skip counting and filtering for specific requests, eg for Escrow
    # Others are not important
    total_property = Property.objects.count()
    total_user = User.objects.count()
    ca_property = Property.objects.filter(state='CA').count()

    los_angeles_property = Property.objects.filter(
        city__contains='Los Angeles').count()

    san_francisco_property = Property.objects.filter(
        city__contains='San Francisco').count()

    total_flagged_properties = FlaggedProperty.objects.count()

    template = loader.get_template('dashboard_admin/dashboard_admin.html')
    context_obj = {
        'total_property_count': total_property,
        'total_user_count': total_user,
        'ca_property_count': ca_property,
        'los_angeles_property_count': los_angeles_property,
        'san_francisco_property_count': san_francisco_property,
        'total_flagged_properties': total_flagged_properties,
        'user': request.user,
    }

    if value not in ('properties', 'users', 'escrow', 'non_pre_approved_user',
                     'flagged_properties'):
        context = RequestContext(request, context_obj)
        return HttpResponse(template.render(context))

    elif value == 'properties':
        state = Property.objects.values("state").distinct()
        city = Property.objects.values("city").distinct()
        search_state = request.GET.get('state')
        search_city = request.GET.get('city')

        reqs = ''
        reqs2 = ''
        if search_state:
            reqs = Property.objects.filter(
                Q(state__iexact=search_state)).count()
        elif search_city:
            reqs2 = Property.objects.filter(
                Q(city__iexact=search_city)).count()

        template = loader.get_template(
            'dashboard_admin/dashboard_admin_properties.html')
        new_context_obj = {
            'city_list': city,
            'state_list': state,
            'reqs': reqs,
            'reqs2': reqs2,
            'search_state': search_state,
            'search_city': search_city,
        }
        new_context_obj.update(context_obj)
        context = RequestContext(request, new_context_obj)
        return HttpResponse(template.render(context))

    elif value == 'users':
        search_users = request.GET.get('users')
        reqs1 = ''
        if search_users == 'SuperUser':
            reqs1 = User.objects.filter(is_superuser=True).count()
        elif search_users == 'Staff':
            reqs1 = User.objects.filter(is_staff=True).count()
        elif search_users == 'Normal-User':
            reqs1 = User.objects.filter(is_active=True, is_superuser=False,
                                        is_staff=False).count()

        template = loader.get_template(
            'dashboard_admin/dashboard_admin_users.html')
        new_context_obj = {
            'reqs1': reqs1,
            'search_users': search_users,
        }
        new_context_obj.update(context_obj)
        context = RequestContext(request, new_context_obj)
        return HttpResponse(template.render(context))

    # rendering escrow_admin page
    elif value == 'escrow':
        return render(request, 'dashboard_admin/dashboard_admin_escrow.html')

    # rendering non-pre-approved-user_admin_page
    elif value == 'non_pre_approved_user':
        return render(request,
                      'dashboard_admin/dashboard_admin_non_pre_approved_user.html')

    # rendering Flagged Properties
    elif value == 'flagged_properties':
        return render(request, 'dashboard_admin/dashboard_admin_flagged_properties.html')


class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    @staticmethod
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value
