class ServiceError(Exception):
    message = "Ошибка сервиса"


class InputServiceError(Exception):
    pass


class InvalidValue(InputServiceError):
    message = "Неправильный формат данных"
