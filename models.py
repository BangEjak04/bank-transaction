from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Cheque(db.Model):
    __tablename__ = 'cheques'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cheque_type: Mapped[str] = mapped_column(String(50), nullable=False) # e.g., "Cek", "Giro"
    cheque_code: Mapped[str] = mapped_column(String(50), nullable=False) # e.g., "TR", "TP"
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False) # e.g., "2023-10-01"
    start_number: Mapped[str] = mapped_column(String(50), nullable=False) # e.g., "000100"
    end_number: Mapped[str] = mapped_column(String(50), nullable=False) # e.g., "000500"
    giro_number: Mapped[str] = mapped_column(String(50), nullable=True)
    giro_name: Mapped[str] = mapped_column(String(50), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False) # e.g., "Belum Dikeluarkan", "Sudah Dikeluarkan"
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Cheque {self.cheque_code} ({self.cheque_type})>"
    
    def __init__(self, cheque_type, cheque_code, date, start_number, end_number, giro_number=None, giro_name=None, status="Belum Dikeluarkan"):
        self.cheque_code = cheque_code
        self.cheque_type = cheque_type
        self.date = date
        self.start_number = start_number
        self.end_number = end_number
        self.giro_number = giro_number
        self.giro_name = giro_name
        self.status = status
