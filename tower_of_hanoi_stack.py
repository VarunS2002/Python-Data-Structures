from stack import Stack


class TowerOfHanoi:
    class __EmptySourceRodError(Exception):
        def __str__(self) -> str:
            return "Number of disks in the source rod cannot be less than 1."

    class __AlreadySolvedError(Exception):
        def __str__(self) -> str:
            return "The puzzle has already been solved. Please reset the puzzle before adding more disks."

    def __init__(self) -> None:
        self.__source_rod: Stack = Stack()
        self.__auxiliary_rod: Stack = Stack()
        self.__destination_rod: Stack = Stack()
        self.__no_of_disks: int = 0
        self.__solved: bool = False

    def solved(self) -> bool:
        return self.__solved

    def add_disks(self, no_of_disks: int) -> None:
        if not self.__solved:
            self.__no_of_disks += no_of_disks
            self.__source_rod.empty_stack()
            for disk_id in reversed(range(1, self.__no_of_disks + 1)):
                self.__source_rod.push(f'disk {disk_id}')
        else:
            raise self.__AlreadySolvedError

    def display(self) -> None:
        print(self.__source_rod, end=' - ')
        print(self.__auxiliary_rod, end=' - ')
        print(self.__destination_rod)

    def __tower_of_hanoi(self, disks: int, source: Stack, destination: Stack, auxiliary: Stack) -> None:
        if disks == 1:
            source.pop()
            destination.push('disk 1')
        elif disks > 1:
            self.__tower_of_hanoi(disks - 1, source=source, destination=auxiliary, auxiliary=destination)
            source.pop()
            destination.push(f'disk {disks}')
            self.__tower_of_hanoi(disks - 1, source=auxiliary, destination=destination, auxiliary=source)

    def start(self) -> None:
        if self.__no_of_disks < 1:
            raise self.__EmptySourceRodError
        self.__tower_of_hanoi(len(self.__source_rod), self.__source_rod, self.__destination_rod, self.__auxiliary_rod)
        self.__solved = True

    def reset(self) -> None:
        self.__source_rod.empty_stack()
        self.__auxiliary_rod.empty_stack()
        self.__destination_rod.empty_stack()
        self.__no_of_disks = 0
        self.__solved = False


if __name__ == '__main__':
    tower = TowerOfHanoi()
    tower.add_disks(int(input('Enter the number of the disks : ')))
    print("Adding 2 more disks")
    tower.add_disks(2)
    print("Unsolved")
    tower.display()
    tower.start()
    print("Solved")
    tower.display()
    tower.reset()
    print("Reset")
    tower.display()