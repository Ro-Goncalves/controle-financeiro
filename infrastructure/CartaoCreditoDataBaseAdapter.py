from db.models import Session, CartaoCredito

class CartaoCreditoDatabaseAdapter:
    def __init__(self) -> None:
        pass        

    def salvar(self, salvar_cartao_credito_command):
        with Session() as session:            
            cartao_credito = CartaoCredito()
            cartao_credito.NM_Cartao = salvar_cartao_credito_command.nome_cartao
            cartao_credito.Bandeira = salvar_cartao_credito_command.bandeira
            cartao_credito.Limite_Disponivel = salvar_cartao_credito_command.limite_disponivel
            
            session.add(cartao_credito)            
            session.commit()

    def select_all(self):
        with Session() as session:
            return session.query(CartaoCredito).all()
            

            