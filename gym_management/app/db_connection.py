from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Sukurkite duomenų bazės variklį (pakeiskite URL pagal savo duomenų bazės konfigūraciją)
engine = create_engine('sqlite:///gym_management.db')

# Sukurkite bazinę klasę, ant kurios bus kuriamos visos lentelės
Base = declarative_base()

# Sukurkite sesijos kūrimo funkciją
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
