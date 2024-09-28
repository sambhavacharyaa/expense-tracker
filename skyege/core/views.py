from django.shortcuts import render

# Create your views here.

# TODO: Define views for each of these functions
def index(request):
    return render(request, 'main/index.html')
def dashboard(request):
    return render(request, 'main/dashboard.html')
def charts(request):
    return render(request, 'main/charts.html')
def reports(request):
    return render(request, 'main/reports.html')