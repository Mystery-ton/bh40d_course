class Car:
    """Класс представления автомобиля"""

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        """
        Инициализация атрибутов объекта

        :param color:
        :param count_passenger_seats:
        :param is_baby_seat:
        """
        if not isinstance(color, str):
            raise ValueError
        if not isinstance(count_passenger_seats, int):
            raise ValueError
        if not isinstance(is_baby_seat, bool):
            raise TypeError

        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self) -> None:
        print(
            f"Color is {self.color}, seats: {self.count_passenger_seats}, {'Car has baby seat ' if self.is_baby_seat==True else 'Car hasnt babyseat'}, {self.is_busy} "
        )


# car1 = Car(color="red", count_passenger_seats=5, is_baby_seat=True)
# print(car1)
