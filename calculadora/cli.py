import msvcrt
from colorama import Fore, Style

# Funções das operações matemáticas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

#limpar a tela do terminal
def clear_screen():
    print("\033c", end="")

def print_menu(options, selected_option):
    clear_screen()
    for i, option in enumerate(options):
        if i == selected_option:
            print(f"{Fore.GREEN}>>> {option}{Style.RESET_ALL}")
        else:
            print(f"    {option}")

def menu():
    options = ["Soma", "Subtração", "multiplicação", "Divisão", "Sair"]
    selected_option = 0

    while True:
        print_menu(options, selected_option)

        key = msvcrt.getch()

        if key == b'\xe0': # tecla especial (setas direcionais)
            key = msvcrt.getch()

            if key == b'H': # Seta para cima
                selected_option = (selected_option - 1) % len(options)
            elif key == b'P': # Seta para baixo
                selected_option = (selected_option + 1) % len(options)
        elif key == b'\r': # tecla enter
            if selected_option == len(options) - 1:
                clear_screen()
                print()
                print(f"{Fore.YELLOW}Calculadora encerrada.{Style.RESET_ALL}")
                print()
                break
            else:
                clear_screen()
                print(f"Opção selecionada: {Fore.RED}{options[selected_option]}{Style.RESET_ALL}\n")

                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                
                if selected_option == 0:
                    resultado = soma(a, b)
                    print()
                    print(f"Resultado: {a} + {b} = {resultado}\n")
                    print()
                    input(f"{Fore.BLUE}Pressione qualquer tecla para continuar...{Style.RESET_ALL}")
                    print()
                    
                elif selected_option == 1:
                    resultado = subtracao(a, b)
                    print()
                    print(f"Resultado: {a} - {b} = {resultado}\n")
                    print()
                    input(f"{Fore.BLUE}Pressione qualquer tecla para continuar...{Style.RESET_ALL}")
                    print()

                elif selected_option == 2:
                    resultado = multiplicacao(a, b)
                    print()
                    print(f"Resultado: {a} * {b} = {resultado}\n")
                    print()
                    input(f"{Fore.BLUE}Pressione qualquer tecla para continuar...{Style.RESET_ALL}")
                    print()

                elif selected_option  == 3:
                    resultado = divisao(a, b)
                    print()
                    print(f"Resultado: {a} / {b} = {resultado}\n")
                    print()
                    input(f"{Fore.BLUE}Pressione qualquer tecla para continuar...{Style.RESET_ALL}")
                    print()




menu()    