# Created By: Usman Mahmood
# File Name: calculator.py

# Required Imports for the Program
from gtts import gTTS
import speech_recognition as sr
import pyttsx3
import os
import math

# Establishes the Microphone
r = sr.Recognizer()

# Converting the Text into Speech
def SpeakText(command):
    engine = pyttsx3.init("sapi5", False)
    engine.say(command)
    engine.runAndWait()
    
# Converting the String 
def StrToList(arg):
    str_list = list(arg.split(" "))
    return str_list

def Operation(arg):
    dup_ary1 = arg
    
    x = True
    while(x):
        for val in range(len(dup_ary1)):
            if (dup_ary1[val] == "^" or dup_ary1[val] == "√"):
                if (dup_ary1[val] == "^"):
                    new_val = float(dup_ary1[(val-1)]) ** float(dup_ary1[(val+1)])
                    new_val_str = str(new_val)
                    dup_ary1[val] = new_val_str
                    dup_ary1.pop(val-1)
                    dup_ary1.pop(val)
                    break
                
                elif (dup_ary1[val] == "√"):
                    new_val = math.sqrt(float(dup_ary1[(val+1)]))
                    new_val_str = str(new_val)
                    dup_ary1[val] = new_val_str
                    dup_ary1.pop(val+1)
                    break
                    
            if (("^" not in dup_ary1) and ("√" not in dup_ary1)):
                x = False
                
    x = True
    while(x):
        for val in range(len(dup_ary1)):
            if (dup_ary1[val] == "*" or dup_ary1[val] == "/"):
                if (dup_ary1[val] == "*"):
                    new_val = float(dup_ary1[(val-1)]) * float(dup_ary1[(val+1)])
                    new_val_str = str(new_val)
                    dup_ary1[val] = new_val_str
                    dup_ary1.pop(val-1)
                    dup_ary1.pop(val)
                    break
                
                elif (dup_ary1[val] == "/"):
                    new_val = float(dup_ary1[(val-1)]) / float(dup_ary1[(val+1)])
                    new_val_str = str(new_val)
                    dup_ary1[val] = new_val_str
                    dup_ary1.pop(val-1)
                    dup_ary1.pop(val)
                    break
                    
            if (("*" not in dup_ary1) and ("/" not in dup_ary1)):
                x = False
    
    x = True       
    while(x):     
        for val in range(len(dup_ary1)):
            if (dup_ary1[val] == "+" or dup_ary1[val] == "-"):  
                if (dup_ary1[val] == "+"):
                    new_val = float(dup_ary1[(val-1)]) + float(dup_ary1[(val+1)])
                    new_val_str = str(new_val)
                    dup_ary1[val] = new_val_str
                    dup_ary1.pop(val-1)
                    dup_ary1.pop(val)
                    val = 0
                    break
                
                elif (dup_ary1[val] == "-"):
                    new_val = float(dup_ary1[(val-1)]) - float(dup_ary1[(val+1)])
                    new_val_str = str(new_val)
                    dup_ary1[val] = new_val_str
                    dup_ary1.pop(val-1)
                    dup_ary1.pop(val)
                    val = 0
                    break
                
            if (("+" not in dup_ary1) and ("-" not in dup_ary1)):
                x = False
                    
    print(dup_ary1)
    return arg

print("<-- Welcome to the Calculator -->")
print("When ready, speak out the calcultion to be made.")
print("For example: 2 * 2, 3 * 2 + 1, or 4 / 2 + 8")
choice = input("Are you ready (Y or N): ")
print("")

if ((choice == 'Y') or (choice == 'y')):
    condition = True  
    while(condition):
        print("Please ask away:")
        try:
            with sr.Microphone() as src2:
                r.adjust_for_ambient_noise(src2, duration=0.2)
                audio2 = r.listen(src2)
                myText = r.recognize_google(audio2)
                myText = myText.lower()
                
                text = "Did you say: " + myText
                print(text)
                SpeakText(text)
                choice2 = input("Yes (Y) or No (N): ")
                if ((choice2 == 'Y') or (choice2 == 'y')):
                    condition = False
                else:
                    print("Please Try Again")
                
        except sr.RequestError as e:
            print("Unable to request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("An unknown error occured")
        
    str_array = StrToList(myText)
    print(str_array)
    answer = Operation(str_array)
    main_ans = answer[0]
    
    testtext = "The answer is: "
    appneded = str(main_ans)
    final_text = testtext + appneded
    print(final_text)
    SpeakText(final_text)

else:
    print("Okay, bye I guess ...")
