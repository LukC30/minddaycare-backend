from .schema import *
from .model import *
from typing import List, Tuple, override
from functools import singledispatchmethod

class UserMapper():

    @singledispatchmethod
    @staticmethod
    def to_user_model_list(data):
        raise NotImplementedError("Tipo de dado não permitido para a conversão")

    @to_user_model_list.register   
    @staticmethod
    def _(user_request_list: list):
        user_model_list = [UserMapper.to_model(user_request) for user_request in user_request_list]
        return user_model_list
    
    @to_user_model_list.register
    @staticmethod
    def _(user_data: list):
        user_model_list = [UserMapper.to_model(user) for user in user_data]
        return user_model_list
    
    @singledispatchmethod
    @staticmethod
    def to_model(data):
        raise NotImplementedError("Tipo de dado não permitido para a conversão")

    @to_model.register
    @staticmethod
    def _(user_request: UserRequestDTO) -> UserModel:
        user_model = UserModel(**user_request.model_dump().copy())
        return user_model
    
    @to_model.register
    @staticmethod
    def _(user_data: tuple) -> UserModel:
        user_model = UserModel(id=user_data[0], nome=user_data[1], email=user_data[2], senha=user_data[3], telefone=user_data[4], created_at=user_data[5],is_active=user_data[6])
        return user_model
    
    @singledispatchmethod
    @staticmethod
    def to_insert(data):
        raise NotImplementedError("Tipo de dado não permitido para a conversão")

    @to_insert.register
    @staticmethod
    def _(user_model: UserModel) -> tuple:
        insert_data = (user_model.nome, user_model.email, user_model.senha, user_model.telefone)
        return insert_data
    
    @to_insert.register
    @staticmethod
    def _(user_request: UserRequestDTO) -> tuple:
        insert_data = (user_request.nome, user_request.email, user_request.senha, user_request.telefone)
        return insert_data
    
    @singledispatchmethod
    @staticmethod
    def to_user_response_schema(data):
        raise NotImplementedError("Tipo de dado não permitido para a conversão")

    @to_user_response_schema.register
    @staticmethod
    def _(user_model: UserModel) -> UserResponseDTO:
        user_response = UserResponseDTO(nome=user_model.nome, email=user_model.email)
        return user_response
    
    @to_user_response_schema.register
    @staticmethod
    def _(user_request: UserRequestDTO) -> UserResponseDTO:
        user_response = UserResponseDTO(nome = user_request.nome, email=user_request.email)
        return user_response
    
    @staticmethod
    def to_user_response_schema_list(user_model_list: List[UserModel]) -> List[UserResponseDTO]:
        user_response_list = [UserMapper.to_user_response_schema(user_model) for user_model in user_model_list]
        return user_response_list
    
    @staticmethod
    def to_response(users_response: List[UserResponseDTO]):
        users = [user.model_dump() for user in users_response]
        return users