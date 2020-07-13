###############################################################################
# libraries
from guizero import App, Window, Combo, Text, TextBox, CheckBox, ButtonGroup, PushButton, info, Picture, Box, MenuBar, yesno
import tkinter, time, subprocess, os, sys, getpass, os.path
###############################################################################

# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )
###############################################################################
# start functions

def file_function():
    print("Update Raspberry Pi")
    subprocess.call('echo  | sudo apt update && sudo apt full-upgrade', shell=True)
    print("Raspberry Pi updated - OK")

def file_function2():
    print("Update packages")
    os.system("sudo apt install -y build-essential")
    os.system("sudo apt install -y git")
    os.system("sudo apt install -y snapd")
    os.system("sudo snap install -y go --classic")
    print("Packages updated - OK")

def Hornet_function():
    print("Hornet option")
    dirname = os.environ['HOME'] + "/test"
    os.makedirs(dirname)
    #os.system("sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.1/HORNET-0.4.1_Linux_x86_64.tar.gz -P /home/paul/test/")
    #os.system("sudo chown paul:paul /home/paul/test/HORNET-0.4.1_Linux_x86_64.tar.gz")
    #os.system("sudo tar -xf /home/paul/test/HORNET-0.4.1_Linux_x86_64.tar.gz")
    #os.system("sudo chown paul:paul -R /home/paul/test/HORNET-0.4.1_Linux_x86_64")
    #os.chmod('/home/paul/test/HORNET-0.4.1_Linux_x86_64.tar.gz', 0o755)
    os.system("sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.1/HORNET-0.4.1_Linux_x86_64.tar.gz -P /home/pi/test")
    os.system("sudo chown pi:pi /home/pi/test/HORNET-0.4.1_Linux_x86_64.tar.gz")
    os.system("sudo tar -xzf /home/pi/test/HORNET-0.4.1_Linux_x86_64.tar.gz -C /home/pi/test/")
    os.system("sudo chown pi:pi -R /home/pi/test/HORNET-0.4.1_Linux_x86_64")
    print("Hornet Node successfully installed")


def GoShimmer_function():
    #username = getpass.getuser()
    dirname = os.environ['HOME'] + "/goshimmer"
    os.makedirs(dirname)
    #os.system("sudo mkdir goshimmer ")
    print("GoShimmer Node successfully installed")

def Ping_function():
    print("Ping")
    process = subprocess.Popen(['ping', '-c 3', 'www.google.com'], 
    stdout=subprocess.PIPE,
    universal_newlines=True)
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            break

def Time_function():
    print("Time: ")
    text.value = ("Local time is:", localtime)
    

def entertext():
    displaytext.value = gettext.value
    print(displaytext.value)

# Ask the user if they really want to close the window
def do_this_when_closed():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()

###############################################################################
# end functions


###############################################################################
# Start main programm - App-Anfang grid = Spalten und Zeilen

app = App(title="Raspihive", bg = (235, 215, 182), width=320, height=480, layout="grid")
text = Text(app, text="", size=16, font="Times New Roman", color="black", grid=[2,0], align="top")
#app.title = ("A different title")

menubar = MenuBar(app,
                  toplevel=["Auswahl", "Node installer", "Tools"],
                  options=[
                      [ ["Update Raspberry Pi", file_function], ["Update packages", file_function2] ],
                      [ ["Install Hornet Node", Hornet_function], ["Install GoShimmer", GoShimmer_function] ],
                      [ ["Ping", Ping_function], ["Show system time", Time_function] ]
                  ])




# insert logo here
#picture1 = Picture(app, image="/home/paul/Dokumente/Raspihive-Projekt-akt/Python_Codeschnipsel/iota.gif", grid=[0,0])


displaytext = Text(app, text="Welcome to Raspihive", size=12, font="Times New Roman", color="black", grid=[0,0])
gettext = TextBox(app, width=10, grid=[2,0])
update_text = PushButton(app, command=entertext, text="enter", grid=[6,0])











# When the user tries to close the window, run the function do_this_when_closed()
app.when_closed = do_this_when_closed

app.display()
###############################################################################
# End main programm 