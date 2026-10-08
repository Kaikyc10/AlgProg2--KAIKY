#Sistema de pedidos
def calcular_total(*precos):

    """
    Recebe uma quantidade variável de preços 
    e retorna a soma.

    O parâmetro Preçoes será uma tupla.
    """

    total = 0
    for preco in precos:
        total+= preco
    
    return total

def aplicar_desconto(valor, percentual=0):
    """
    Aplica um desconto percentual sobre um valor.
    """

    if (percentual < 0 or percentual > 100):
        print("Valor % informado inválido")
        return valor
    
    desconto = valor * percentual/100
    return valor - desconto

def exibir_dados_cliente(**dados):
    """
    Recebe dados nomeados do cliente. 

    O parâmetro dados é um dicionário.

    """

    print("\nDados do Cliente ============")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

def registrar_pedido(numero, *produtos, desconto=0, **cliente):
    """
    Registra e exibe um pedido completo.

    numero: parâmetro obrigatório;
    *produtos: recebe vários produtos;
    desconto: parâmetro opcional;
    **cliente: recebe os dados do cliente.
    """

    print("="*55)
    print(f"Pedido n.º {numero}")

    if(len(produtos)==0):
        print("Nenhum produto foi informado")
        return
    
    precos=[]
    print("\nProdutos")
    for nome, preco in produtos:
        print(f"{nome:<25} R$ {preco:>8.2f}")
        precos.append(preco)

    #A lista é desempacotada na chamada da função
    subtotal = calcular_total(*precos)

    total = aplicar_desconto(valor=subtotal, percentual=desconto)

    valor_desconto = subtotal - total

    print("-"*55)
    print(f"{'Subtotal:':<25} R$ {subtotal:>8.2f}")
    print(f"{'Desconto:':<25} R$ {valor_desconto:>8.2f}")
    print(f"{'Total':<25} R$ {total:>8.2f}")

    exibir_dados_cliente(**cliente)
    print("\nPedido registrado com sucesso!!")
    print("="*55)


#dados do programa

lista_produtos = [
    ("Teclado Mecânico",250.00),
    ("Mouse sem fio", 120.00),
    ("Mousepad",475.25),
    ("Cabo USB", 30.00)
]

dados_cliente = {
    "nome": "Mariana Souza",
    "email": "marian@facamp.com",
    "cidade": "Campinas",
    "pagamento": "PIX"
 }

registrar_pedido(
    1001,
    *lista_produtos,
    desconto=10,
    **dados_cliente
)

