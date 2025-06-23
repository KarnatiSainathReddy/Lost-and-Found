from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LostFoundItem
from .forms import LostFoundItemForm
from django.http import HttpResponseForbidden
from django.contrib import messages

@login_required
def report_item(request):
    if request.method == 'POST':
        form = LostFoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.posted_by = request.user
            item.save()
            return redirect('view_items')
    else:
        form = LostFoundItemForm()
    return render(request, 'items/report_item.html', {'form': form})

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)

    if item.posted_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this item.")

    if request.method == 'POST':
        form = LostFoundItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('item_detail', item_id=item.id)
    else:
        form = LostFoundItemForm(instance=item)

    return render(request, 'items/report_item.html', {'form': form, 'edit_mode': True, 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)

    # Ensure only the user who posted the item can delete it
    if item.posted_by != request.user:
        return HttpResponseForbidden("You are not allowed to delete this item.")

    if request.method == "POST":
        item.delete()
        return redirect('profile')  # Or wherever you want to redirect after deletion

    # Optional: You can render a confirmation page before deleting
    return render(request, 'items/confirm_delete.html', {'item': item})


def view_items(request):
    items = LostFoundItem.objects.all().order_by('-date_reported')
    return render(request, 'items/view_items.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)
    return render(request, 'items/item_detail.html', {'item': item})
