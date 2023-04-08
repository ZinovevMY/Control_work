from controller.Controller import Controller
from datetime import *

class UserInterface:

    def __init__(self, controller: Controller):
        self.__controller = controller

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
                    new_note = self.input_note()
                    self.__controller.add_new_note(new_note)
                case 2:
                    notes = self.__controller.read_all_notes()
                    self.__controller.show_all_notes(notes)
                case 3:
                    self.__controller.read_all_notes()
                    note = self.__controller.search_by_id()


    def input_note(self):
        new_note = []
        header = input("Тема заметки: ")
        text = input("Текст заметки")
        dtm = datetime.now()
        new_note.append(header)
        new_note.append(text)
        new_note.append(dtm)
        return new_note
