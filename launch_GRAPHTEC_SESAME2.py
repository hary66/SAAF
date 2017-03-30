# python3

#Lance GRAPHTEC & SESAME

import subprocess, pyautogui, time

#subprocess.Popen([r"cmd"])

parametres = '23.5 2 47 73 7.8'
parametres = pyautogui.prompt(text='Entrer 5 paramètres ou confirmez', title='Lancement SESAME' , default=parametres)



subprocess.Popen([r"C:\Program Files (x86)\Graphtec\GL100_240_840-APS\GL100_240_840-APS.exe"])

print("GRAPHTEC se lance")
#time.sleep(4)

##while pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Start_the_standard_mode.png') == None:
##    print('attente1')
##    time.sleep(0.5)

##while pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Start_the_standard_mode.png') != None:
##    print("GRAPHTEC démarre")
    
while pyautogui.locateOnScreen(r"C:\Users\Harold\Documents\Reine\Python\not_connected.png") ==None: #wait until the nice window to come
    print("waiting until the nice window to come to click on the right button !")
    time.sleep(9)
    
if pyautogui.locateOnScreen(r"C:\Users\Harold\Documents\Reine\Python\not_connected.png") !=None:
    print("GRAPHTEC en attente de connection")
    pyautogui.press('f5')
while pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\a_connecter.PNG')  ==None:
    print("GRAPHTEC connexion en cours")
    time.sleep(0.5)
    

connect_button = pyautogui.locateCenterOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Connect_F5.png')
if connect_button != None:
    pyautogui.click(connect_button)

while pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Connected.PNG') ==None:
    print("GRAPHTEC pas encore connecté, mais bientot !")
    time.sleep(0.25)

if pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Connected.PNG') !=None:
    print("GRAPHTEC connecté")
    pyautogui.click(pyautogui.locateCenterOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Close.PNG'))

while pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Start.png') ==None:
    time.sleep(1)

Start_png = pyautogui.locateCenterOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Start.png')
#print (Start_png)
pyautogui.click(Start_png)
print('Lancement de l\'enregistrement du GRAPHTEC')
#print('Clické sur Start.png')

confirmation_enregistrement_en_cours_R = pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Recording_R.png')
confirmation_enregistrement_en_cours_B = pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Recording_B.png')
while (pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Recording_R.png')) == None:
#while ((pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Recording_R.png')) || (pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Recording_B.png'))) ==None:
    time.sleep(0.25)
if pyautogui.locateOnScreen(r'C:\Users\Harold\Documents\Reine\Python\Recording_R.png') != None:
    print('Enregistrement GRAPHTEC en cours')    

parabox = pyautogui.confirm(text=parametres, title='Confirmez vous les parametres SESAME', buttons=['OK', 'Cancel'])
print (parabox)

if parabox =="OK":
    print('Lancement du SESAME avec les paramètres suivant : ' + parametres)
    subprocess.check_output(['c:\Program Files (x86)\EGSesameTriangle\Debug\EGSesameTriangle.exe', '23.5', '0.25', '47', '73', '7.8'])
elif parabox == 'Cancel':
    print("Arretez tout !")
