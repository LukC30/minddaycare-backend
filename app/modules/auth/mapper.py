from .model import AuthModel

class AuthMapper():

    @staticmethod
    def model_to_tuple(auth_model: AuthModel):
        return(auth_model.id_user, auth_model.token, auth_model.created_at, auth_model.expires_at)