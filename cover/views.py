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
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request.GET['animal_code']
    color_code = request.GET['color_code']
    guide_text = request.GET['guide_text']
    guide_text_placement = request.GET['guide_text_placement']

    img = Image.new('RGB', (256,256), 'white')

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    d = ImageDraw.Draw(img)

    font = ImageFont.truetype(ttf_path, 40)
    d.text((10,10), title, font=font, fill=(0,255,0,120))
        
    font = ImageFont.truetype(ttf_path, 20)
    d.text((10,60), top_text, font=font, fill=(0,255,0,255))

    font = ImageFont.truetype(ttf_path, 10)
    d.text((10,110), author, font=font, fill=(0,255,0,255))

    response = HttpResponse(content_type = 'image/png')
    img.save(response, format='PNG')
    return response