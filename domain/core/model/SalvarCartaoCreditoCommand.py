
class SalvarCartaoCreditoCommand:
    def __init__(self, nome_cartao, bandeira, limite_disponivel):
        self.nome_cartao = nome_cartao
        self.bandeira = bandeira
        self.limite_disponivel = limite_disponivel