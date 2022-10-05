from zoneinfo import available_timezones
from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'cadastrar_usuarios_aux': True,
        'conceder_permissoes': True,
        'remover_usuarios_aux': True,
    }

class Auxiliar(AbstractUserRole):
    available_permissions = {
        'cadastrar_patrimonio': True,
        'editar_patrimonio': True,
        'remover_patrimonio': True,
        'remover_comentario': True,
    }