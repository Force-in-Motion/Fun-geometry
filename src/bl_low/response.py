

class ResponseUser:

    @staticmethod
    def provides_data(data: list):
        """
        Транслирует пользователю полученные данные
        :param data: list
        """
        for elem in data:
            print(elem)

