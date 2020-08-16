from win32com.client import Dispatch
from datetime import datetime
from time import time


#Speak Function
def jarvis(str,stop_input):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    while True:
        user = input("Enter:")
        if user == stop_input:
            break

#My log function 
def my_log(messege):
    with open("logList.txt","a") as f:
        f.write(f"{messege} {datetime.now()}\n")
            

if __name__ == "__main__":
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak("Hi I am Jarvis. I am a health reminder system of bappy sir")

    
    #For getting seconds
    init_water = time()
    init_eyes = time()
    init_ex = time()
    
    #Setting the actual times
    water_sec = 40*60
    eyes_sec = 50*60
    ex_sec = 60*60

    while True:
        if time() - init_water > water_sec:
            print("Write 'd' to log water.")
            jarvis("Hello Bappy sir. You have passed 40 minutes so you have to drink water now. Please drink water","d")
            
            init_water = time()
            my_log("Drank water at")
            
            

        if time() - init_eyes > eyes_sec:
            print("Write 'e' to log eyes.")
            jarvis("Hello Bappy sir. You have passed 50 minutes so you have to relax your eyes now. Please relax your eyes","e")
            
            init_eyes = time()
            my_log("Relaxed eyes at")
            

        if time() - init_ex > ex_sec:
            print("Write 'ex' to log exercise.")
            jarvis("Hello Bappy sir. You have passed 1 hour so you have to do exercise now. Please do exercise","ex")
            
            init_ex = time()
            my_log("Did exercise at")
            

    
    




    

        

       

    
    

    
    
        
        
#     print("Ok sir!")

   




        
