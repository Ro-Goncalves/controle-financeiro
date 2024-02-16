from datetime import datetime
from sqlalchemy import (create_engine, MetaData)

engine = create_engine('sqlite:///controle-financeiro.db',
                       echo=False)

metadata = MetaData(bind=engine)