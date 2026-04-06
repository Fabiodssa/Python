import random

def gerar_cpf():
    # Gera os 9 primeiros dígitos aleatórios
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Cálculo do primeiro dígito verificador
    soma = sum(a * b for a, b in zip(cpf, range(10, 1, -1)))
    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 < 10 else 0
    cpf.append(digito_1)

    # Cálculo do segundo dígito verificador
    soma = sum(a * b for a, b in zip(cpf, range(11, 1, -1)))
    digito_2 = (soma * 10) % 11
    digito_2 = digito_2 if digito_2 < 10 else 0
    cpf.append(digito_2)

    # Formata o CPF como string: XXX.XXX.XXX-XX
    cpf_str = "".join(map(str, cpf))
    return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

# Exemplo de uso
print(f"CPF Gerado: {gerar_cpf()}")