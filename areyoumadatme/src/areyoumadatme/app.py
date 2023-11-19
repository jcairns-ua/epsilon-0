"""
Social media for axious attachment styles<3
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class AreYouMadatMe(toga.App):

    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN, background_color="#704C5E"))
        self.box = toga.Box(style=Pack(background_color="#704C5E"))

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
            style=Pack(padding=5, background_color="#704C5E")            
        )

        signup_button = toga.Button(
            "Sign Up",
            on_press=self.signup,
            style=Pack(padding=5, background_color="#704C5E")
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
            "Still mad? Stay mad?",
            style=Pack(padding=(0, 5))
        )
        self.box_login = toga.Box(style=Pack(direction=COLUMN, padding=5))
        self.box_login.add(name_label)

        usern_label = toga.Label(
            "username:",
            style=Pack(padding=(0, 5))
        )
        self.usern_input = toga.TextInput(style=Pack(flex=1))
        self.box_login.add(usern_label)
        self.box_login.add(self.usern_input)

        password_label = toga.Label(
            "password:",
            style=Pack(padding=(0, 5))
        )
        self.password_input = toga.PasswordInput()
        self.box_login.add(password_label)
        self.box_login.add(self.password_input)

        self.main_box.add(self.box_login)

        self.enter_button = toga.Button("Enter", on_press=self.enter_login, style=Pack(padding=5))
        self.main_box.add(self.enter_button)

    def enter_login(self, widget):
        print(f"Hiiii, {self.usern_input.value} and {self.password_input.value}")
        self.main_page(widget)
        #call the check function returns true or false into logged
        """
        if logged:
            main_page()
        """

    
    def signup(self, widget):
        self.main_box.remove(self.box)
        print("not swag")
        name_label = toga.Label(
            "Ready to get mad!!!",
            style=Pack(padding=(0, 5))
        )
        self.box_login = toga.Box(style=Pack(direction=COLUMN, padding=5))
        self.box_login.add(name_label)

        name_label = toga.Label(
            "Name:",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.box_login.add(name_label)
        self.box_login.add(self.name_input)

        email_label = toga.Label(
            "Email:",
            style=Pack(padding=(0, 5))
        )
        self.email_input = toga.TextInput(style=Pack(flex=1))
        self.box_login.add(email_label)
        self.box_login.add(self.email_input)

        usern_label = toga.Label(
            "Username:",
            style=Pack(padding=(0, 5))
        )
        self.usern_input = toga.TextInput(style=Pack(flex=1))
        self.box_login.add(usern_label)
        self.box_login.add(self.usern_input)

        password_label = toga.Label(
            "Password:",
            style=Pack(padding=(0, 5))
        )
        self.password_input = toga.PasswordInput()
        self.box_login.add(password_label)
        self.box_login.add(self.password_input)
        self.main_box.add(self.box_login)

        self.enter_button = toga.Button("Enter", on_press=self.enter_signin, style=Pack(padding=5))
        self.main_box.add(self.enter_button)

    def enter_signin(self, widget):
        print(f"Hiiii, {self.name_input.value} and {self.email_input.value} {self.usern_input.value} {self.password_input.value}")
        self.main_page(widget)

    def main_page(self, widget):
        self.main_box.remove(self.box_login, self.enter_button)
        next_check = toga.Label("Time Till Next Check:", style=Pack(padding=(0,5), background_color="#44344F", color="#F1C8DB"))
        self.default_page = toga.Box(style=Pack(direction=COLUMN, padding=5))
        self.default_page.add(next_check)
        self.main_box.add(self.default_page)

def main():
    return AreYouMadatMe()
