#Static class for handling key presses
class KeyPressHandler():
    keyActionDict = {}

    #Register a key with a callback function
    @staticmethod
    def RegisterKey(key, callback):
        KeyPressHandler.keyActionDict[key] = callback

    #Call the appropriate function for the key if it has been registered
    def __call__(self, event):  
        if(KeyPressHandler.keyActionDict.has_key(event.key)):
            KeyPressHandler.keyActionDict[event.key]()

"""Example of use:

#Setup callback for key press
KeyPressHandler.RegisterKey ('escape', exit);
pathPlotFigure.canvas.mpl_connect('key_press_event', KeyPressHandler())
"""
