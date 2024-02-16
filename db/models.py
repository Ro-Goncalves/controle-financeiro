from sqlalchemy import Column, Integer, String, Numeric, DATE, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Crie o engine do SQLAlchemy
engine = create_engine('sqlite:///db/controle-financeiro.db')

# Crie uma sessão do banco de dados
Session = sessionmaker(bind=engine)

Base = declarative_base()

class CartaoCredito(Base):
    __tablename__ = 'cartao_credito'

    ID_Cartao = Column(Integer, primary_key=True)
    NM_Cartao = Column(String(50), nullable=False)
    Bandeira = Column(String(50), nullable=False)
    Limite_Disponivel = Column(Numeric(10, 2), nullable=False)
    Lancamentos = relationship("Lancamentos", back_populates="Cartao")

class Lancamentos(Base):
    __tablename__ = 'lancamento'

    ID_Lancamento = Column(Integer, primary_key=True)
    ID_Cartao = Column(Integer, ForeignKey('cartao_credito.ID_Cartao'))
    NM_Local_Compra = Column(String(50), nullable=False)
    TP_Compra = Column(String(15), nullable=False) #-> Parcelado, A Vista, Recorrente
    TP_Produto = Column(String(20), nullable=False) #-> Mercado, Eletronico, Livro, Jogo
    VL_Compra = Column(Numeric(10,2), nullable=False)
    NO_Parcela_Atual = Column(Integer, nullable=False)
    NO_Parcela_Final = Column(Integer, nullable=False)
    DT_Compra = Column(DATE, nullable=False, default=func.now())
    Cartao = relationship("CartaoCredito", back_populates="Lancamentos")