from django.shortcuts import render

# Create your views here.

def datafit(requests):
    context={
        'nav' : {
            'Home': '/home', 
            'Project':'/project', 
            'Resume':'../static/doc/Resume.pdf',
            },
    }
    return render(requests, 'Data_Fiting.html', context)

def montecarlo(requests):
    context={
        'nav' : {
            'Home': '/home', 
            'Project':'/project', 
            'Resume':'../static/doc/Resume.pdf',
            },
    }
    return render(requests, 'Monte_Carlo.html', context)    

