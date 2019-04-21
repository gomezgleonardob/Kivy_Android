
#Importamos Componentes de Kivy
import os
os.environ['KIVY_GL_BACKEND'] = 'agdl_sdl2'
from kivy.app import App
from kivy.uix.button import Button

#Definimos la clase
class MyApp(App):
    #Funcion
    def build(self):
        return Button(text='Hello World')

if __name__ in ('__android__', '__main__'):
#Corremos nuestra aplicacion
    MyApp().run()