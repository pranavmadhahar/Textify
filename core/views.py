from django.shortcuts import render
from django.http import HttpResponse
import string, unicodedata




# Create your views here.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    jtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
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
        analyzed = ''.join(char for char in jtext if char != '\n')
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
    


