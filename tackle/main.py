from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.textinput import TextInput
from kivy.factory import Factory



nav = {"manifest": ["Create Manifest", "Modify Manifest", "Cancel Manifest", "Combine Manifest", "Trans-load Manifest"],
        "ticket": ["Create Ticket","Modify Ticket","Cancel Ticket","View Tickets"],
        "journal": ["Create Loading info"],
        "report": ["Create Incident Report", "View Incident Report", "Sales Report"]}
menu = ["Manifest", "Ticket", "Journal", "Report"]





# username : password dict
users = {"admin": "admin", "demo": "demo"}


class TackleRoot(BoxLayout):

    texture = ObjectProperty()
    navigation = ObjectProperty()

    def __init__(self, **kwargs):
        super(TackleRoot, self).__init__(**kwargs)
        self.texture = Image(source='icons/bg.png').texture




class LoginScreen(BoxLayout):


    """
    This screen takes care of User Login etc...

    """
    def login(self):

            if self.uname.text != "" and self.password.text != "":
                try:
                    if self.password.text != users[self.uname.text]:
                        raise KeyError
                    else:
                        self.clear_widgets()
                        transport = TransportScreen()
                        self.add_widget(transport)
                except KeyError:
                    self.message.text = "Username or Password incorrect"
            else:
                self.message.text = "Nothing entered! Please type in your username and password"


class FormInput(TextInput):
    next = ObjectProperty()
    def _keyboard_on_key_down(self, window, keycode, text, modifiers):

        if keycode[0] == 9:  # 9 is the keycode for tab
            self.next.focus = True
        elif keycode[0] == 13:  # 13 is the keycode for enter
            self.parent.parent.set_odds()
        else:
            super(FormInput, self)._keyboard_on_key_down(
                window, keycode, text, modifiers)



class TransportScreen(BoxLayout):
    #@Todo implement screen selection, logic and actions
    """
    This screen takes care of all courier and Transport related operations
    Manifest Generation, Ticket, Route Management etc...

    """
    navi = ObjectProperty()

    def __init__(self, **kwargs):
        super(TransportScreen, self).__init__(**kwargs)
        self.get_navigation_items()

    def get_navigation_items(self):
        navi = Menu()
        items = navi.update_navigation()
        del self.navi.adapter.data[:]
        self.navi.adapter.data.extend(items)
        self.navi._trigger_reset_populate()


class CourierScreen(BoxLayout):
     #@Todo implement screen selection, logic and actions
    """
    This screen takes care of all courier and cargo related operations
    Order/Airway Bill, etc
    """
    pass

class NavigationButton(ListItemButton):
    pass


class Menu(BoxLayout):

    def update_navigation(self):
        menu_name = ""
      #  for id in self.menu.ids:
        #    print (id)
       #     if id.state == "down":
       #         menu_name = id

        navi= self.get_navi_menu("nav", "manifest")

        return navi


    def get_navi_menu(self, category, navi=None):
        if not category == "menu":
            menu_template = nav[navi]
        else:
            menu_template = menu
        return menu_template


class Tackle(App):
    def build(self):
        root = TackleRoot()
        return root

if __name__ == '__main__':
    Tackle().run()
