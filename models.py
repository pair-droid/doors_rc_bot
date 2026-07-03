from sqlalchemy import BigInteger, String, Integer, Column, Text
from database import Base

class ChatSettings(Base):
    __tablename__ = "chat_settings"
    chat_id = Column(BigInteger, primary_key=True)
    
    rank_0_name = Column(String(50), default="Новичок")
    rank_1_name = Column(String(50), default="Активный")
    rank_2_name = Column(String(50), default="Модератор")
    rank_3_name = Column(String(50), default="Старший Модератор")
    rank_4_name = Column(String(50), default="Администратор")
    rank_5_name = Column(String(50), default="Владелец")
    
    rules_text = Column(Text, default="Правила чата пока не установлены.")

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    chat_id = Column(BigInteger, primary_key=True)
    rank = Column(Integer, default=0)
    reputation = Column(Integer, default=0)
    iris_count = Column(Integer, default=0)
    warnings = Column(Integer, default=0)
