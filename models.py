# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, String, Time, text, create_engine
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

engine = create_engine('mysql+pymysql://root:123@localhost:3306/odontosys', poolclass=NullPool)
#CREA LA CONEXION
db_session = scoped_session(sessionmaker(bind=engine, autocommit=False))
Base = declarative_base()
Base.query = db_session.query_property()
metadata = Base.metadata


class TPaciente(Base):
    __tablename__ = 't_paciente'

    id_pacientes = Column(INTEGER(11), primary_key=True)
    nombres = Column(String(500), nullable=False)
    apellidos = Column(String(500), nullable=False)
    documento = Column(String(500), nullable=False)
    direccion = Column(String(500), nullable=False)
    ciudad = Column(String(500), nullable=False)
    telefono = Column(String(500), nullable=False)
    email = Column(String(500), nullable=False)
    razon_social = Column(String(500), nullable=False)
    ruc = Column(String(500), nullable=False)
    activo = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class TTarjetaHorario(Base):
    __tablename__ = 't_tarjeta_horario'

    id_tarjeta_horario = Column(SMALLINT(6), primary_key=True)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    activo = Column(TINYINT(1), nullable=False)


class TTipoAgendum(Base):
    __tablename__ = 't_tipo_agenda'

    id_tipo_agenda = Column(INTEGER(11), primary_key=True)
    denominacion = Column(String(500), nullable=False)
    activo = Column(TINYINT(1), nullable=False)


class TTipoUsuario(Base):
    __tablename__ = 't_tipo_usuario'

    id_tipo = Column(SMALLINT(6), primary_key=True)
    denominacion = Column(String(500), nullable=False)
    activo = Column(String(500), nullable=False)


class TUsuario(Base):
    __tablename__ = 't_usuario'

    username = Column(String(500), primary_key=True)
    hash_password = Column(String(500), nullable=False)
    nombres = Column(String(500), nullable=False)
    apellidos = Column(String(500), nullable=False)
    activo = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    id_tipo = Column(ForeignKey('t_tipo_usuario.id_tipo'), nullable=False, index=True)

    t_tipo_usuario = relationship('TTipoUsuario')


class TAgendum(Base):
    __tablename__ = 't_agenda'

    id_pacientes = Column(ForeignKey('t_paciente.id_pacientes'), primary_key=True, nullable=False)
    username = Column(ForeignKey('t_usuario.username'), primary_key=True, nullable=False, index=True)
    fecha_cita = Column(Date, primary_key=True, nullable=False)
    descripcion = Column(String(500), nullable=False)
    estado = Column(String(500), nullable=False)
    id_tipo_agenda = Column(ForeignKey('t_tipo_agenda.id_tipo_agenda'), nullable=False, index=True)

    t_paciente = relationship('TPaciente')
    t_tipo_agendum = relationship('TTipoAgendum')
    t_usuario = relationship('TUsuario')


class TCita(Base):
    __tablename__ = 't_cita'
    __table_args__ = (
        ForeignKeyConstraint(['id_pacientes', 'username', 'fecha_cita'], ['t_agenda.id_pacientes', 't_agenda.username', 't_agenda.fecha_cita']),
    )

    id_pacientes = Column(ForeignKey('t_paciente.id_pacientes'), primary_key=True, nullable=False)
    username = Column(String(500), primary_key=True, nullable=False)
    fecha_cita = Column(Date, primary_key=True, nullable=False)
    id_tarjeta_horario = Column(ForeignKey('t_tarjeta_horario.id_tarjeta_horario'), primary_key=True, nullable=False, index=True)
    denominacion = Column(String(500), nullable=False)
    estado = Column(String(500), nullable=False)

    t_agendum = relationship('TAgendum')
    t_paciente = relationship('TPaciente')
    t_tarjeta_horario = relationship('TTarjetaHorario')
