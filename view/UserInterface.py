from controller.Controller import Controller

class UserInterface:

    def __init__(self):
        pass

    def main_menu(self):
        print('-----------')
        print('Мои заметки')
        print('-----------')
        print('Выберите действие:\n'
              '1. Создать новую заметку\n'
              '2. Посмотреть все заметки\n'
              '3. Редактировать заметку\n'
              '4. Найти заметку\n'
              '5. Удалить заметку\n'
              '6. Удалить все заметки\n'
              '0. Выход')

    def run(self):
        while True:
            self.main_menu()
            option = int(input('-> '))
            match(option):
                case 0:
                    quit()
                case 1:


