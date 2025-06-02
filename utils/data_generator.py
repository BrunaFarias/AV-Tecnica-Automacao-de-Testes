import random
import string

def generate_random_string(tamanho=10):
    """
    Gera uma string aleatória de tamanho especificado, composta por letras minúsculas e dígitos.
    """
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(tamanho))

def generate_random_email(domain="qa.com"):
    """
    Gera um email aleatório com o domínio.
    """
    return f"teste.{generate_random_string(8)}@{domain}"

def generate_random_user():
     """Gera dados de um usuário aleatório."""
     return {
        "nome": f"Usuário Teste {generate_random_string(5)}",
        "email": generate_random_email(),
        "senha": "senha" + generate_random_string(4)
    }

def generate_random_product():
     return {
         "nome": f"Produto Teste {generate_random_string(5)}",
         "preco": random.randint(10, 1000),
         "descricao": f"Descrição do produto {generate_random_string(15)}",
         "quantidade": random.randint(1, 50)
     }