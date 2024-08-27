from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la stringa di connessione al database
DATABASE_URL = "sqlite:///./test.db"  # Cambia con il tuo database

# Crea il motore del database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crea una classe base per i modelli
Base = declarative_base()

# Crea una sessione
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Funzione per ottenere una sessione
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()