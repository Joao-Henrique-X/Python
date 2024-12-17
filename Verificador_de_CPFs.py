soma1 = 0
soma2 = 0 
y = 10 
y2 = 11

while True:
    # Verificação do CPF se há Ponto ou Traço e realizando a eliminação deles, se possui 11 dígitos ou letras
    cpf_original = input("Digite seu CPF para verificação ")
    cpf_limpo = "".join(x for x in cpf_original if x.isdigit())

    if any(x.isalpha() for x in cpf_original):
        print("O CPF digitado contém letras, verifique o CPF inserido.")
        continue
    
    if len(cpf_limpo) != 11:
        print("O CPF deve conter 11 dígitos!")
    
    else:
        cpf_base = cpf_limpo[:9]
        break

# Cálculo do Primeiro Dígito
for x in cpf_base:
    x = int(x)
    soma1 += x * y
    y -= 1

digito1 = soma1 % 11

if digito1 < 2:
    cpf_base += '0'
else:
    cpf_base += str(11 - digito1)

    


# Cálculo do Segundo Dígito

for x in cpf_base:
    x = int(x)
    soma2 += x * y2
    y2 -= 1

digito2 = soma2 % 11

if digito2 < 2:
    cpf_base += '0'
else:
    cpf_base += str(11 - digito2)


#Finalização

if (cpf_base == cpf_limpo):
    print("CPF Válido!")
else:
    print("CPF Inválido!")

