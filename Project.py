import pynput
import smtplib
 

from pynput.keyboard import Key, Listener


def user_input(key):
    print(key)
    
def display_type(key):
    #Stopping the program
    if key == Key.esc:
        return False
    
    
    

#Using the listener I will take in two agruments
#One argument will be used to detect what the user types while the other argument will display what the user types
with Listener(user_input, display_type) as listener:
    #I will create a loop to check when the keys are pressed 
    listener.join()
    
