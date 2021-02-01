from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image

# Create your views here.

@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assing current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image added succesfully")

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        #built form with data provided by te bookmarklet vie GET
        form = ImageCreateForm(data=request.GET)
    return render(request,
                    'images/image/create.html',
                    {'section':'images', 'form':form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 
                    'images/image/detail.html',
                    {'section':'images',
                    'image':image})
