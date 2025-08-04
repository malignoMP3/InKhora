from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class AuthLoginService(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        tipo_de_login = kwargs.get("tipo_de_login", "usuario")

        try:
            if tipo_de_login == "tatuador":
                user = UserModel.objects.get(
                    Q(email__iexact=username) |
                    Q(tattoo_profile__artistic_name__iexact=username)
                )
            elif tipo_de_login == "usuario":
                user = UserModel.objects.get(
                    Q(email__iexact=username) |
                    Q(phone__iexact=username)
                )
            elif tipo_de_login == "root":
                user = UserModel.objects.get(
                    Q(email__iexact=username) |
                    Q(username__iexact=username)
                )
            else:
                return None
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
