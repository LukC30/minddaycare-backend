from .model import AuthModel

class AuthMapper():

    @staticmethod
    def model_to_tuple(auth_model: AuthModel):
        return(auth_model.id_user, auth_model.token, auth_model.created_at, auth_model.expires_at)
    
    @staticmethod
    def tuple_to_model(data: tuple):
        return AuthModel(id_user=data[1], token=data[2], created_at=data[3], expires_at=data[4])