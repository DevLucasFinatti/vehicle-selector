from cs2test.app.service.pages import Page

class Questions:
    def question_one():
        loop = True
        
        while loop:
            Page.clear_console()
            print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                        @                                     ║
        ║                     (__)    (__) _____/                                      ║
        ║                  /| (oo) _  (oo)/----/_____    *                             ║
        ║        _o\______/_|\_\/_/_|__\/|____|//////== *- *  *                        ║
        ║       /_________   \   00 |   00 |       /== -* * -                          ║
        ║      [_____/^^\_____\_____|_____/^^\_____]     *- * -                        ║
        ║            \__/                 \__/                                         ║
        ║                                                                              ║
        ║      Você gosta de carros que são...                                         ║
        ║                                                                              ║
        ║      1 - 🛻  pra Trabalho 🛻                                                   ║
        ║      2 - 🚗 De Família 🚗                                                    ║
        ║      3 - 🦾 Fortes 🦾                                                        ║
        ║      4 - 🏎️  Velozes 🏎️                                                        ║
        ║      5 - 👑 De Luxo 👑                                                       ║
        ║                                                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
            """)
            response = input(": ")
            
            if response in ['1','2','3','4','5']:
                loop = False
                return response 
            
    def question_two():
        loop = True
        
        while loop:
            Page.clear_console()
            print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║                 .-"''-.  _                                                   ║
        ║               .'       `( \                                                  ║
        ║             @/            ')   ,--,__,-"                                     ║
        ║             /        /      \ /     /   _/                                   ║
        ║           __|           ,   |/         /                                     ║
        ║         .~  `\   / \ ,  |   /                                                ║
        ║       .~      `\    `  /  _/   _/                                            ║
        ║     .~          `\  ~~`__/    /                                              ║
        ║     ~             `--'/                                                      ║
        ║                  /   /    /                                                  ║
        ║                 /  /'    /                                                   ║
        ║                                                                              ║
        ║      Se você fosse criança, qual carro gostaria de ter?                      ║
        ║                                                                              ║
        ║      1 - Batmóvel                                                            ║
        ║      2 - Dodge Charger R/T 1970 (Velozes e Furiosos)                         ║
        ║      3 - Super Maquina                                                       ║
        ║      4 - Delorean (De volta para o futuro)                                   ║
        ║      5 - Mini cooper do johnny english                                       ║
        ║                                                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
            """)
            response = input(": ")
            
            if response in ['1','2','3','4','5']:
                loop = False
                return response 
            
            
            
    def question_three():
        loop = True
        
        while loop:
            Page.clear_console()
            print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║         -           __                                                       ║
        ║       --          ~( @\   \                                                  ║
        ║      ---   _________]_[__/_>________                                         ║
        ║           /  ____ \ <>     |  ____  \                                        ║
        ║          =\_/ __ \_\_______|_/ __ \__D                                       ║
        ║      ________(__)_____________(__)____        Onde vc gosta de dirigir?      ║
        ║                                                                              ║
        ║                                                                              ║
        ║      1 - Estradas de terra e areas rochosas                                  ║
        ║      2 - Estradas de terra e interior                                        ║
        ║      3 - Estradas de viagens longas                                          ║
        ║      4 - Ruas da cidade                                                      ║
        ║      5 - Orla                                                                ║
        ║                                                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
            """)
            response = input(": ")
            
            if response in ['1','2','3','4','5']:
                loop = False
                return response 
            
            
            
    def question_four():
        loop = True
        
        while loop:
            Page.clear_console()
            print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║                  __-------__                                                 ║
        ║                / _---------_ \                                               ║
        ║               / /           \ \                                              ║
        ║               | |           | |                                              ║
        ║               |_|___________|_|                                              ║
        ║           /-\|                 |/-\                                          ║
        ║          | _ |\       0       /| _ |                                         ║
        ║          |(_)| \      !      / |(_)|      E você dirige bem?                 ║
        ║          |___|__\_____!_____/__|___|                                         ║
        ║          [_________|BRAIA|_________]                                         ║
        ║           ||||    ~~~~~~~~     ||||                                          ║
        ║           `--'                 `--'                                          ║
        ║                                                                              ║
        ║                                                                              ║
        ║      1 - Não tenho carteira de habilitação 😥                                ║
        ║      2 - Eu vou devgar por segurança 👵                                      ║
        ║      3 - Sei oq estou fazendo                                                ║
        ║      4 - Sou o próprio speedracer 🏎️                                          ║
        ║      5 - Apredi a dirigir em SP e to ótimo 🫠                                 ║
        ║                                                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
            """)
            response = input(": ")
            
            if response in ['1','2','3','4','5']:
                loop = False
                return response 
            
            
            
            