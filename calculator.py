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
    
# Converting the String w/ Numerical Values Only 
def StrToList(arg):
    str_list = list(arg.split(" "))
    return_ary = []
    for item in range(len(str_list)):
        text = str(str_list[item])
        if((text.isdigit()) or (text == '^') or (text == '√') or (text == '*') or (text == '/') or (text == '+') or (text == '-') or (text == '/') ):
            return_ary.append(str_list[item])
    return return_ary

# Function to Perform the Calculation
def Operation(arg):
    dup_ary1 = arg
    
    # Performing the Simple Exponent Functions
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
    
    # Performing the Multiple or Division     
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
    
    # Performing the Addition and Subtraction
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

# The main code starts here:
text = ("<-- Welcome to the Calculator -->")
text0 = ("Welcome to the Calculator")
text2 = ("When ready, speak out the calculation to be made.")
text3 = ("For example: 2 * 2, 3 * 2 + 1, or 4 / 2 + 8")
print(text)
SpeakText(text0)
print(text2)
SpeakText(text2)
print(text3)
SpeakText(text3)
text4 = "Are you ready (Y or N): "
SpeakText(text4)
choice = input("Are you ready (Y or N): ")

print("")

if ((choice == 'Y') or (choice == 'y')):
    condition = True  
    while(condition):
        text5 = ("Please ask away:")
        print(text5)
        SpeakText(text5)
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
                    text6 = "Please Try Again"
                    print(text6)
                    SpeakText(text6)
                
        except sr.RequestError as e:
            print("Unable to request results; {0}".format(e))
            
        except sr.UnknownValueError:
            text7 = "An unknown error occured"
            print(text7)
            SpeakText(text7)
        
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
