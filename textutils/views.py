from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = (request.POST.get('text','default')).strip()

    #Variables
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    newlineremove = request.POST.get('newlineremove','off')

    #func
    if removepunc == 'on' :
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext :
            if char not in punctuations :
                analyzed+=char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on' :
        analyzed=""
        for char in djtext :
            analyzed+=char.upper()

        params = {'purpose' : 'Changed to Uppercase' , 'analyzed_text' : analyzed}
        djtext = analyzed

    if extraspaceremove == 'on' :
        analyzed = ""
        for index,char in enumerate(djtext) :
            if not (djtext[index] == " " and djtext[index+1] == " "):
                   analyzed += char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremove == 'on' :
        analyzed= ""
        for char in djtext : 
            if char != "\n" and char != "\r" :
                analyzed+=char

        params = {'purpose' : 'New line removed' , 'analyzed_text' : analyzed}

    if removepunc != 'on' and fullcaps != 'on' and extraspaceremove != 'on' and newlineremove != 'on' :
        return HttpResponse("Error")


    return render(request,'analyze.html', params)
