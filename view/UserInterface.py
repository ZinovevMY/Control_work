from controller.Controller import Controller
from datetime import *
from model.Note import Note

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
                    self.__controller.save_note(new_note)
                case 2:
                    self.show_all_notes()
                case 3:
                    self.show_all_notes()
                    self.edit_note()
                case 4:
                    self.read_note()
                case 5:
                    self.show_all_notes()
                    self.delete_note()
                case 6:
                    self.delete_all_notes()

    def input_note(self):
        header = input("Тема заметки: ")
        text = input("Текст заметки: ")
        dtm = datetime.now()
        return Note(header=header, text=text, date=dtm)

    def create_note(self):
        return self.__controller.save_note(self.input_note())

    def read_note(self):
        id = input("Введите ID заметки: ")
        note = self.__controller.read_note(id)
        print(note.__str__())

    def show_all_notes(self):
        notes = self.__controller.read_all_notes()
        for note in notes:
            print(note.__str__() + "\n")

    def edit_note(self):
        self.show_all_notes()
        id = input("Введите ID редактируемой заметки: ")
        try:
            self.__controller.update_note(id, self.input_note())
        except:
            print("Неверный ID!")

    def delete_note(self):
        self.show_all_notes()
        id = input("Введите ID удаляемой заметки: ")
        self.__controller.delete_note(id)

    def delete_all_notes(self):
        self.__controller.delete_all_notes()

