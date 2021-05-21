from django.shortcuts import redirect, render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        characters = 'abcdefghijklmnoprstuwvxyz'
        numbers = '1234567890'
        special = '!@#$%&'

        if request.POST.get('numbers'):
            characters += numbers
  
        if request.POST.get('special'):
            characters += special      
        
        length = int(request.POST.get('length'))
        domain = request.POST.get('domain')

        preMail = ''

        for _ in range(length):
            preMail += random.choice(characters)

        mail = preMail + domain


        return render(request, 'result.html', {'mail': mail})
    else:
        return redirect('generator:home')

def about(request):
    return render(request, 'about.html')


