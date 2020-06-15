from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, IntField, UUIDField
)

class Department(Document):
    meta = {'collection': 'upax_department'}
    name = StringField()

class Role(Document):
    meta = {'collection': 'upax_role'}
    name = StringField()

class FranquiciaDashboard(Document):
    meta = {'collection': 'franquicia_dashboard'}
    _id = UUIDField()
    id = IntField()
    nombre = StringField()
    tipoDashboard = IntField()
    alcance = IntField()
    nombreAlcance = StringField()
    anioAlcance = IntField()
    idDimension = IntField()
    nombreDimension = StringField()
    idRubro = IntField()
    nombreRubro = StringField()
    idEncuesta = IntField()
    idEncuestaContestada = IntField()
    ponderacionEvaluador = IntField()
    ponderacionObtenida = IntField()
    ponderacionImperdonables = IntField()
    textoPregunta = StringField()
    idOpcRespuesta = IntField()
    textoRespuesta = StringField()
    tipoRubro = IntField()
    idPregunta = IntField()
    ordenDimension = IntField()
    descripcionScored = StringField()
    observacionesCalidad = StringField()
    idTipoOpcionRespuesta = IntField()
    ordenRubro = IntField()
    scoredVisible = IntField()



class Employee(Document):
    meta = {'collection': 'upax_employee'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    role = ReferenceField(Role)

