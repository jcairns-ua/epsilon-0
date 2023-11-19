"""
Social media for axious attachment styles<3
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class AreYouMadatMe(toga.App):

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.box = toga.Box()

        name_label = toga.Label(
            "Are You Mad at Me?",
            style=Pack(padding=(0, 5))
        )
        #self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        #name_box.add(self.name_input)

        login_button = toga.Button(
            "Login",
            on_press = self.login,
            style=Pack(padding=5)            
        )

        signup_button = toga.Button(
            "Sign Up",
            on_press=self.signup,
            style=Pack(padding=5)
        )

        self.box.add(name_box)
        self.box.add(login_button)
        self.box.add(signup_button)
        
        self.main_box.add(self.box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
        
    def login(self, sender):
        self.main_box.remove(self.box)
        print("swag")
        name_label = toga.Label(
            "stay mad?",
            style=Pack(padding=(0, 5))
        )
        self.main_box.add(name_label)

    def signup(self, widget):
        self.main_box.remove(self.box)
        print("no swag")


def main():
    return AreYouMadatMe()
