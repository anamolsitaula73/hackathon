# route_manager/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RouteManagerLoginForm
from .models import Route, Bus
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Route, BusStop
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Route

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Route
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Route

from django.http import JsonResponse
from .models import Route
import json
from django.shortcuts import render, redirect
from .models import Route
from django.http import JsonResponse

from django.shortcuts import render, redirect
from .models import Route
from django.http import HttpResponse

# route_manager/views.py

from django.shortcuts import render

def empty_page(request):
    return render(request, 'empty_page.html')


from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

# views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Route  # Import your Route model

# views.py
from django.http import JsonResponse
from django.shortcuts import render
from .models import Route

from django.shortcuts import render, redirect
from .forms import RouteForm

from django.shortcuts import render, redirect
from .forms import RouteForm

from django.shortcuts import render, redirect
from .forms import RouteForm

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Route
from django.shortcuts import render, redirect
from .forms import RouteForm
from .models import Route
from django.http import JsonResponse
from django.shortcuts import render
from .models import Route
from .forms import RouteForm
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Route

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RouteForm

from django.shortcuts import render
from .models import Route

from django.shortcuts import render
from .models import Route
import json

def view_saved_routes(request):
    # Fetch all saved routes from the database
    routes = Route.objects.all()

    # Prepare the routes data to pass to the template
    route_data = []
    for route in routes:
        route_data.append({
            'route_name': route.route_name,
            'starting_point': route.starting_point,
            'destination': route.destination,
            'route_data': json.loads(route.route_data)  # Convert the route_data JSON back to a list of coordinates
        })

    return render(request, 'route_manager/view_saved_routes.html', {'routes': route_data})


def save_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Route saved successfully!'})
        else:
            return JsonResponse({'message': 'Invalid data', 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)



def route_list(request):
    # Fetch all routes and bus stops
    routes = Route.objects.all()
    bus_stops = BusStop.objects.all()

    return render(request, 'route_manager/routelist.html', {
        'routes': routes,
        'bus_stops': bus_stops,
    })


# Route Manager Login View
def route_manager_login(request):
    if request.method == "POST":
        form = RouteManagerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('route_manager_home')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = RouteManagerLoginForm()

    return render(request, 'route_manager/login.html', {'form': form})

# Route Manager Home View
def route_manager_home(request):
    if not request.user.is_authenticated:
        return redirect('route_manager_login')

    routes = Route.objects.all()
    return render(request, 'route_manager/home2.html', {'routes': routes})


def create_route(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            route = Route.objects.create(
                name=data['name'],
                starting_point=data['starting_point'],
                destination=data['destination'],  # This now comes from the form
            )

            # Save bus stops
            for stop in data['bus_stops']:
                BusStop.objects.create(
                    route=route,
                    lat=stop['lat'],
                    lon=stop['lon']
                )

            return JsonResponse({"success": True, "route_id": route.id}, status=201)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)


# API View to Get Route Details
def get_route(request, route_id):
    try:
        route = Route.objects.get(id=route_id)
        route_data = {
            'start_lat': route.start_lat,
            'start_lon': route.start_lon,
            'end_lat': route.end_lat,
            'end_lon': route.end_lon,
            'name': route.name,
            'starting_point': route.starting_point,
            'destination': route.destination,
        }
        return JsonResponse({'route': route_data})
    except Route.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Route not found'}, status=404)

# Assign Route to Driver
def assign_route_to_driver(request, bus_id):
    if request.method == "POST":
        route_id = request.POST.get("route_id")
        try:
            bus = Bus.objects.get(id=bus_id)
            route = Route.objects.get(id=route_id)
            bus.route = route
            bus.save()
            return redirect('bus_details', bus_id=bus.id)
        except (Bus.DoesNotExist, Route.DoesNotExist):
            return JsonResponse({'success': False, 'message': 'Bus or Route not found'}, status=404)
    routes = Route.objects.all()
    return render(request, 'route_manager/assign_route.html', {'routes': routes})
