from sqlalchemy.orm import Session
from app.models.room_model import Room
from app.models.room_type_model import RoomType
from app.models.room_status_model import RoomStatus
from app.schemas.room_schemas import RoomCreate, RoomUpdate
from fastapi import HTTPException, status

def get_rooms(db: Session):
    habitaciones = db.query(Room).all()
    resultado = []

    for h in habitaciones:
        # 🔹 Obtener tipo
        tipo = db.query(RoomType).filter(RoomType.Roomtype_Id == h.Roomtype_Id).first()
        tipo_info = None
        if tipo:
            tipo_info = {
                "Roomtype_Id": tipo.Roomtype_Id,
                "Roomtype_Description": tipo.Roomtype_Description
            }

        # 🔹 Obtener estado
        estado = db.query(RoomStatus).filter(RoomStatus.Roomstatus_Id == h.Roomstatus_Id).first()
        estado_info = None
        if estado:
            estado_info = {
                "Roomstatus_Id": estado.Roomstatus_Id,
                "Roomstatus_Description": estado.Roomstatus_Description
            }

        # 🔹 Construir el diccionario completo
        resultado.append({
            "Room_Id": h.Room_Id,
            "Room_night_price": h.Room_night_price,
            "Room_day_price": h.Room_day_price,
            "Room_Capacity": h.Room_Capacity,
            "Roomstatus_Id": h.Roomstatus_Id,
            "Roomtype_Id": h.Roomtype_Id,
            "tipo": tipo_info,
            "estado": estado_info
        })

    return resultado

    
def get_room_por_id(db: Session, room_id: int):
    return db.query(Room).filter(Room.Room_Id == room_id).first()


def room_create(db: Session, room: RoomCreate):
   
    existing_room = get_room_por_id(db, room.Room_Id)
    if existing_room:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Una habitacion esta registrada con el mismo Num"
        )

    # Crear el usuario normalmente
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def room_update(db: Session, room_id: int, room: RoomUpdate):
    db_room = db.query(Room).filter(Room.Room_Id == room_id).first()
    if not db_room:
        return None

    # Actualizar los campos
    db_room.Room_night_price = room.Room_night_price
    db_room.Room_day_price = room.Room_day_price
    db_room.Room_Capacity = room.Room_Capacity
    db_room.Roomstatus_Id = room.Roomstatus_Id
    db_room.Roomtype_Id = room.Roomtype_Id

    db.commit()
    db.refresh(db_room)
    return db_room




def get_tipos(db):
    tipos = db.query(RoomType).all()
    return [{"value": t.Roomtype_Id, "label": t.Roomtype_Description} for t in tipos]

def get_estados(db: Session):
    tipos = db.query(RoomStatus).all()
    return [{"value": t.Roomstatus_Id, "label": t.Roomstatus_Description} for t in tipos]
