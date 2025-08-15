from django.shortcuts import render
from django.http import HttpResponse
import string, unicodedata




# Create your views here.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    jtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(jtext)

    if removepunc == "on":
        def is_punctuation(char):
            return char in string.punctuation or unicodedata.category(char).startswith('P')

        analyzed = ''.join(char for char in jtext if not is_punctuation(char))

        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed,
            'original_text': jtext
        }
        return render(request, 'analyze.html', params)
    
    elif capitalize == 'on':
        analyzed = ''.join(char.upper()for char in jtext )
        params = {
            'purpose': 'Capitalized Text',
            'analyzed_text': analyzed,
            'original_text': jtext
        }
        return render(request, 'analyze.html', params)
    
    elif newlineremove == 'on':
        analyzed = ''.join(char for char in jtext if char != '\n' and char != '\r')
        params = {
            'purpose': 'Newlines Removed',
            'analyzed_text': analyzed,
            'original_text': jtext
        }
        return render(request, 'analyze.html', params)
    
    elif spaceremove == 'on':
        analyzed = "".join(char for char in jtext if char != " ")

        params = {
            'purpose': 'Extra Spaces Removed',
            'analyzed_text': analyzed,
            'original_text': jtext
        }
        return render(request, 'analyze.html', params)

    elif charcount == 'on':
        analyzed = len(jtext)
        params = {
            'purpose': 'Total Characters',
            'analyzed_text': str(analyzed),
            'original_text': jtext
        }
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("Error: Checkbox not selected")
    


