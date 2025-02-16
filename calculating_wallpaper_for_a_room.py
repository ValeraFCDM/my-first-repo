from math import ceil

class WinDoor:
    """
    Класс, представляющий окна и двери помещения.
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        self.square = x * y


class Room:
    """
        Класс, представляющий комнату.
    """

    def __init__(self, x: int | float, y: int | float, z: int | float) -> None:
        """
        Создание и подготовка к работе объекта класса Room.
        Объект имеет 3 замера и пустой список для добавления окон и дверей.

        :param x: int | float:  длина комнаты
        :param y: int | float:  ширина комнаты
        :param z: int | float:  высота комнаты
        """
        self.length = x
        self.width = y
        self.height = z
        self.wd = []

    def walls_square(self) -> int | float:
        return 2 * self.height * (self.width + self.length)

    def add_wd(self, w, h) -> None:
        self.wd.append(WinDoor(w, h))

    def work_surface(self) -> int | float:
        wd_square = 0
        for wd in self.wd:
            wd_square += wd.square
        return self.walls_square() - wd_square

    def wallpaper_roll_count(self, w: int | float, l: int | float) -> int:
        return ceil(self.work_surface() / (w * l))


def get_validate_input(parameter: str, input_type: type) -> int | float:
    """
    Проверка формата ввода от пользователя.
    Запрашивает у пользователя замер определенного объекта, до тех пор,
    пока пользователь не укажет положительное число.

    :param parameter: str: описание запрашиваемого измерения (длина, количество и т.д.)
    :param input_type: type: int или float, в зависимости от запрашиваемого измерения
    :return: int | float: замер объекта для формирования параметров объекта Room()
    :raise: ValueError: если пользователь ввел не число
    """
    number = None
    while True:
        try:
            number = input_type(input(f'Введите параметр - {parameter}: '))
        except ValueError:
            print('Недопустимое значение!')
            continue
        if number > 0:
            break
        print('Недопустимое значение!')
    return number


room_length = get_validate_input('длина помещения', float)
room_width = get_validate_input('ширина помещения', float)
room_height = get_validate_input('высота помещения', float)

room = Room(room_length, room_width, room_height)   # экземпляр класса Room с введенными параметрами

wd_count = get_validate_input('количество дверей и окон', int)
i = 0
while i < wd_count:
    print(f'\nУкажите замеры для окна/двери №{i + 1}!')
    wd_width = get_validate_input('ширина', float)
    wd_height = get_validate_input('высота', float)
    room.add_wd(wd_width, wd_height)
    i += 1

if room.work_surface() > 0: # проверка, не превышает ли площадь окон/дверей площадь стен.
    print('\nУкажите параметры выбранных обоев!')
    roll_width = get_validate_input('ширина рулона', float)
    roll_length = get_validate_input('длина рулона', float)

    print(f'\nОклеиваемая поверхность вашего помещения: {room.work_surface()}.'
          f'\nНеобходимо рулонов обоев: {room.wallpaper_roll_count(roll_width, roll_length)} шт.')
else:
    print('\nГабариты окон и дверей превышают площадь стен помещения! '
          'Проверьте правильность замеров и попробуйте сначала!')
