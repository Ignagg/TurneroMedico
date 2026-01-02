# Importamos Users y Perfiles
from .users import User, Rol, Cliente, Medico

# Importamos Estructura Médica
from .clinical import Especialidad, ObraSocial, Plan, Prestacion, Cobertura

# Importamos Turnos y Lógica
from .turnos import Turno, Notificaciones

# Importamos Registros Médicos (LO NUEVO)
from .records import Receta, HistoriaClinica