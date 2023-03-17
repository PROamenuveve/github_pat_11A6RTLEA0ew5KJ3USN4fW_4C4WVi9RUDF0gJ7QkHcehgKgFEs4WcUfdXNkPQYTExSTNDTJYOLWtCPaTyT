
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty,NumericProperty,BooleanProperty
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCardSwipe







class les_noms():
    noms = ""
    nb_message = 0
    message  = ""
    vue = True
    def __init__ (self,nom,message,nb_message,vue):
        self.nom = nom 
        self.message = message
        self.nb_message = nb_message
        self.vue = vue
    def dictionaire(self):
        return {"nom":self.nom,"message":self.message,"nb_message":self.nb_message,"vue":self.vue}
    

class MenuPrincipale(MDBoxLayout):
    screen_stack = []
    right_action = []
    titres = []
    titre_de_bar = StringProperty()
    noms = "NOSSI"

    message = StringProperty()
    mon_Nom = []
    icon_left_action =  BooleanProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.titres.append("Messagerie")
        self.titre_de_bar =self.titres [len(self.titres)-1]
        self.nom = self.noms
        self.icon_left_action = True
        self.noms =[
            les_noms("NOSSI","salut salut",19,False),
            les_noms("MOSSI","mois c'est jeremie",25,False),
            les_noms("NOSSI","a demain",18,True),
            les_noms("MOUSSA","cc",20,False),
            les_noms("josianne","bisou",20,False),
            les_noms("daniel","daniel",5,True),
            les_noms("rose","salut",12,True),
            les_noms("jean","sa va ?",30,True),
            les_noms("alice","hello",1,False),
            les_noms("piere","je suis piere",22,False),
            les_noms("amenuveve","amen",19,False),
            les_noms("jeremie","victoire",2,True),
            les_noms("david","slt",8,False),
            les_noms("viviane","bonjour",20,False),
            les_noms("martin","salut la famille",15,True),
            les_noms("elise","bisou",7,True),
            les_noms("GOTO","hummmm",3,False),
            les_noms("louis","on se voit demain",6,False),
            les_noms("jacque","je suis etudient",22,False)
        ]
    def on_parent ( self, widget, parent):
        l= [
            les_noms.dictionaire() for les_noms  in self.noms
                    ]
        
        self.mon_Nom.data = l


    def push(self,titre):
        self.titres.append(titre)
        self.titre_de_bar =self.titres [len(self.titres)-1]
        self.icon_left_action = False
        
        
    def le_pere(self,commende):
        pass
        

    def suprimer (self):
        del self.titres[-1]
        self.titre_de_bar =self.titres [len(self.titres)-1]
        self.icon_left_action =  True





class LesNoms(MDBoxLayout):
    nom = StringProperty()
    nb_message = NumericProperty()
    message = StringProperty()
    vue = BooleanProperty()

class Menulist(MDCardSwipe):
    mon_Nom = []
    nom = StringProperty()
    nb_message = NumericProperty()
    message = StringProperty()
    vue = BooleanProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        

class Menumessage(MDBoxLayout):
    les_message = [ "salut","bonsoir ","cc","hello","comment ?","sa va" ,"cc","cc","bonjour","bonjour bonjour" ,"et la famille","ils vont bien" ]
    les_messages = []
    s = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.les_message :
            self.s.append(i) 
        self.les_messages = self.s





class MyScreenManager(ScreenManager):
    screen_stack = []
    texte = StringProperty()
    texte = "bonjour"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = self.texte

    def push(self, screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name

    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name
        
    

class BoxLayoutWithActionBar(MDBoxLayout):
    title = StringProperty()

class MessagesApp(MDApp):
    screen_stack = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "Blue"
    
    
MessagesApp().run()
