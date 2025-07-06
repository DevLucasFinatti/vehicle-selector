#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs2test.settings')
django.setup()

from cs2test.app.service.questions import Questions
from cs2test.app.service.loading import Porcentage
from cs2test.app.service.vehicle import Services
from cs2test.app.service.pages import Page
perfil = ''

def main():
    loop = True
    while loop:
        response = Page.initial_page()
        if response.lower() == "n":
            Page.exit_page()
            break
        elif response.lower() == "s":
            loop = False
            perfil = get_perfil()
            home(perfil)
            
def home(user_perfil):
    loop = True
    
    while loop:
        task = Page.home_page()

        if task == '1':
            Page.src_brand_name()
            src_text = input(": ")
            src_result = Services.search_vehicle_by_brand_name(src_text)
            Services.form_response(src_result)
        elif task == '2':
            Page.src_page()
            src_text = input(": ")
            src_result = Services.search_vehicle(src_text)
            Services.form_response(src_result)
        elif task == '3':
            Page.src_page_perfil(user_perfil)
            print('Perfil: ',user_perfil)
            src_result = Services.search_vehicle_by_profile(user_perfil)
            Services.form_response(src_result)
        elif task == '5':
            Page.exit_page()
            break
            
def get_perfil():
    options = [] 
    
    Page.quiz_page()
    response = Questions.question_one()
    options.append(response)
    Porcentage.porcentage1()
    
    response = Questions.question_two()
    options.append(response)
    Porcentage.porcentage2()
    
    response = Questions.question_three()
    options.append(response)
    Porcentage.porcentage3()
    
    response = Questions.question_four()
    options.append(response)
    Porcentage.porcentage4()
    
    loop = True
    while loop:
        perfil = Page.result_page(options)
        response = input(": ")
            
        if response.lower() =='s':
            loop = False
            return perfil
        elif response.lower() == 'n':
            Page.exit_page() 
        
    
    

if __name__ == '__main__':
    main()
