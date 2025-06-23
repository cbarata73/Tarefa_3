import os

def calcular_multa_cidade(velocidade: int) -> None:
    if  velocidade >= 120:
        print('Multa de 320€')
    elif velocidade >= 90:
        print('Multa de 120€')
    elif velocidade > 50:
        print('Multa de 60€')
    else:
        print('Não tem multa a pagar!')

def calcular_multa_estrada(velocidade: int) -> None:
    if velocidade >= 120:
        print('Multa de 120€')
    elif velocidade > 90:
        print('Multa de 60€')
    else:
        print('Não tem multa a pagar!')

def calcular_multa_autoestrada(velocidade: int) -> None:
    if velocidade > 120:
        print('Multa de 60€')
    else:
        print('Não tem multa a pagar!')

def calcular_multa(velocidade: int, local: int) -> None:
    if local == 1:
        calcular_multa_cidade(velocidade)
    elif local == 2:
        calcular_multa_estrada(velocidade)
    else:
        calcular_multa_autoestrada(velocidade)


if __name__ == '__main__':
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            print('Onde circulava o veiculo?')
            print('Escolha uma opção:')
            print('1 - Localidade')
            print('2 - Fora da localidade')
            print('3 - Autoestrada')
            print()
            loc = int(input('Introduza o local: '))

            if loc not in {1, 2, 3}:
                raise ValueError('Introduza um valor válido!')

            print()
            vel = int(input('Introduza a velocidade do veiculo: '))

            calcular_multa(vel, loc)

            if input('Deseja continuar? (s/n) ').lower() == 'n':
                break

        except ValueError:
            print('Introduza um valor válido!')
            print()
            input('Pressione qualquer tecla para continuar...')
