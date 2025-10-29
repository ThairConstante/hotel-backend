from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.reservation_model import Reservation
from app.models.client_model import Client
from app.models.user_model import Usuarios
from app.models.room_model import Room
from app.models.room_type_model import RoomType
from app.models.reservation_status_model import ReservationStatus

from app.schemas.reservation_schemas import ReservationCreate, ReservationUpdate


def get_reservas(db: Session):
    reservas = db.query(Reservation).all()
    resultado = []

    for r in reservas:
        # Cliente
        cliente = db.query(Client.Client_Names).filter(Client.Client_Id == r.Client_Id).first()
        cliente_nombre = cliente[0] if cliente else "No encontrado"

        # Habitación y tipo
        habitacion = db.query(Room.Room_Id, Room.Roomtype_Id).filter(Room.Room_Id == r.Room_Id).first()
        if habitacion:
            tipo = db.query(RoomType.Roomtype_Description).filter(RoomType.Roomtype_Id == habitacion.Roomtype_Id).first()
            habitacion_nombre = f" {habitacion.Room_Id} - {tipo[0]}" if tipo else f" {habitacion.Room_Id}"
        else:
            habitacion_nombre = "No encontrada"

        # Usuario
        usuario = db.query(Usuarios.User_Names).filter(Usuarios.User_Id == r.User_Id).first()
        usuario_nombre = usuario[0] if usuario else "No encontrado"

        # Estado de reserva
        estado = db.query(ReservationStatus.Reservationstatus_Description).filter(
            ReservationStatus.Reservationstatus_Id == r.Reservationstatus_Id
        ).first()
        estado_nombre = estado[0] if estado else "Sin estado"

        # Construimos el resultado
        resultado.append({
            "Res_Id": r.Res_Id,
            "Client_Id": r.Client_Id,
            "Room_Id": r.Room_Id,
            "User_Id": r.User_Id,
            "Reservationstatus_Id": r.Reservationstatus_Id,
            "Check_in_date": r.Check_in_date,
            "Check_out_date": r.Check_out_date,
            "Note": r.Note,
            "Total": r.Total,
            "cliente": cliente_nombre,
            "habitacion": habitacion_nombre,  
            "usuario": usuario_nombre,
            "estado": estado_nombre,
        })

    return resultado



def get_reserva(db: Session, reserva_id: int):
    return db.query(Reservation).filter(Reservation.Res_Id == reserva_id).first()


def crear_reserva(db: Session, reserva: ReservationCreate):
    # Verificar habitación
    habitacion = db.query(Room).filter(Room.Room_Id == reserva.Room_Id).first()
    if not habitacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Habitación no encontrada")

    if habitacion.Roomstatus_Id == 2:  # ocupada
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Habitación ya está ocupada")

    # Verificar estado de reserva
    estado_reserva = db.query(ReservationStatus).filter(
        ReservationStatus.Reservationstatus_Id == reserva.Reservationstatus_Id
    ).first()
    if not estado_reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado de reserva no encontrado")

    # Crear reserva
    db_reserva = Reservation(
        User_Id=reserva.User_Id,
        Client_Id=reserva.Client_Id,
        Room_Id=reserva.Room_Id,
        Reservationstatus_Id=reserva.Reservationstatus_Id,
        Check_in_date=reserva.Check_in_date,
        Check_out_date=reserva.Check_out_date,
        Total=reserva.Total,
        Note=reserva.Note
    )

    # Marcar habitación como ocupada
    habitacion.Roomstatus_Id = 2

    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva



def actualizar_reserva(db: Session, reserva_id: int, reserva: ReservationUpdate):
    db_reserva = get_reserva(db, reserva_id)
    if not db_reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva no encontrada")

    db_reserva.Client_Id = reserva.Client_Id
    db_reserva.Room_Id = reserva.Room_Id
    db_reserva.User_Id = reserva.User_Id
    db_reserva.Reservationstatus_Id = reserva.Reservationstatus_Id
    db_reserva.Check_in_date = reserva.Check_in_date
    db_reserva.Check_out_date = reserva.Check_out_date
    db_reserva.Note = reserva.Note
    db_reserva.Total = reserva.Total

    db.commit()
    db.refresh(db_reserva)
    return db_reserva





def get_estados(db: Session):
    estados = db.query(ReservationStatus).all()
    return [{"value": e.Reservationstatus_Id, "label": e.Reservationstatus_Description} for e in estados]
