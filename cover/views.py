from django.shortcuts import render, redirect
from PIL import Image,ImageFont, ImageDraw
from .forms import CoverForm
from django.http import HttpResponse
from django.conf import settings
from .utils import COLOR_CODES

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

    animal_path = settings.ROOT('assets', 'animal', '{}.png'.format(animal_code))
    animal_img = Image.open(animal_path)

    color = COLOR_CODES[int(color_code)]

    img = Image.new('RGB', (500,700), (255,255,255))
    animal_img = animal_img.resize((400,400))

    img.paste(animal_img, (50,40))

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    d = ImageDraw.Draw(img)
    
    d.rectangle((20,0,480,10), fill = color)
    
    d.rectangle((10,400,480,510), fill = color)

    font = ImageFont.truetype(ttf_path, 70)
    d.text((45,430), title, font=font, fill=(255,255,255,255))
        
    font = ImageFont.truetype(ttf_path, 20)
    d.text((160,15), top_text, font=font, fill=(0,0,0,255))

    font = ImageFont.truetype(ttf_path, 25)
    d.text((360,655), author, font=font, fill=(0,0,0,255))
    
    position = (125,505)#bottom-right
    
    font = ImageFont.truetype(ttf_path, 30)
    d.text(position, guide_text, font=font, fill=(0,0,0,255))

    response = HttpResponse(content_type = 'image/png')
    img.save(response, format='PNG')
    return response