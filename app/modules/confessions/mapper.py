from .schemas import ConfessionRequestDTO, ConfessionResponseDTO
from .models import ConfessionModel
from functools import singledispatchmethod

class ConfessionMapper():

    @singledispatchmethod
    @staticmethod
    def to_insert(data):
        raise NotImplementedError("Tipo de dado não permitido para a conversão")

    @to_insert.register
    @staticmethod
    def _(confession_model: ConfessionModel) -> tuple:
        data = (confession_model.id_user, confession_model.humor, confession_model.descricao)
        return data