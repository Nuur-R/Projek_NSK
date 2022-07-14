import eel
import os

@eel.expose
def hello():
    print("Hello from Python")
    
eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/GUI')
eel.start("main.html")