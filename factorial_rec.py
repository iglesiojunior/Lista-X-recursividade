import random
import os

def limpar_console():
    input("\tPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_eh_letra(letra):
    if ord(letra) > 64 and ord(letra) < 91 or ord(letra) > 96 and ord(letra) < 123:
        return True
    return False

def converter_letra_minuscula(letra):
    if verificar_eh_letra(letra):
        if ord(letra) > 64 and ord(letra) < 91:
            letra_minuscula = chr(ord(letra)+32)
            return letra_minuscula
        else:
            return letra
    else:
        return letra

def contar_consoantes(frase):
    qtd_consoantes = 0
    for i in range(len(frase)):
        letra_formatada = converter_letra_minuscula(frase[i])
        if verificar_eh_letra(frase[i]):
            if letra_formatada not in ["a", "e", "i", "o", "u"]:
                qtd_consoantes += 1
                
    return qtd_consoantes

def contar_vogais(frase):
    qtd_vogais = 0
    for i in range(len(frase)):
        letra_formatada = converter_letra_minuscula(frase[i])
        if verificar_eh_letra(frase[i]):
            if letra_formatada in ["a", "e", "i", "o", "u"]:
                qtd_vogais += 1

    return qtd_vogais

def somatorio_vetores(vetor, i = 0):
    if i < len(vetor):
        return vetor[i]+somatorio_vetores(vetor, i+1)
    else:
        return 0 

def producao_vetor_automatico(inicio_range, final_range, tamanho_vetor):
    vetor_final = []
    for i in range(tamanho_vetor):
        prox_digito = random.randint(inicio_range, final_range)
        vetor_final.append(prox_digito)
        
    return vetor_final


def calcular_resultado_exponencial(numero, expoente):
    if expoente >= 1:
        return numero*calcular_resultado_exponencial(numero, expoente-1)
    else:
        return 1

def calcular_produto_multiplicação(multiplicando, multiplicador):
    if multiplicador >= 1:
        return multiplicando + calcular_produto_multiplicação(multiplicando, multiplicador-1)
    else:
        return 0

def calcular_sequencia_simples():
    pass

def mostrar_fibonacci(tamanho_sequencia, x1 = 1, x2 = 1):
    if tamanho_sequencia > 1:
        variavel_auxiliadora = 0
        print(f"\t{x1}")
        variavel_auxiliadora = x2
        x2 = x2+x1
        x1 = variavel_auxiliadora
        return mostrar_fibonacci(tamanho_sequencia-1, x1, x2)
    
def calcular_fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero *calcular_fatorial(numero-1)

def mostrar_menu():
    menu = """
    \t=========================================================
    \t1 - Calcular fatorial de um número N
    \t2 - Mostrar uma sequência de fibonacci com comprimento C
    \t3 - Mostrar sequencia simples de A até B
    \t4 - Calcular um produto através de somas sucessivas
    \t5 - Calcular o exponencial de um número N
    \t6 - Somatório de um vetor com N elementos aleatórios
    \t7 - Contar as Vogais e Consoantes de uma frase
    \t
    \t0 - Encerrar o programa
    \t=========================================================
    """
    print(menu)

def main():
    mostrar_menu()
    entrada = int(input("\t>>>"))
    
    while(entrada):
        if entrada == 1:
            print("\t=============================================================")
            numero_N = int(input("\tInsira um número N: "))
            fatorial = calcular_fatorial(numero_N)
            print(f"\tfatorial de {numero_N} é igual a: {fatorial}")
            print("\t=============================================================")
        elif entrada == 2:
            print("\t=============================================================")
            mostrar_fibonacci(int(input("\tInsira o comprimento da sequência de fibonacci desejada: ")))
            print("\t=============================================================")
        elif entrada == 3:
            print("\t=============================================================")
            inicio_sequencia = int(input("\tInsira o começo da sua sequência: "))
            final_sequencia = int(input("\tInsira o final da sua sequência: "))
            sequencia_simples = calcular_sequencia_simples(inicio_sequencia, final_sequencia)
            print(f"{sequencia_simples}")
            print("\t=============================================================")
        elif entrada == 4:
            print("\t=============================================================")
            multiplicando = int(input("\tInsira um número para ser multiplicado: "))
            multiplicador = int(input("\tInsira um número para ser o multiplicador: "))
            produto_multiplicaçao = calcular_produto_multiplicação(multiplicando, multiplicador)
            print(f"\t{produto_multiplicaçao}")
            print("\t=============================================================")
        elif entrada == 5:
            print("\t=============================================================")
            numero = int(input("\tInsira um número para ser elevado: "))
            expoente = int(input("\tInsira um número para ser o expoente da operação: "))
            resultado_exponenciacao = calcular_resultado_exponencial(numero, expoente)
            print(f"\t{resultado_exponenciacao}")
            print("\t=============================================================")
        elif entrada == 6:
            print("\t=============================================================")
            tamanho_vetor = int(input("\tInsira o tamanho do vetor desejado: "))
            valor_minimo = int(input("\tInsira o valor mínimo permitido no vetor: "))
            valor_maximo = int(input("\tInsira o valor máximo permitido no vetor: "))
            vetor = producao_vetor_automatico(valor_minimo, valor_maximo, tamanho_vetor)
            print(f"\tvetor produzido: {vetor}")
            somatorio_vetor = somatorio_vetores(vetor)
            print(f"\tsomatório do vetor: {somatorio_vetor}")
            print("\t=============================================================")
        elif entrada == 7:
            print("\t=============================================================")
            frase = input("\tInsira uma frase desejada: ")
            qtd_vogais = contar_vogais(frase)
            qtd_consoates = contar_consoantes(frase)
            print(f"\tA quantidade de vogais na frase é de: {qtd_vogais} e consoantes: {qtd_consoates}")
            print("\t=============================================================")
        limpar_console()
        mostrar_menu()
        entrada = int(input("\t>>>"))
        
main()