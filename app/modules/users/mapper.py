from .schema import *
from .model import *
from typing import List, Tuple, override

class UserMapper():

    @staticmethod
    def to_user_model(user_request: UserRequestDTO):
        user_model = UserModel(**user_request.model_dump().copy())
        return user_model
       
    @staticmethod
    def to_user_model_list(user_request_list: List[UserRequestDTO]):
        user_model_list = [(lambda user: UserModel(**user))(user_request)for user_request in user_request_list]
        return user_model_list
    
    @override
    @staticmethod
    def to_user_model_list(user_data: List[tuple]):
        user_model_list = [UserMapper.to_user_model(user) for user in user_data]
        return user_model_list
    
    @override
    @staticmethod
    def to_user_model(user_data: Tuple) -> UserModel:
        pass

    @staticmethod
    def to_insert(user_model: UserModel):
        insert_data = (user_model.nome, user_model.email, user_model.senha, user_model.telefone)
        return insert_data

    @staticmethod
    def to_user_response_schema(user_model: UserModel):
        user_response = UserResponseDTO(nome=user_model.nome,email=user_model.email)
        return user_response
    
    def to_user_response_schema_list(user_model_list: List[UserModel]):
        user_response_list = [(lambda user: UserResponseDTO(nome=user.nome,email=user.email))(user_model)for user_model in user_model_list]
        return user_response_list
    
    def to_response(users_response: List[UserResponseDTO]):
        users = [user.model_dump() for user in users_response]
        return users