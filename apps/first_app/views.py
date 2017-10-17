from django.shortcuts import render, HttpResponse, redirect
# import random                 #another method
# import string                 #another method
from django.utils.crypto import get_random_string 

# Create your views here.

# def random_word(n):
#     return ''.join(random.choice(string.ascii_uppercase) for _ in range(n))
    

def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    return render(request, 'random_word/index.html')





def generate(request):
    request.session ['tries'] += 1
    request.session ['word'] = get_random_string(length=22)
    return redirect('/random_word')  



def reset(request):
    del request.session['tries']        # kicks you out of the current session
    del request.session['word']
    return redirect('/random_word')



# def generate(request):                            #another method
#     request.session ['tries'] += 1
#     request.session ['word'] = random_word(11)
#     return redirect('/random_word')               # redirect to original page.