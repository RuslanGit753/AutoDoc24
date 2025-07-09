import jwt
from utils.token_appl_1_api import bearer_appl_1


def decod_token_appl():
    token_appl = jwt.decode(
        bearer_appl_1, options={"verify_signature": False},
        algorithms=["HS256", "RS256"])

    # Извлечение user_id из декодированного токена
    user_id_appl = token_appl.get('user_id')

    # Запись user_id в файл user_id_appl_api.py
    with open("utils/user_id_appl_api.py", "w") as file:
        file.write(f"user_id_appl = {repr(user_id_appl)}")
