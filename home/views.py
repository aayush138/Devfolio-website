from django.shortcuts import render

# Create your views here.

def home(requests):
    context={
        'nav' : {
            'Project': '/project', 
            'Skills':"#skills", 
            'Hobbies':'#hobbies', 
            'Intern':'#intern', 
            'Extra':'#extra', 
            'About':'#about'
            },
    }
    return render(requests,'home.html', context)

def project(requests):
    context={
        'nav' : {
            'Home': '/home', 
            'Resume':'../static/doc/Resume.pdf', 
            'Web-Dev':'#web', 
            'Programming':'#prog', 
            'Data-Analytics':'#data',
            },
    }
    return render(requests, 'project.html', context)    


