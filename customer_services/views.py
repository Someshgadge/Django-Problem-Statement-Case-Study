from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm, RequestUpdateForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save()
            return redirect('customer_services:submit_request')
    else:
        form = ServiceRequestForm()
    
    context = {'form': form}
    return render(request, 'service_requests/submit_request.html', context)

@login_required
def track_requests(request):
    user = request.user
    service_requests = ServiceRequest.objects.filter(customer=user)
    context = {'service_requests': service_requests}
    return render(request, 'service_requests/track_requests.html', context)

@login_required
def update_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    if request.method == 'POST':
        form = RequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('customer_services:track_requests')
    else:
        form = RequestUpdateForm(instance=service_request)
    
    context = {'form': form, 'service_request': service_request}
    return render(request, 'service_requests/update_request.html', context)
