#Primeiro Exercício
#1) Observe o trecho de código abaixo:
#Ao final do processamento, qual será o valor da variável SOMA?

int INDICE = 13, SOMA = 0, K = 0;

while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}

imprimir(SOMA);

K = 13, SOMA = 78 + 13 = 91

#Segundo Exercício

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def sequencia(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

# Número a ser verificado
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if sequencia(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Terceiro Exercício
# 3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, 9

#Cada número é igual ao anterior + 2, formando os números ímpares. Assim, o próximo número é igual a 7 + 2 = 9.

b) 2, 4, 8, 16, 32, 64, 128

#Cada número é igual ao anterior multiplicado por 2. Assim, o próximo número é igual a 64 x 2 = 128.

c) 0, 1, 4, 9, 16, 25, 36, 49

#Cada número é igual ao anterior acrescido de um número ímpar que segue a sequência 1, 3, 5, 7, 9. Realizando a subtração dos dois últimos números, temos que 36 - 25 = 11. Assim, devemos acrescentar 11 + 2 = 13 ao último número, obtendo 36 + 13 = 49.

d) 4, 16, 36, 64, 100

#Cada número é igual ao quadrado dos números pares. Com isso, temos que 64 = 8². Então, o próximo número par é 10, e o seu quadrado é 10² = 100.

e) 1, 1, 2, 3, 5, 8, 13

#Cada número é igual à soma do número atual com o número anterior. Assim, o próximo número é igual a 8 + 5 = 13.

f) 2, 10, 12, 16, 17, 18, 19, 200

#Sequência formada através de todos os números que iniciam com a letra d. Assim, o próximo número em ordem crescente que inicia com a letra d é 200.

#4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
#Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Primeira rodada de testes:

Ligue o primeiro interruptor e o mantenha ligado por alguns minutos.
Depois, desligue o primeiro interruptor e ligue o segundo interruptor.
Segunda rodada de testes:

Entre na sala das lâmpadas.
Agora, observe:

Se uma lâmpada estiver acesa:

O interruptor que você ligou e desligou controla essa lâmpada.
O interruptor que você ligou e deixou ligado controla a segunda lâmpada.
O interruptor que você não tocou controla a terceira lâmpada.
Se todas as lâmpadas estiverem apagadas:

O interruptor que você ligou e desligou controla a terceira lâmpada.
O interruptor que você ligou e deixou ligado controla a primeira lâmpada.
O interruptor que você não tocou controla a segunda lâmpada.
Dessa forma, com apenas duas idas até a sala das lâmpadas, você pode determinar qual interruptor controla cada uma das lâmpadas.

5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(string):
    # Converte a string para uma lista de caracteres
    caracteres = list(string)
    
    # Obtém o comprimento da string
    comprimento = len(caracteres)
    
    # Inverte os caracteres usando um loop
    for i in range(comprimento // 2):
        # Troca os caracteres nas posições i e comprimento - i - 1
        temp = caracteres[i]
        caracteres[i] = caracteres[comprimento - i - 1]
        caracteres[comprimento - i - 1] = temp
    
    # Junta os caracteres novamente em uma string invertida
    string_invertida = ''.join(caracteres)
    return string_invertida

# Exemplo de uso:
string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)