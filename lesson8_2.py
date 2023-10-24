from lesson8_1 import Car


class Taxi:
    """Класс представления такси"""

    def __init__(self, cars: list[Car]):
        """

        :param cars: список автомобилей
        """
        if not isinstance(cars, list):
            raise ValueError

        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for i in self.cars:
            if count_passengers <= i.count_passenger_seats and (
                is_baby == i.is_baby_seat or is_baby == False
            ):
                i.is_busy = True
                return i
        return None


car1 = Car(color="red", count_passenger_seats=5, is_baby_seat=True)

car2 = Car(color="white", count_passenger_seats=5, is_baby_seat=False)
yandex_taxi = Taxi([car1, car2])
print(yandex_taxi.find_car(count_passengers=2, is_baby=False).__str__())
