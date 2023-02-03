from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def textInput(request):
    # return HttpResponse("Its Home Page")
    return render(request, "index.html")


def about(request):
    # return HttpResponse("Its About Page")
    text = request.POST.get('text', 'default')  # Fetching data from HTML Page
    removePunc = request.POST.get('removepunc', 'off')
    upperCase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')

    analyzed_text = ''

    # REMOVING PUNCTUATIONS
    if removePunc == 'on':
        punctuations = ''':;()-[]{}!'"/\,.<>?@#$%^&*_`~'''
        for char in text:
            if char not in punctuations:
                analyzed_text += char
            params = {"purpose": "Removed Punctuation",
                      "analyzed_text": analyzed_text}

    # TEXT TO UPPERCASE
    if upperCase == 'on':
        if analyzed_text == '':
            analyzed_text = text.upper()
            params = {"purpose": "Removed Punctuation",
                      "analyzed_text": analyzed_text}

        else:
            analyzed_text = analyzed_text.upper()
            params = {"purpose": "Removed Punctuation",
                      "analyzed_text": analyzed_text}

    # TEXT TO LOWERCASE
    if lowercase == 'on':
        if analyzed_text == '':
            analyzed_text = text.lower()
            params = {"purpose": "Removed Punctuation",
                      "analyzed_text": analyzed_text}

        else:
            analyzed_text = analyzed_text.lower()
            params = {"purpose": "Removed Punctuation",
                      "analyzed_text": analyzed_text}

    else:
        analyzed_text = text

    return render(request, "about.html", params)
