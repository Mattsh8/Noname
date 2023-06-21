#!/usr/bin/python3

import random
import string

def gerar_senha(tamanho, letras_maiusculas=True, letras_minusculas=True, numeros=True, caracteres_especiais=True):
    caracteres = ''
    if letras_maiusculas:
        caracteres += string.ascii_uppercase
    if letras_minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if caracteres_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def validar_tamanho(tamanho):
    try:
        tamanho = int(tamanho)
        if tamanho <= 0:
            print("Tamanho inválido. Insira um valor positivo maior que zero.")
            return False
        return True
    except ValueError:
        print("Entrada inválida. Insira um número inteiro válido.")
        return False

def main():
    tamanho = input("Digite o tamanho da senha desejada: ")
    while not validar_tamanho(tamanho):
        tamanho = input("Digite o tamanho da senha desejada: ")

    letras_maiusculas = input("Incluir letras maiúsculas? (S/N): ").upper() == "S"
    letras_minusculas = input("Incluir letras minúsculas? (S/N): ").upper() == "S"
    numeros = input("Incluir números? (S/N): ").upper() == "S"
    caracteres_especiais = input("Incluir caracteres especiais? (S/N): ").upper() == "S"

    senha = gerar_senha(int(tamanho), letras_maiusculas, letras_minusculas, numeros, caracteres_especiais)
    print("Senha gerada:", senha)

if __name__ == "__main__":
    main()



