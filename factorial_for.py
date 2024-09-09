import random

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

def somatorio_vetores(vetor):
    somatorio = 0
    for i in range(len(vetor)):
        somatorio += vetor[i]

    return somatorio

def producao_vetor_automatico(inicio_range, final_range, tamanho_vetor):
    vetor_final = []
    for i in range(tamanho_vetor):
        prox_digito = random.randint(inicio_range, final_range)
        vetor_final.append(prox_digito)
        
    return vetor_final


def calcular_resultado_exponencial(numero, expoente):
    resultado_exponencial = 1
    for i in range(expoente):
        resultado_exponencial *= numero
    
    return resultado_exponencial

def calcular_produto_multiplicação(multiplicando, multiplicador):
    produto = 0
    for i in range(multiplicador):
        produto += multiplicando
    
    return produto

def calcular_sequencia_simples():
    pass

def mostrar_fibonacci(tamanho_sequencia):
    x1 = 1
    x2 = 1
    variavel_auxiliadora = 0
    for i in range(tamanho_sequencia):
        print(x1)
        variavel_auxiliadora = x2
        x2 = x2+x1
        x1 = variavel_auxiliadora
        
def calcular_fatorial(numero):
    resultado = 1
    for i in range(numero):
        resultado *= numero
        numero-=1
        
    return resultado

def mostrar_menu():
    menu = """
    \t=========================================================
    \t1 - calcular fatorial de um número N
    \t2 - mostrar uma sequência de fibonacci com comprimento C
    \t3 - mostrar sequencia simples de A até B
    \t4 - calcular um produto através de somas sucessivas
    \t5 - calcular o exponencial de um número N
    \t6 - Somatório de um vetor com N elementos aleatórios
    \t7 - Contar as Vogais e Consoantes de uma frase
    \t=========================================================
    """
    print(menu)

def main():
    mostrar_menu()
    entrada = int(input("\t>>>"))
    
    while(entrada != 0):
        if entrada == 1:
            numero_N = int(input("Insira um número N: "))
            fatorial = calcular_fatorial(numero_N)
            print(fatorial)
        elif entrada == 2:
            mostrar_fibonacci(int(input("Insira o comprimento da sequência de fibonacci desejada: ")))
        elif entrada == 3:
            inicio_sequencia = int(input("Insira o começo da sua sequência: "))
            final_sequencia = int(input("Insira o final da sua sequência: "))
            sequencia_simples = calcular_sequencia_simples(inicio_sequencia, final_sequencia)
            print(sequencia_simples)
        elif entrada == 4:
            multiplicando = int(input("Insira um número para ser multiplicado: "))
            multiplicador = int(input("Insira um número para ser o multiplicador: "))
            produto_multiplicaçao = calcular_produto_multiplicação(multiplicando, multiplicador)
            print(produto_multiplicaçao)
        elif entrada == 5:
            numero = int(input("Insira um número para ser elevado: "))
            expoente = int(input("Insira um número para ser o expoente da operação: "))
            resultado_exponenciacao = calcular_resultado_exponencial(numero, expoente)
            print(resultado_exponenciacao)
        elif entrada == 6:
            tamanho_vetor = int(input("Insira o tamanho do vetor desejado: "))
            valor_minimo = int(input("Insira o valor mínimo permitido no vetor: "))
            valor_maximo = int(input("Insira o valor máximo permitido no vetor: "))
            vetor = producao_vetor_automatico(valor_minimo, valor_maximo, tamanho_vetor)
            print(vetor)
            somatorio_vetor = somatorio_vetores(vetor)
            print(somatorio_vetor)
        elif entrada == 7:
            frase = input("Insira uma frase desejada: ")
            qtd_vogais = contar_vogais(frase)
            qtd_consoates = contar_consoantes(frase)
            print(f"A quantidade de vogais na frase é de: {qtd_vogais} e consoantes: {qtd_consoates}")
        mostrar_menu()
        entrada = int(input("\t>>>"))
        
main()