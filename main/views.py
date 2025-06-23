from django.shortcuts import render
from items.models import LostFoundItem

# Create your views here.
def home_view(request):
    lost_items = LostFoundItem.objects.filter(status='lost').order_by('-date_reported')[:3]
    found_items = LostFoundItem.objects.filter(status='found').order_by('-date_reported')[:3]

    return render(request, 'home.html', {
    'lost_items': lost_items,
    'found_items': found_items,
    })