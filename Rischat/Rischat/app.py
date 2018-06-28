import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import eliza
import random

class Rischat(toga.App):
    def startup(self):

        self.chat = toga.DetailedList(data=[
            {
                'icon':toga.Icon(),
                'title':'RisBot',
                'subtitle':'Hello,Wassup?',
            }
        ],style=Pack(flex=1))

        self.text_input = toga.TextInput(style=Pack(flex=1))
        send_button = toga.Button('Send',style=Pack(padding_left=5),on_press=self.handle_input)

        input_box = toga.Box(children=[self.text_input,send_button],
                             style=Pack(direction=ROW,alignment='CENTER',padding=5))


        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        main_box = toga.Box()

        # Add the content on the main window
        self.main_window.content = toga.Box(children=[self.chat,input_box],
                                            style=Pack(direction=COLUMN))


        self.partner = eliza.Eliza()
        # Show the main window
        self.main_window.show()

    def handle_input(self,widget,**kwargs):
        input_text = self.text_input.value

        self.chat.scroll_to_bottom()

        yield random.random()*3

        response = self.partner.respond(input_text)
        self.chat.data.append(
            icon=toga.Icon(),
            title='You',
            subtitle=input_text,
        )

        self.text_input.value=''


def main():
    return Rischat('RisChat', 'org.risabhmishra.Rischat')

