from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect
from .models import App
import json

@csrf_exempt
def add_app(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            app = App(
                app_name=data.get('app_name'),
                version=data.get('version'),
                description=data.get('description')
            )
            app.save()
            return JsonResponse({'message': 'App added successfully', 'app_id': app.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_app(request):
    app_id = request.GET.get('app_id')  # Fetch 'app_id' from query parameters
    if not app_id:
        return JsonResponse({'error': 'App ID is required'}, status=400)
    
    try:
        app = App.objects.get(id=app_id)
        return JsonResponse({
            'app_name': app.app_name,
            'version': app.version,
            'description': app.description
        }, status=200)
        
    except App.DoesNotExist:
        return JsonResponse({'error': 'App not found'}, status=404)

@csrf_exempt
def delete_app(request, id):
    if request.method == 'DELETE' or request.method == 'POST':  # Allow POST for delete
        try:
            app = get_object_or_404(App, id=id)
            app.delete()
            return redirect('app_management')  # Redirect to app management page
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def app_management(request):
    if request.method == 'POST':
        app_name = request.POST.get('app_name')
        version = request.POST.get('version')
        description = request.POST.get('description')
        App.objects.create(app_name=app_name, version=version, description=description)

    apps = App.objects.all()
    return render(request, 'app_management.html', {'apps': apps})