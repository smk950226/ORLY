from django.shortcuts import render, redirect
from PIL import Image,ImageFont, ImageDraw
from .forms import CoverForm
from django.http import HttpResponse
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {
        'form': form,
    })

def image_generator(request):
    img = Image.new('RGB', (256,256), 'white')

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    font = ImageFont.truetype(ttf_path, 40)
    d = ImageDraw.Draw(img)

    d.text((10,10), 'Hello', font=font, fill=(0,255,0,120))
    d.text((10,60), 'World', font=font, fill=(0,255,0,255))

    response = HttpResponse(content_type = 'image/png')
    img.save(response, format='PNG')
    return response