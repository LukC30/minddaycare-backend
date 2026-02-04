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
    
    @singledispatchmethod
    @staticmethod
    def to_confession_model(data):
        raise NotImplementedError("Tipo de dado não permitido para a conversão")

    @to_confession_model.register
    @staticmethod
    def _(id_user: int, confession_request: ConfessionResponseDTO):
        return ConfessionModel(id_user=id_user, humor=confession_request.humor, descricao=confession_request.descricao)
    
    @to_confession_model.register
    @staticmethod
    def _(confession_data: tuple):
        return ConfessionModel(id=confession_data[0], id_user=confession_data[1], humor=confession_data[2], descricao=confession_data[3], created_at=confession_data[4])

    @staticmethod
    def to_confession_model_list(confessions_data):
        confessions_models = [ConfessionMapper.to_confession_model(confession) for confession in confessions_data]
        return confessions_models