def duplicador(num):
    num_duplicado = num * 2
    return (f"Seu número duplicado é: {num_duplicado}")

def triplicador(num):
    num_duplicado = num * 3
    return (f"Seu número triplicado é: {num_duplicado}")

def quadruplicador(num):
    num_duplicado = num * 4
    return (f"Seu número quadruplicado é: {num_duplicado}")


num = int(input("Digite um número para multiplicar em 2x 3x e 4x: "))

print (duplicador(num))
print (triplicador(num))
print (quadruplicador(num))