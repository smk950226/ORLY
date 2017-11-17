from django.shortcuts import render, redirect
from PIL import Image
from .forms import CoverForm
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            return redirect('cover:index')
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {
        'form': form,
    })

def image_generator(request):
    img = Image.new('RGB', (256,256), 'yellow')
    response = HttpResponse(content_type = 'image/jpeg')
    img.save(response, format='JPEG')
    return response