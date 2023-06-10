from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
import os
import ast
import time

#для озвучки
import pyttsx3
from win32com.client import Dispatch


#zvuk=""
#ввод текста из консоли- a=str(input('Ввод текста (русский\английский-без разницы): '))



class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        #начинается другое

        #------------------
        box.add_widget(Button(text='Recipe Set', color='black', background_color =('#E318FF'), font_size=dp(100), on_press=lambda x:
                              set_screen('glavnay')))
        
        self.add_widget(box)


class Glavnay(Screen):
    def __init__(self, **kw):
        super(Glavnay, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        

        self.layout = GridLayout(cols=4, spacing=15, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Страница приветствия', color='white', background_color =('#9400D3'),
                             on_press=lambda x: set_screen('menu'),
                             size_hint_y=None, height=dp(40))
        
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        btn3 = Button(text ='Sport', color =('white'), font_size ="18sp", background_color =('#E318FF'), pos =(300, 250), on_press=lambda x:
                      set_screen('sport'))
        self.layout.add_widget(btn3)
        btn4 = Button(text ='Timer ', color =('white'), font_size ="18sp", background_color =('#E318FF'), pos =(300, 250), on_press=lambda x:
                      set_screen('timer'))
        self.layout.add_widget(btn4)
        btn5 = Button(text ='Рецепты ', color =('white'), font_size ="18sp", background_color =('#E318FF'), pos =(300, 250), on_press=lambda x:
                      set_screen('recipe')) 
        self.layout.add_widget(btn5)
        
        btn6 = Button(text ='Добавить Свой Рецепт ', color =('white'), font_size ="18sp", background_color =('#E318FF'), pos =(300, 250), on_press=lambda x:
                      set_screen('add')) 
        self.layout.add_widget(btn6)

        btn7 = Button(text =' добавленные рецепты ', color =('white'), font_size ="18sp", background_color =('#E318FF'), pos =(800, 250), on_press=lambda x:
                      set_screen('list_food')) 
        self.layout.add_widget(btn7)
        dic_foods = ast.literal_eval(
            App.get_running_app().config.get('General', 'user_data'))



    def on_leave(self):  # Будет вызвана в момент закрытия экрана

        self.layout.clear_widgets()  # очищаем список
        
class Sport(Screen):
    def __init__(self, **kw):
        super(Sport, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        #начинается другое

        #------------------
        box.add_widget(Button(background_color =('black'), font_size=dp(30), on_press=lambda x:
                              set_screen('sport')))
        
        self.add_widget(box)
    def on_enter(self):  # Будет вызвана в момент открытия экрана

        
        self.layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        btn5 = Button(text ='< Назад в главное меню', color =('white'), font_size ="15sp", background_color =('#E318FF'), pos =(200, 150), on_press=lambda x:
                      set_screen('glavnay'))
        self.layout.add_widget(btn5)

        btn100 = Button(text ='< Этот раздел скоро появится >', color =('white'), font_size ="15sp", background_color =('black'), pos =(600, 3040), on_press=lambda x:
                      set_screen('menu'))
        self.layout.add_widget(btn100)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        #btn2 = Button(text ='Hello World ', color =('blue'), font_size ="15sp", background_color =('#1822FF'), pos =(300, 250))

class Timer(Screen):
    def __init__(self, **kw):
        super(Timer, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        #начинается другое

        #------------------
        box.add_widget(Button(background_color =('black'), font_size=dp(40), on_press=lambda x:
                              set_screen('timer')))
        
        self.add_widget(box)
        

    
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        

        self.layout = GridLayout(cols=4, spacing=15, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='Поставить таймер', color='white', background_color =('#E318FF'),
                             on_press=lambda x: set_screen('add_food'),
                             size_hint_y=None, height=dp(40))
        
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

        
class Recipe(Screen):
    def __init__(self, **kw):
        super(Recipe, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        #начинается другое

        #------------------
        box.add_widget(Button(background_normal = 'C:\кнопки,фотки и прочее\рецепты фон.png', font_size=dp(40), on_press=lambda x:
                              set_screen('recipe')))
        
        self.add_widget(box)
        
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        

        self.layout = GridLayout(cols=5, spacing=40, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Вернуться',
                             on_press=lambda x: set_screen('glavnay'),
                             size_hint_y=None, height=dp(40))
        
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        
        btn8 = Button(text ='Блины', color =('white'), font_size ="20sp", background_color =('#BB08FD'), pos =(300, 250), on_press=lambda x:
                              set_screen('blin'))
        self.layout.add_widget(btn8)
        
        btn9 = Button(text ='Салат "Цезарь"', color =('white'), font_size ="15sp", background_color =('#BB08FD'), pos =(900, 950), on_press=lambda x:
                              set_screen('salade_king'))
        self.layout.add_widget(btn9)
        
        btn10 = Button(text ='Борщ', color =('#FFFFFF'), font_size ="20sp", background_color =('#BB08FD'), pos =(300, 250), on_press=lambda x:
                              set_screen('borsh'))
        self.layout.add_widget(btn10)
        
        btn11 = Button(text ='Омлет', color =('white'), font_size ="20sp", background_color =('#BB08FD'), pos =(350, 350), on_press=lambda x:
                              set_screen('omlet'))
        self.layout.add_widget(btn11)
        
        btn12 = Button(text ='Оливье', color =('white'), font_size ="20sp", background_color =('#BB08FD'), pos =(350, 350), on_press=lambda x:
                              set_screen('olive'))
        self.layout.add_widget(btn12)
        
        dic_foods = ast.literal_eval(
            App.get_running_app().config.get('General', 'user_data'))
#--------------------------------------------------------------------------------------START---------------------------------------------------

class Vdele(Screen):
    def __init__(self, **kw):
        super(Vdele, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='Назад', color='white', background_color='red',
                              on_press=lambda x: set_screen('glavnay')))
        self.add_widget(box)

class SortedListFood(Screen):
    def __init__(self, **kw):
        super(SortedListFood, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана

        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Назад в главное меню',
                             on_press=lambda x: set_screen('menu'),
                             size_hint_y=None, height=dp(40))
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

        dic_foods = ast.literal_eval(
            App.get_running_app().config.get('General', 'user_data'))

        for f, d in sorted(dic_foods.items(), key=lambda x: x[1]):
            fd = f.decode('u8') + ' ' + (datetime.fromtimestamp(d).strftime('%Y-%m-%d'))
            btn = Button(text=fd, size_hint_y=None, height=dp(40), on_press=lambda x:
                              set_screen('maksvdele'))
            self.layout.add_widget(btn)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана

        self.layout.clear_widgets()  # очищаем список


class Add(Screen):

    def buttonClicked(self, btn1):
        if not self.txt1.text:
            return
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'user_data'))
        self.app.user_data[self.txt1.text.encode('u8')] = int(time.time())

        self.app.config.set('General', 'user_data', self.app.user_data)
        self.app.config.write()

        text = "Последнее добавленное блюдо:  " + self.txt1.text
        self.result.text = text
        self.txt1.text = ''

    def __init__(self, **kw):
        super(Add, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        back_button = Button(text='< Назад в главное меню', on_press=lambda x:
                             set_screen('menu'), size_hint_y=None, height=dp(40))
        box.add_widget(back_button)
        self.txt1 = TextInput(text='', multiline=False, height=dp(40),
                              size_hint_y=None, hint_text="Название блюда")
        box.add_widget(self.txt1)
        btn1 = Button(text="Добавить блюдо", size_hint_y=None, height=dp(40))
        btn1.bind(on_press=self.buttonClicked)
        box.add_widget(btn1)
        self.result = Label(text='')
        box.add_widget(self.result)
        self.add_widget(box)




        
#-----------------------------------------------------FINISH----------------------------------------------------------------------

class Blin(Screen):
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        self.layout = GridLayout(cols=5, spacing=40, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Вернуться',
                             on_press=lambda x: set_screen('recipe'),
                             size_hint_y=None, height=dp(40))
        
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        
    def __init__(self, **kw):
        super(Blin, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')

        box.add_widget(Button(text='Блины, способ приготовления:', font_size=dp(15), color='black',  background_color =('#E318FF'), on_press=lambda x:
                              set_screen('recipe')))
        
        self.add_widget(box)
        
class Borsh(Screen):
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        

        self.layout = GridLayout(cols=4, spacing=40, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Вернуться',
                             on_press=lambda x: set_screen('recipe'),
                             size_hint_y=None, height=dp(40))
        

        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        #a='Находится в разработке, но всё равно работает'
        btn15 = Button(text ='Озвучить', color =('#FFFFFF'), font_size ="20sp", background_color =('green'), pos =(100, 100), on_press=lambda x:
                       engine.say(a) and sleep.time(3) and print('Озвучивается'))
        self.layout.add_widget(btn15)
        a='Находится в разработке, но всё равно работает'
        
        engine = pyttsx3.init()     # инициализация движка
    
        engine.setProperty('rate', 150)     # скорость речи
        engine.setProperty('volume', 0.9)   # громкость (0-1)


        engine.runAndWait()


         
    def build(self): 
   
        # create an image a button 
        # Adding images normal.png image as button
        # decided its position and size 
        btn = Button(text ="-",
                     color =(1, 0, .65, 1),
                     background_normal = 'борщ ингридиенты.png',
                     size_hint = (.3, .3),
                     pos_hint = {"x":0.35, "y":0.3}
                   ) 
      
        return btn 
        
    def __init__(self, **kw):
        super(Borsh, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
      
        box.add_widget(Button(font_size=dp(15), color='black', background_normal = 'C:\кнопки,фотки и прочее\борщ ингридиенты.png', on_press=lambda x:
                              set_screen('recipe')))
        
        self.add_widget(box)
        
class Olive(Screen):
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        

        self.layout = GridLayout(cols=4, spacing=40, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Вернуться',
                             on_press=lambda x: set_screen('recipe'),
                             size_hint_y=None, height=dp(40))
        

        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        a='Оливье озвучка'
        btn15 = Button(text ='Озвучить', color =('#FFFFFF'), font_size ="20sp", background_color =('green'), pos =(100, 100), on_press=lambda x:
                       engine.say(a) and sleep.time(3) and print('Озвучивается'))
        self.layout.add_widget(btn15)
        
        
        engine = pyttsx3.init()     # инициализация движка
    
        engine.setProperty('rate', 150)     # скорость речи
        engine.setProperty('volume', 0.9)   # громкость (0-1)


        engine.runAndWait()


        
    def __init__(self, **kw):
        super(Olive, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
      
        box.add_widget(Button(font_size=dp(15), color='black', background_normal = 'C:\RecipeSet\кнопки,фотки и прочее\оливье.png', on_press=lambda x:
                              set_screen('recipe')))
        
        self.add_widget(box)

        
class SaladeKing(Screen):
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        

        self.layout = GridLayout(cols=5, spacing=40, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Вернуться', on_press=lambda x: set_screen('recipe'),
                            size_hint_y=None, height=dp(40))
        
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        
    def __init__(self, **kw):
         
        super(SaladeKing, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
       
        box.add_widget(Button(text='Салат Цезарь, способ приготовления:', font_size=dp(15), color='black',  background_color =('#E318FF'), on_press=lambda x:
                              set_screen('recipe')))
        
        self.add_widget(box)
        
class Omlet(Screen):
    
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        

        self.layout = GridLayout(cols=5, spacing=40, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Вернуться',
                             on_press=lambda x: set_screen('recipe'),
                             size_hint_y=None, height=dp(40))
        
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        
    def __init__(self, **kw):
        super(Omlet, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        
        box.add_widget(Button(background_normal = 'C:\кнопки,фотки и прочее\омлет ингридиенты.png', font_size=dp(15), on_press=lambda x:
                              set_screen('recipe')))
        
        self.add_widget(box)

#______________________________________________________-_-___________

class Time(Screen):
    def on_enter(self):  # Будет вызвана в момент открытия экрана
        
        self.layout = GridLayout(cols=1, spacing=40, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Вернуться',
                             on_press=lambda x: set_screen('recipe'),
                             size_hint_y=None, height=dp(40))
        
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)
        
    def __init__(self, **kw):
        super(Time, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')

        
        btn5 = Button(text = '-_-', color =('white'), font_size ="18sp", background_color =('black'), pos =(300, 250), on_press=lambda x:
                              set_screen('recipe')) 
        self.add_widget(btn5)
        

        
class AddFood(Screen):

    def buttonClicked(self, btn3):
        if not self.txt3.text:
            return
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'user_data'))
        self.app.user_data[self.txt3.text.encode('u8')] = int(time.time())

        self.app.config.set('General', 'user_data', self.app.user_data)
        self.app.config.write()
        text2 = "Таймер на " + self.txt3.text + " (минуты)"
        self.result.text = text2
        self.txt3.text = ''
        
        while text2 > 0:
            print(t)
            text2 -= 1
            time.sleep(1)
        print("ТАЙМЕР ОТКЛЮЧЕН!")
    #seconds = int(seconds)
        buttonClicked(text2*60)
        
 
    def __init__(self, **kw):
        super(AddFood, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        back_button = Button(text='< Назад в главное меню', on_press=lambda x:
                             set_screen('glavnay'), size_hint_y=None, height=dp(40))
        box.add_widget(back_button)
        self.txt3 = TextInput(text='', multiline=False, height=dp(40),
                              size_hint_y=None, hint_text="Добавить таймер(минуты)")
        box.add_widget(self.txt3)
        btn15 = Button(text="+", color='white', background_color =('green'), size_hint_y=None, height=dp(40))
        btn15.bind(on_press=self.buttonClicked)
        box.add_widget(btn15)
        self.result = Label(text='')
        box.add_widget(self.result)
        self.add_widget(box)
          #btn2 = Button(text ='Hello World ', color =('blue'), font_size ="15sp", background_color =('#1822FF'), pos =(300, 250))

                 
def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Glavnay(name='glavnay'))
sm.add_widget(AddFood(name='add_food'))
sm.add_widget(SortedListFood(name='list_food'))
sm.add_widget(Vdele(name='maksvdele'))
sm.add_widget(Sport(name='sport'))
sm.add_widget(Timer(name='timer'))
sm.add_widget(Recipe(name='recipe'))
sm.add_widget(Borsh(name='borsh'))
sm.add_widget(SaladeKing(name='salade_king'))
sm.add_widget(Blin(name='blin'))
sm.add_widget(Omlet(name='omlet'))
sm.add_widget(Olive(name='olive'))
sm.add_widget(Add(name='add'))
sm.add_widget(Time(name='time_do'))

class RecipeSet(App):
    def __init__(self, **kvargs):
        super(RecipeSet, self).__init__(**kvargs)
        self.config = ConfigParser()

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'user_data', '{}')

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'user_data'))

    def get_application_config(self):
        return super(RecipeSet, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return sm


if __name__ == '__main__':
    RecipeSet().run()
#FoodOptionsApp
