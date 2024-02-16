from domain.core.model.SalvarCartaoCreditoCommand import SalvarCartaoCreditoCommand
from infrastructure.CartaoCreditoDataBaseAdapter import CartaoCreditoDatabaseAdapter

salvar_cartao_credito_command = SalvarCartaoCreditoCommand("Nome Cartão Dois", "Bandeira Cartão", 1000.00)
adapter = CartaoCreditoDatabaseAdapter()

# adapter.salvar(salvar_cartao_credito_command)
cartoes = adapter.select_all()
for cartao in cartoes:
    print(cartao.NM_Cartao)
