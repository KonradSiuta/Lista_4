class Pupil:
    available_marks = set({1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6})

    def __init__(self, name, surname) -> None:
        self._name = name
        self._surname = surname
        self._marks = dict()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Podane imie nie jest ciagiem znakow")
        if len(name) < 3:
            raise ValueError("Podane imie jest za krotkie")
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Podane imie nie jest ciagiem znakow")
        if len(surname) < 3:
            raise ValueError("Podane imie jest za krotkie")
        self._surname = surname

    def complete_marks(self):
        while True:
            subject = str(input("Podaj nazwe przedmiotu (aby zakonczyć wpisz koniec): "))
            if subject == "koniec":
                break
            mark = float(input("Podaj ocene: "))
            if isinstance(mark, int):
                mark = float(mark)
            if not isinstance(subject, str) or not isinstance(mark, float):
                raise TypeError("Przedmiot i ocena nie sa ciagiem znakow")
            if subject == "" or mark == "":
                raise ValueError("Nie podano przedmiotu lub oceny")
            if mark not in Pupil.available_marks:
                raise ValueError("Nieprawidlowa ocena")
            self._marks[subject] = mark

    def print_marks(self):
        for subject, mark in self.marks.items():
            print(f'{subject}: {mark}')

    def mean(self):
        sum = 0
        for mark in self._marks.values():
            sum += mark
        return sum / len(self._marks)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}: {self.mean()}'

class Student(Pupil):
    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)
        self.weights = dict()

    def complete_weights(self):
        for subject in self._marks:
            temp = float(input(f'Podaj wage oceny z przedmiotu {subject}: '))
            if temp is None:
                raise ValueError("Nie podano wagi")
            if temp < 0 or temp > 1:
                raise ValueError("Waga musi byc w przedziale [0, 1]")
            self.weights[subject] = float(temp)

    def mean(self):
        sum = 0
        for subject, mark in self._marks.items():
            sum += mark * self.weights[subject]
        sum_weights = 0
        for subject, weight in self.weights.items():
            sum_weights += weight

        return sum / sum_weights

    def __str__(self) -> str:
        return super().__str__()

if __name__ == "__main__":
    # pupil1 = Pupil("Jan", "Kowalski")
    # pupil1.complete_marks()
    # print(pupil1)

    student1 = Student("Adam", "Malinowski")
    student1.complete_marks()
    student1.complete_weights()
    print(student1)