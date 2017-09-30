import pygame, sys, os
def fIn(strSymb):
    #X / T / C / R / S / SP
    global strLogin
    global lvl    
    strLogin = strLogin + strSymb
    if (strSymb == "S"):
        strLogin=""
        lvl = ""
        os.system('clear')
    elif(strSymb =="SP"):
        if (strLogin == strD):
            lvl = "0;"            
            dfMenu.print_menu(lvl)
        else:
            os.system("sudo shutdown -h now")
            #print("SHUT")
    else:
        lvl = ""        
        if (len(strLogin) < 4):        
            #strLogin[3]=strSymb
            strLogin = strLogin + strSymb
            os.system('clear')
            print(5 * '\n')
            print(10* ' ' + strLogin)
