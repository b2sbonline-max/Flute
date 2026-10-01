from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    full_name = Column(String(150))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    tables = relationship("TableRegistry", back_populates="creator")

class TableRegistry(Base):
    __tablename__ = "tbl_registry"
    
    id = Column(Integer, primary_key=True, index=True)
    table_name_en = Column(String(100), unique=True, nullable=False, index=True)
    table_name_he = Column(String(100), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    creator = relationship("User", back_populates="tables")
    fields = relationship("Field", back_populates="table", cascade="all, delete-orphan")

class Field(Base):
    __tablename__ = "tbl_fields"
    
    id = Column(Integer, primary_key=True, index=True)
    table_name_en = Column(String(100), ForeignKey("tbl_registry.table_name_en"), nullable=False)
    field_name_he = Column(String(100), nullable=False)
    field_name_en = Column(String(100), nullable=False)
    field_type = Column(String(20), nullable=False)
    field_position = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    table = relationship("TableRegistry", back_populates="fields")
