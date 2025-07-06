#!/usr/bin/env python
import os
import django

from cs2test.app.service.questions import Questions
from cs2test.app.service.loading import Porcentage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs2test.settings')
from cs2test.app.service.pages import Page
django.setup()

def main():
    loop = True
    while loop:
        options = [] 
        response = Page.initial_page()
        if response.lower() == "n":
            Page.exit_page()
            break
        elif response.lower() == "s":
            loop = False
            get_perfil()
            
            

def get_perfil():
    options = [] 
    
    Page.quiz_page()
    response = Questions.question_one()
    options.append(response)
    print(response)
    Porcentage.porcentage1()
    
    response = Questions.question_two()
    options.append(response)
    print(response)
    Porcentage.porcentage2()
    
    response = Questions.question_three()
    options.append(response)
    print(response)
    Porcentage.porcentage3()
    
    response = Questions.question_four()
    options.append(response)
    print(response)
    Porcentage.porcentage4()
    
    Page.result_page(options)

if __name__ == '__main__':
    main()
