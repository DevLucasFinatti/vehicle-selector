import os
import time

class Page:
    def wait(sec):
        time.sleep(sec)
    
    def clear_console():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
    def exit_page():
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║    █▀█ █▄█ █▀█ █▀█ █▀█ █▀█ █▄█ █▄█ █▄█ █▀█                                   ║
        ║    █▀▄ ░█░ █▄█ █▄█ █▄█ █▀▄ ░█░ ░█░ ░█░ █▄█                                   ║
        ║    Encerrado                                                                 ║             
        ║                                                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        
    def initial_page():
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║    █░█ █▀█ █░█ █▄█ █▀█ █▄█    █░█ █▀█ █▀█ █░█ █▄█ █░█ █▀█ █▄█ █▀█            ║
        ║    █▀█ █▄█ █▄█ ░█░ █▄█ ░█░    █▀█ █▄█ █▄█ █▄█ █░█ █▄█ █▄█ █░█ █▄█            ║                                  
        ║    Anti                       Bucha                                          ║
        ║                                                                              ║
        ║    Quer encontrar um carro de qualidade? (S/N)                               ║
        ║                                                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)

        return input(": ")

    def quiz_page():
        from cs2test.app.service.loading import Porcentage
        Page.clear_console()
        Porcentage.loading_page()
        Porcentage.loading_page()
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║    Já sei, vamos fazer um quiz...                                            ║
        ║                                                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        Page.wait(2)
        
    def result_page(options: list[str]):
        values = list(map(int, options))
        total = sum(values)

        if 4 <= total <= 8:
            Page.perfil_result1()
            return 'conan'
        elif 9 <= total <= 12:
            Page.perfil_result2()
            return 'paidefamilia'
        elif 13 <= total <= 16:
            Page.perfil_result3()
            return 'garotao'
        elif 17 <= total <= 20:
            Page.perfil_result4()
            return 'fino'
        else:
            return "Perfil fora da faixa esperada"


    def perfil_result1():
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║                          ___ ___  _ __   __ _ _ __                           ║
        ║                         / __/ _ \| '_ \ / _` | '_ \                          ║
        ║                        | (_| (_) | | | | (_| | | | |                         ║
        ║                         \___\___/|_| |_|\__,_|_| |_|                         ║
        ║                                                                              ║
        ║    🚜 Conan — "Estrada é opcional, testosterona não."                        ║
        ║                                                                              ║
        ║    Você é o Conan das estradas: dirige como se cada ida ao mercado           ║
        ║    fosse uma expedição na Amazônia. Lama, buraco, pedra?                     ║
        ║    Tudo isso é massagem nos pneus.                                           ║
        ║    Escova o dente com cerveja,                                               ║
        ║    troca o óleo com a mão                                                    ║
        ║    e usa o carro como extensão da alma bruta.                                ║
        ║    Seu porta-malas já viu mais ferramentas que uma oficina mecânica.         ║
        ║                                                                              ║
        ║    “Ar condicionado? Tenho vento na cara e grito na alma.”                   ║
        ║                                                                              ║
        ║                                                                              ║
        ║  Prosseguir: digite 'S'                                                      ║
        ║  Fechar: digite 'N'                                                          ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)


    def perfil_result2():
        Page.clear_console()
        print(r'''
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║                        ,=====,                                               ║
        ║                        /_   _\                                               ║
        ║                        |a` `a|                                               ║
        ║                        |  u  |                                               ║
        ║                        \  =  /                                               ║
        ║                        |\___/|                                               ║
        ║               ___ ____/:     :\____ ___                                      ║
        ║             .'   `.-===-\   /-===-.`   '.                                    ║
        ║            /      .-"""""- -"""""-.      \                                   ║
        ║           /'             =:=             '\                                  ║
        ║         .'  ' .:    o   -=:=-   o    :. '  `.                                ║
        ║         (.'   /'. '-.....-'-.....-' .'\   '.)                                ║
        ║                                                                              ║
        ║       👨‍👩‍👧‍👦 Pai de Família                                                ║
        ║       "Modo passeio ativado com fralda na mochila."                          ║
        ║                                                                              ║
        ║       Você é o mestre da estrada pavimentada e da Kombi imaginária.          ║
        ║       Vai do supermercado pro interior com o Waze na alma                    ║
        ║       e o porta-malas cheio de compras, brinquedos                           ║
        ║       e “só mais uma parada rápida”.                                         ║
        ║       Conhece todos os atalhos e acha vaga até em shopping lotado.           ║ 
        ║       Se o carro falar “cinto de segurança”,                                 ║
        ║       você já respondeu “tá no banco de trás!”.                              ║
        ║                                                                              ║
        ║       “O carro é meu, mas o banco de trás é do caos.”                        ║
        ║                                                                              ║
        ║  Prosseguir: digite 'S'                                                      ║
        ║  Fechar: digite 'N'                                                          ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
    ''')


    def perfil_result3():
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║        😎 Garotão — "Meu carro, minhas regras (e 3 parcelas atrasadas)."     ║          
        ║             ____                                                             ║
        ║            /___/\_                                        __                 ║
        ║           _\   \/_/\__                                  _|  |_               ║
        ║         __\       \/_/\                               _|      |_             ║
        ║         \   __    __ \ \                             |  _    _  |            ║
        ║        __\  \_\   \_\ \ \   __                       | |_|  |_| |            ║
        ║       /_/\\   __   __  \ \_/_/\                   _  |  _    _  |  _         ║
        ║       \_\/_\__\/\__\/\__\/_\_\/                  |_|_|_| |__| |_|_|_|        ║
        ║          \_\/_/\       /_\_\/                      |_|_        _|_|          ║
        ║            \_\/       \_\/                          |_|      |_|             ║
        ║                                                                              ║
        ║        Primeiro carro, primeiro amor. Você é o Garotão das quatro rodas:     ║           
        ║        lava o carro na chuva, troca o escapamento por estilo                 ║
        ║        e jura que o som alto melhora o desempenho.                           ║
        ║        Já fez rolê só pra abastecer, já pediu Pix pra trocar o óleo          ║      
        ║        e acha que “suspensão” é um estado de espírito.                       ║
        ║                                                                              ║
        ║        “Não sei pra onde tô indo, mas vou de carro.”                         ║
        ║                                                                              ║
        ║  Prosseguir: digite 'S'                                                      ║
        ║  Fechar: digite 'N'                                                          ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        
    def perfil_result4():
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║
        ║  💼 Fino — "0 a 100 em 3 segundos, ostentação em tempo integral."            ║
        ║                                                                              ║  
        ║                    ____----------- _____                                     ║
        ║      \~~~~~~~~~~/~_--~~~------~~~~~     \                                    ║
        ║       `---`\  _-~      |                   \                                 ║
        ║         _-~  <_         |                     \[]                            ║
        ║       / ___     ~~--[""] |      ________-------'_                            ║ 
        ║      > /~` \    |-.   `\~~.~~~~~                _ ~ - _                      ║
        ║       ~|  ||\%  |       |    ~  ._                ~ _   ~ ._                 ║    
        ║         `_//|_%  \      |          ~  .              ~-_   /\                ║     
        ║                `--__     |    _-____  /\               ~-_ \/.               ║      
        ║                     ~--_ /  ,/ -~-_ \ \/          _______---~/               ║      
        ║                         ~~-/._<   \ \`~~~~~~~~~~~~~     ##--~/               ║      
        ║                               \    ) |`------##---~~~~-~  ) )                ║     
        ║                                ~-_/_/                  ~~ ~~                 ║            
        ║                                                                              ║  
        ║                                                                              ║  
        ║  Você é o Rei do couro perfumado. Seu carro brilha mais que sua carreira,    ║
        ║  e se tiver que escolher entre manchar o tapete ou deixar o amigo na chuva...║
        ║  bom, o Uber tá aí.                                                          ║
        ║  Curte teto solar, massageador de banco,                                     ║
        ║  e acha que IPVA é uma espécie de doação nobre pro governo.                  ║
        ║                                                                              ║
        ║  “Gasto mais com a lavagem do carro do que com terapia.”                     ║
        ║                                                                              ║
        ║                                                                              ║
        ║  Prosseguir: digite 'S'                                                      ║
        ║  Fechar: digite 'N'                                                          ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        
    def home_page():
        loop = True
        
        while loop == True:
            Page.clear_console()
            print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║ 
        ║       █▀█ █▄█ █▀█      Digite o numero par prosseguir:                       ║
        ║       █▀▄ ░█░ █▄█                                                            ║
        ║       Home             Buscar veiculos por:            Comandos:             ║
        ║                             1 - Nome/Marca                  5 - sair         ║ 
        ║                             2 - Geral                                        ║ 
        ║                                                                              ║ 
        ╚══════════════════════════════════════════════════════════════════════════════╝
            """)
            response = input(": ")
            
            if response in ['1','2','3','5']:
                loop = False
                return response 
        
    def src_brand_name():
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║ 
        ║                                                                              ║ 
        ║               E vamos pra busca 😎                                           ║ 
        ║               Digite a marca ou nome do possante aqui em baixo               ║ 
        ║                                       |                                      ║ 
        ║                                       |                                      ║ 
        ║                                       V                                      ║ 
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)
    
    def src_page():
        Page.clear_console()
        print(r"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║ 
        ║                                                                              ║ 
        ║               E vamos pra busca 😎                                           ║ 
        ║               Busque seu possante aqui, você pode pesquisar por:             ║ 
        ║               Marca, Nome, Valor, Ano de fabrição e etc...                   ║ 
        ║                                       |                                      ║ 
        ║                                       |                                      ║ 
        ║                                       V                                      ║ 
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        
    def src_page_perfil(perfil):
        Page.clear_console()
        print(f"""
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                                                                              ║ 
        ║                                                                              ║ 
        ║               E vamos pra busca 😎                                           ║ 
        ║               Busque seu possante aqui, com base no seu perfil               ║ 
        ║                                       |                                      ║ 
        ║                                       |                                      ║ 
        ║                                       V                                      ║ 
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """)