# empleado_limpieza.py
from empresa import Empresa
from persona import Persona

class EmpleadoLimpieza(Persona, Empresa):
    def __init__(self):
        Persona.__init__(self)
        Empresa.__init__(self)
        self._numero_empleado = ""

    # Getter y Setter
    def get_numero_empleado(self):
        return self._numero_empleado

    def set_numero_empleado(self, numero_empleado):
        self._numero_empleado = numero_empleado

    def mostrar_informacion(self):
        base_info_persona = Persona.mostrar_informacion_perosna(self)
        base_info_empresa = Empresa.mostrar_informacion_empresa(  self)
        return f"{base_info_persona}, {base_info_empresa}, Número de Empleado: {self._numero_empleado}, Turno: {self._turno}"