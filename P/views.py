from django.shortcuts import render, redirect
from googletrans import Translator
from .forms import ImageForm
from .models import Image as ImageM

import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(extracted)
    form = ImageForm()
    return render(request, "index.html",{'form':form})

def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    if(text==""):
        tr= "Please Enter Text To Translate... Click on Translate again!!"
    elif(lang=="ZZ"):
        tr= "Please Choose Language... Click on Translate again!!"
    else:
        translator = Translator()
        dt = translator.detect(text)
        dt2 = dt.lang
        translated =translator.translate(text, lang)
        tr = translated.text
    return render(request, 'translated.html', {'translated': tr})

def extracted(request):
    rcParams['figure.figsize'] = 8, 16
    reader = easyocr.Reader(['en'])
    image=ImageM.objects.all()
    for i in image:
        c=i
    output = reader.readtext('static/images/'+str(c.photo))
    s=" "
    for i in output:
        s=s+i[-2]
    ex=s
    return render(request, "extracted.html",{'extracted':ex})





