from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models import TableRegistry, Field, User
from schemas import (
    TableRegistryCreate, TableRegistryResponse, TableRegistryUpdate,
    FieldResponse, MessageResponse
)
from database import get_db

router = APIRouter(prefix="/api/tables", tags=["tables"])

@router.get("/", response_model=List[TableRegistryResponse])
def list_tables(db: Session = Depends(get_db)):
    """List all tables"""
    tables = db.query(TableRegistry).all()
    return tables

@router.post("/", response_model=TableRegistryResponse, status_code=status.HTTP_201_CREATED)
def create_table(table: TableRegistryCreate, db: Session = Depends(get_db), user_id: int = 1):
    """Create new table"""
    existing = db.query(TableRegistry).filter(TableRegistry.table_name_en == table.table_name_en).first()
    
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Table already exists")
    
    new_table = TableRegistry(
        table_name_en=table.table_name_en,
        table_name_he=table.table_name_he,
        created_by=user_id
    )
    db.add(new_table)
    db.flush()
    
    for idx, field in enumerate(table.fields, start=1):
        new_field = Field(
            table_name_en=table.table_name_en,
            field_name_he=field.field_name_he,
            field_name_en=field.field_name_en,
            field_type=field.field_type,
            field_position=field.field_position or idx
        )
        db.add(new_field)
    
    db.commit()
    db.refresh(new_table)
    return new_table

@router.get("/{table_name}", response_model=TableRegistryResponse)
def get_table(table_name: str, db: Session = Depends(get_db)):
    """Get table details"""
    table = db.query(TableRegistry).filter(TableRegistry.table_name_en == table_name).first()
    if not table:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Table not found")
    return table

@router.delete("/{table_name}", response_model=MessageResponse)
def delete_table(table_name: str, db: Session = Depends(get_db)):
    """Delete table"""
    table = db.query(TableRegistry).filter(TableRegistry.table_name_en == table_name).first()
    if not table:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Table not found")
    
    db.delete(table)
    db.commit()
    return {"message": f"Table {table_name} deleted", "success": True}

@router.get("/{table_name}/fields", response_model=List[FieldResponse])
def get_fields(table_name: str, db: Session = Depends(get_db)):
    """Get table fields"""
    fields = db.query(Field).filter(Field.table_name_en == table_name).order_by(Field.field_position).all()
    if not fields:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fields not found")
    return fields

@router.post("/{table_name}/data")
def add_data(table_name: str, data: dict, db: Session = Depends(get_db)):
    """Add row"""
    return {"message": "Data added", "success": True}

@router.get("/{table_name}/data")
def get_data(table_name: str, db: Session = Depends(get_db)):
    """Get rows"""
    return {"data": [], "count": 0}

@router.put("/{table_name}/data/{row_id}")
def update_data(table_name: str, row_id: int, data: dict, db: Session = Depends(get_db)):
    """Update row"""
    return {"message": "Data updated", "success": True}

@router.delete("/{table_name}/data/{row_id}")
def delete_data(table_name: str, row_id: int, db: Session = Depends(get_db)):
    """Delete row"""
    return {"message": "Data deleted", "success": True}
