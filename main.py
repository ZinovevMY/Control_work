from controller.Controller import Controller
from model.Note import Note
from model.Repository import Repository
from model.Notemapper import Notemapper
from model.Fileoperations import Fileoperations
from view.UserInterface import UserInterface

if __name__ == '__main__':
    file = Fileoperations("notes")
    mapper = Notemapper()
    repo = Repository(file, mapper)
    controller = Controller(repo)
    ui = UserInterface(controller)
    ui.run()