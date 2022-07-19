# I have created this website
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Prasad', 'place': 'Pune'}
    return render(request, 'index1.html', params)


def analyze(request):
    # get the text
    djtext = request.POST.get("text", "default")

    # Check the checkbox
    removepunc = request.POST.get("removepunc", "off")
    capitalize = request.POST.get("capitalize", "off")
    newlineremove = request.POST.get("newlineremove", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")

    purpose = ''
    if removepunc == "on":
        analyzed = ''
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        purpose = "Removed Punctuations |"
        djtext = analyzed
    if capitalize == "on":
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper', 'analyzed_text': analyzed}
        purpose += "Changed to Upper |"
        djtext = analyzed
    if newlineremove == "on":
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        purpose += "New Line Remover |"
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char;
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        purpose += "Extra Space Remover |"
        djtext = analyzed
    if removepunc == "on" or capitalize == "on" or newlineremove == "on" or extraspaceremover == "on":
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error Occured.")
