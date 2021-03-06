#!/usr/bin/env python3
#!-*- coding: utf-8 -*-
#This Programm is made with love from the IOTA-Community for the IOTA-Community. 
#


###############################################################################
# libraries
from tkinter import Tk as tk, Menu, FLAT, Label, Entry, Button, W, StringVar, ttk
from subprocess import call, Popen, PIPE
import subprocess as sp, os, getpass, sys  
import subprocess, sys, socket, pwd, os, crypt, getpass, spwd
import tkinter as tk, time, os, sys, getpass, os.path
import tkinter.simpledialog
import tkinter.ttk as ttk
from tkinter import messagebox, font, Message, Scrollbar
from functools import partial
# Needed for ping function
from queue import Queue
from ipaddress import ip_address
from threading import Thread
from subprocess import check_output
from tkinter.ttk import (Label, Entry)
from tkinter import (Tk, Button, Text, StringVar, END, Toplevel, BOTH)
import webbrowser
import tkinter as tk
from tkinter import Label 
# Check for root
#if not os.geteuid() == 0:
#    messagebox.showinfo("Raspberry Pi Authentication", "You need sudo privileges to start raspihive")
#    sys.exit("\n Only root can run this script \n")
###############################################################################
# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )

##############################################################################
##############################################################################
# start functions
#####################################Start of Window frames############################################

class mainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
        

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,  background="#0B3861")
        #self.master.geometry("600x200")

        tk.Label(self, text="Raspihive menu", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 16").grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        # For page one
        tk.Button(self, text="Update menu", bg="lightblue",  height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(PageOne)).grid(row=1, column=0, padx='30', pady='0', ipadx=3,  ipady=3)
         # For page two
        tk.Button(self, text="Install menu", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=lambda: master.switch_frame(PageTwo)).grid(row=1, column=1, padx='30', pady='20', ipadx=3,  ipady=3)
        # For page three
        tk.Button(self, text="Tools", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=lambda: master.switch_frame(PageThree)).grid(row=3, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        # For page four
        tk.Button(self, text="Help", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=lambda: master.switch_frame(PageFour)).grid(row=3, column=1, padx='30', pady='20', ipadx=3,  ipady=3)
        # For page five
        tk.Button(self, text="Node control", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=lambda: master.switch_frame(PageFive)).grid(row=2, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        
        # For page six Dashboard Access
        tk.Button(self, text="Dashboard access", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=lambda: master.switch_frame(PageSix)).grid(row=2, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        # For page seven Quit-Raspihive
        tk.Button(self, text="Quit-Raspihive", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=lambda: master.switch_frame(PageSeven)).grid(row=4, column=0, padx='30', pady='30', ipadx=3,  ipady=3)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#0B3861")
        #self.master.geometry("650x200")

        tk.Label(self, text="Update menu", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 16").grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=3, column=1, padx='30', pady='20', ipadx=3,  ipady=3)
        """
        tk.Label(self, text="Update OS").grid(row=1, column=0, padx='0', pady='0')
        tk.Button(self, text="update", command=lambda: master.switch_frame(StartPage)).grid(row=1, column=1, padx='0', pady='0')
        """
        #label1 = tk.Label(self, text = "Update OS", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "System-update", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=update_os_function)
        button1.grid(row=1, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

        button2 = tk.Button(self, text = "Packages-update", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=update_packages_function).grid(row=1, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        button3 = tk.Button(self, text = "Hornet-update", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=update_hornet_node).grid(row=2, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

        button4 = tk.Button(self, text = "Raspihive-update", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=update_raspihive).grid(row=2, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#0B3861")
        #self.master.geometry("650x200")

        tk.Label(self, text="Install menu", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 16").grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=3, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        #label1 = tk.Label(self, text = "Install Hornet-Node", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "Install Hornet", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=Hornet_install_function).grid(row=1, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

        button1u = tk.Button(self, text = "Uninstall Hornet", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=Hornet_uninstall_function).grid(row=1, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        #button2 = tk.Button(self, text = "Install Bee", bg="lightblue", height = 1,  width = 20, command=Bee_install_function).grid(row=3, column=1, padx='0', pady='0')

        button3 = tk.Button(self, text = "Install Nginx + Certbot", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=SSL_reverse_proxy_install_function).grid(row=2, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

        button4 = tk.Button(self, text = "Remove Nginx + Certbot", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=uninstall_function).grid(row=2, column=1, padx='30', pady='20', ipadx=3,  ipady=3)


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#0B3861")
        #self.master.geometry("650x200")

        tk.Label(self, text="Tools", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 16").grid(row=0, column=0, padx='0', pady='0', ipadx=3,  ipady=3)
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=2, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        #label1 = tk.Label(self, text = " Ping test ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "ping", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=Ping_function).grid(row=1, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        
        button2 = tk.Button(self, text = "mount DB - beta", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=mounthornetDBtoextDrive).grid(row=1, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        button3 = tk.Button(self, text = "SSD-fix - beta", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=fixforolderssdsuasprob).grid(row=2, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

        #b.grid(column=1,row=1,sticky=E+W)
        #root.grid_columnconfigure(1,weight=1)


class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#0B3861")
        #self.master.geometry("650x200")

        tk.Label(self, text="Help", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 16").grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=4, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        #label1 = tk.Label(self, text = " About Raspihive ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "About", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=about).grid(row=2, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

        button2 = tk.Button(self, text = "Report", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=report).grid(row=2, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        button3 = tk.Button(self, text = "Ports and FW settings", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=infopreparations).grid(row=4, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        
class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#0B3861")
        #self.master.geometry("650x200")

        tk.Label(self, text="Node control", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 16").grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=1, column=2, padx='30', pady='20', ipadx=3,  ipady=3)
        
        # For page six
        tk.Button(self, text="Hornet Node Control", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(PageSix)).grid(row=1, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        class PageSix(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master, background="#0B3861")
                #self.master.geometry("650x200")

                tk.Label(self, text="Hornet Node Control Center", bg="lightblue", height = 1,  width = 28, fg="black", font="Verdana 16").grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
                tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=5, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

                #label1 = tk.Label(self, text = " Start hornet node ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
                button1 = tk.Button(self, text = "Start HORNET ", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=start_h_function).grid(row=2, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

                button2 = tk.Button(self, text = "Stop HORNET", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=stop_h_function).grid(row=3, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

                button3 = tk.Button(self, text = "Restart HORNET", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=restart_h_function).grid(row=4, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

                button4 = tk.Button(self, text = "Check HORNET status ", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13",  command=status_h_function).grid(row=2, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

                button5 = tk.Button(self, text = "Watch the logs", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=logs_h_function).grid(row=3, column=1, padx='30', pady='20', ipadx=3,  ipady=3)
                
                label6 = tk.Label(self, text = " Remove the mainnetdb (e.g. in case of a failure): ", bg="lightblue", height = 1,  width = 40, fg="black", font="Verdana 13").grid(row=5, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
                button6 = tk.Button(self, text = "Remove the mainnnetdb", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=mainnetdb_h_function).grid(row=6, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#0B3861")
        #self.master.geometry("650x200")

        tk.Label(self, text="Dashboard-access", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 16").grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=2, column=2, padx='30', pady='20', ipadx=3,  ipady=3)

        #label1 = tk.Label(self, text = " Hornet Dashboard ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "Open dashboard", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=hornet_dashboard).grid(row=2, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

class PageSeven(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#0B3861")
        #self.master.geometry("650x200")

        tk.Label(self, text="Quit-Raspihive", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='30', pady='20', ipadx=3,  ipady=3)
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=lambda: master.switch_frame(StartPage)).grid(row=1, column=1, padx='30', pady='20', ipadx=3,  ipady=3)

        #label1 = tk.Label(self, text = " About Raspihive ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "Quit-Raspihive", bg="lightblue", height = 1,  width = 20, fg="black", font="Verdana 13", command=Close_Raspihive).grid(row=1, column=0, padx='30', pady='20', ipadx=3,  ipady=3)

#####################################End of Window frames############################################
def Time_function():
    print("Time: ", localtime)

def clock():
    t=time.strftime('%H:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='Verdanda 13')
    app.after(100,clock)         

#Functions in page one
def update_os_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()
        subprocess.Popen("sudo apt update && sudo apt -y full-upgrade && sudo apt -y autoremove",shell = True)
        #os.system('sudo apt update && sudo apt -y full-upgrade && sudo apt -y autoremove')
        while progress_bar['value'] < 100:
            progress_bar['value'] += 2
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("OS Update", "OS successfully updated")
        progress_bar.destroy()
   
def update_packages_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()
        subprocess.Popen("sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic",shell = True)
        #os.system('sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic')
        while progress_bar['value'] < 100:
            progress_bar['value'] += 2
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("Packages Update", "Packages successfully updated")
        progress_bar.destroy()

def update_hornet_node():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 2
        app.update()
        #subprocess.Popen("sudo service hornet stop && sudo apt-get update && sudo apt-get -y upgrade hornet && sudo systemctl restart hornet",shell = True)
        os.system('sudo service hornet stop && sudo apt-get update && sudo apt-get -y upgrade hornet && sudo systemctl restart hornet')
        while progress_bar['value'] < 100:
            progress_bar['value'] += 2
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("Hornet update", "Hornet Node succesfully updated")
        progress_bar.destroy()


def update_raspihive():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 2
        app.update()
        subprocess.Popen("cd /var/lib/ && sudo rm -r raspihive && sudo git clone https://github.com/Raspihive/raspihive.git /var/lib/raspihive ",shell = True) 
        #os.system('sudo rm -r raspihive && sudo git clone https://github.com/Raspihive/raspihive.git')   # #      sudo git pull https://github.com/Raspihive/raspihive.git && sudo git reset --hard origin/master
        while progress_bar['value'] < 100:
            progress_bar['value'] += 20
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("Raspihive updated", "Raspihive succesfully updated")
        progress_bar.destroy()
#

#Functions in page two
def Hornet_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 2
        app.update()
        os.system('sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic && sudo apt update && sudo apt -y upgrade && sudo wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add -  && sudo echo "deb http://ppa.hornet.zone stable main" >> /etc/apt/sources.list.d/hornet.list && sudo apt update && sudo apt install hornet && sudo systemctl enable hornet.service && sudo apt-get install -y ufw && sudo ufw allow 15600/tcp && sudo ufw allow 14626/udp && sudo ufw limit openssh && sudo ufw enable && sudo apt-get install sshguard -y && sudo service hornet start')
        while progress_bar['value'] < 100:
            progress_bar['value'] += 2
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("Hornet installer", "Hornet Node succesfully installed")
        progress_bar.destroy()

def Hornet_uninstall_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 2
        app.update()
        os.system('sudo systemctl stop hornet && sudo apt -qq purge hornet -y && sudo rm -rf /etc/apt/sources.list.d/hornet.list')
        while progress_bar['value'] < 100:
            progress_bar['value'] += 2
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("Hornet installer", "Hornet Node succesfully uninstalled")
        progress_bar.destroy()


#def Bee_install_function():
#    if os.geteuid() != 0:
#        print("You need to have root privileges")  
#        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
#        sys.exit
#    messagebox.showinfo("Bee node installer", "Bee node - coming soon ;) ")


def SSL_reverse_proxy_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()
        os.system('sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get install -y nginx && sudo ufw allow "Nginx Full" && sudo apt-get install -y apache2-utils && sudo htpasswd -c /etc/nginx/.htpasswd Raspihive')
        # Nginx configuration
        f = open("/etc/nginx/sites-available/default", "w")
        f.write("server { \n listen 80 default_server; \n listen [::]:80 default_server; \n server_tokens off;  \n server_name _; \n location /node { \n proxy_pass http://127.0.0.1:14265/; \n } \n \n location /ws {   \n proxy_pass http://127.0.0.1:8081/ws; \n proxy_http_version 1.1; \n proxy_set_header Upgrade $http_upgrade; \n proxy_set_header Connection "'"upgrade"'"; \n proxy_read_timeout 86400; \n } \n \n location / { \n proxy_pass http://127.0.0.1:8081; \n auth_basic “Dashboard”; \n  auth_basic_user_file /etc/nginx/.htpasswd;  } \n } \n")
        f.close()
        os.system('sudo systemctl start nginx && sudo systemctl enable nginx')
        os.system('sudo apt install software-properties-common -y && sudo apt update && sudo apt install certbot python3-certbot-nginx -y')
        
        while progress_bar['value'] < 100:
            progress_bar['value'] += 20
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("Installer", "Nginx RP and Certbot successfully installed")
        progress_bar.destroy()

#Test-Remove-Function
def uninstall_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()
        os.system('sudo systemctl stop nginx && sudo systemctl disable nginx && sudo apt -qq purge software-properties-common certbot python3-certbot-nginx -y && sudo apt-get purge -y nginx ')
        while progress_bar['value'] < 100:
            progress_bar['value'] += 20
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
            #End progress bar loop
        messagebox.showinfo("Hornet installer", "Successfully removed Nginx & Certbot")
        progress_bar.destroy()


#Functions in page three

# Start of Ping function
def Ping_function():

    def validate_ip(ip):
        """
        Validate an ip address
        if the address is a valid ipv4 or ipv6 address
        the functions returns True, otherwise
        it returns False
        """
        try:
            ip_address(ip)
        except:
            return False
        else:
            return True
 
    class Showinfo(Toplevel):
        """
        Spawns a new Toplevel window.
        """
        def __init__(self, *, title, msg, width, height):
            super().__init__(width=width, height=height)
            self.title(title)
            Label(self, text=msg).pack(fill=BOTH)
            Button(self, text="Ok", command=self.destroy).pack(fill=BOTH)
 
    class App(Tk):
        def __init__(self):
            super().__init__()
            self.title('My Ping GUI')
            self.geometry('250x250')
            self.ping_active = False
            self.validation_queue = Queue()
            self.validation_loop()
            self.ip = StringVar(self)
            self.ip.trace_add("write", self.validate)
            self.setup()

        def setup(self):
            Label(self, text="Enter target IP or host as required.").pack()
            Entry(self, textvariable=self.ip).pack()
            ping_button = Button(self, text="Ping Test", command=self.ping)
            ping_button.pack()
            self.ping_button = ping_button
            self.textbox = Text(self, width=150, height=10)
            self.textbox.pack(fill=BOTH)
            Button(self, text="Exit", command=self.destroy).pack()
 
        def validate(self, *args):
            self.validation_queue.put(self.ip.get())
 
        def validation_loop(self):
            self._validation_loop = Thread(target=self._validation_worker, daemon=True)
            self._validation_loop.start()
 
        def set_ping_color(self, color):
            self.ping_button['activebackground'] = color
            self.ping_button['bg'] = color
            self.ping_button['highlightbackground'] = color
 
        def _validation_worker(self):
            while True:
                ip_or_host = self.validation_queue.get()
                is_ip = validate_ip(ip_or_host)
                if is_ip:
                    self.set_ping_color("green")
                else:
                    self.set_ping_color("red")
                # is useful if you want to join a queu
                # then join blocks, until all tasks are done
                self.validation_queue.task_done()
 
        def ping(self):
            if not self.ping_active:
                self.ping_active = True
                self.textbox.delete(1.0, END)
                ip = self.ip.get()
                thread = Thread(target=self.ping_thread)
                thread.start()
 
        def ping_thread(self):
            # code tested on linux
            # ping on windows has different options
            stdout = check_output(['ping', '-c', '3', self.ip.get()], encoding="utf8")
            # print(stdout)
            self.textbox.insert(END, stdout)
            Showinfo(title='Results', msg=stdout, width=200, height=100)
            self.ping_active = False
 
    App().mainloop()
# End of Ping function

#Test mount hornet DB to external SSD 
def mounthornetDBtoextDrive():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        subprocess.Popen('sudo mkdir /media/hornetdb && sudo mount /dev/sdb1 /media/hornetdb && sudo chmod 775 /media/hornetdb && sudo echo "/dev/sdb1 /media/hornetdb ext4 defaults  1 1" >> /etc/fstab && sudo cp -fr --preserve /var/lib/hornet/mainnetdb /media/hornetdb/ && sudo mv var/lib/hornet/mainnetdb /var/lib/hornet/mainnetdb.old && sudo ln -sf /media/hornetdb /var/lib/hornet/mainnetdb',shell = True)
        #os.system('sudo mkdir /media/hornetdb && sudo mount /dev/sdb1 /media/hornetdb && sudo chmod 775 /media/hornetdb && sudo echo "/dev/sdb1 /media/hornetdb ext4 defaults  1 1" >> /etc/fstab && sudo cp -fr --preserve /var/lib/hornet/mainnetdb /media/hornetdb/ && sudo mv var/lib/hornet/mainnetdb /var/lib/hornet/mainnetdb.old && sudo ln -sf /media/hornetdb /var/lib/hornet/mainnetdb')
        messagebox.showinfo("Mount-DB", "Hornet mainnetdb successfully mounted ")


def fixforolderssdsuasprob():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        subprocess.Popen('sudo echo -e "blacklist uas \n blacklist sg" > /etc/modprobe.d/disable_uas.conf',shell = True)
        #os.system('sudo echo -e "blacklist uas \n blacklist sg" > /etc/modprobe.d/disable_uas.conf')
        messagebox.showinfo("SSD fix", "SSD fix executed ")

#Functions in page four
def report():
    if (screen_width*screen_height<=614400): # 7 inch Display = Fullscreen
        messageWindow = tk.Tk()
        messageWindow.geometry("600x210+350+250")
        messageWindow.title("Report") 
        messageWindow['bg'] = '#0B3861'
        Label(messageWindow, text="If you found a bug or experience any issues, please write as at:", bg="#0B3861", fg="white", font="Verdana 13").grid(row=0, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=1, column=0, padx='0', pady='0')

        Link = Button(messageWindow, text = "https://raspihive.org/", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = report_raspihive).grid(sticky="W")
        #link1 = Label(messageWindow, text="https://raspihive.org/", fg="blue", cursor="hand2", font="Verdana 13")
        #link1.grid(row=1, column=0, padx='0', pady='0')
        #link1.bind("<Button-1>", lambda e: callback("https://raspihive.org/"))

        #Label(messageWindow, text="https://raspihive.org/", bg="#0B3861", fg="white", font="Verdana 13").grid(row=2, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
        
        Label(messageWindow, text="Thanks for your feedback!", bg="#0B3861", fg="white", font="Verdana 13").grid(row=4, column=0, padx='0', pady='0')

        B = Button(messageWindow, text = "Quit-window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = messageWindow.destroy).grid(sticky="W")
        messageWindow.mainloop()
        
    if (screen_width*screen_height<=2073600): # > 7 inch Display no Fullscreen
        messageWindow = tk.Tk()
        messageWindow.geometry("600x210+350+250")
        messageWindow.title("Report") 
        messageWindow['bg'] = '#0B3861'
        Label(messageWindow, text="If you found a bug or experience any issues, please write as at:", bg="#0B3861", fg="white", font="Verdana 13").grid(row=0, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=1, column=0, padx='0', pady='0')

        Link = Button(messageWindow, text = "https://raspihive.org/", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = report_raspihive).grid(sticky="W")

        #link1 = Label(messageWindow, text="https://raspihive.org/", fg="blue", cursor="hand2", font="Verdana 13")
        #link1.grid(row=1, column=0, padx='0', pady='0')
        #link1.bind("<Button-1>", lambda e: callback("https://raspihive.org/"))

        #Label(messageWindow, text="https://raspihive.org/", bg="#0B3861", fg="white", font="Verdana 13").grid(row=2, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
        
        Label(messageWindow, text="Thanks for your feedback!", bg="#0B3861", fg="white", font="Verdana 13").grid(row=4, column=0, padx='0', pady='0')

        B = Button(messageWindow, text = "Quit-window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = messageWindow.destroy).grid(sticky="W")
        messageWindow.mainloop()
        
    #messagebox.showinfo("About", " If you found a bug or experience any issues, please write as at: https://raspihive.org/")


def about():
    if (screen_width*screen_height<=614400): # 7 inch Display = Fullscreen
        messageWindow = tk.Tk()
        messageWindow.geometry("600x210+350+250")
        messageWindow.title("About") 
        messageWindow['bg'] = '#0B3861'
        Label(messageWindow, text="The Plug and Play solution for a Raspberry Pi IOTA Fullnode!", bg="#0B3861", fg="white", font="Verdana 13").grid(row=0, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=1, column=0, padx='0', pady='0')
        Label(messageWindow, text="Raspihive: Version 1.0", bg="#0B3861", fg="white", font="Verdana 13").grid(row=2, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
        
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=4, column=0, padx='0', pady='0')

        B = Button(messageWindow, text = "Quit-window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = messageWindow.destroy).grid(sticky="W")
        messageWindow.mainloop()
        
    if (screen_width*screen_height<=2073600): # > 7 inch Display no Fullscreen
        messageWindow = tk.Tk()
        messageWindow.geometry("600x210+350+250")
        messageWindow.title("About") 
        messageWindow['bg'] = '#0B3861'
        Label(messageWindow, text="The Plug and Play solution for a Raspberry Pi IOTA Fullnode!", bg="#0B3861", fg="white", font="Verdana 13").grid(row=0, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=1, column=0, padx='0', pady='0')
        Label(messageWindow, text="Raspihive: Version 1.0", bg="#0B3861", fg="white", font="Verdana 13").grid(row=2, column=0, padx='0', pady='0')
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
        
        Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=4, column=0, padx='0', pady='0')

        B = Button(messageWindow, text = "Quit-window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = messageWindow.destroy).grid(sticky="W")
        messageWindow.mainloop()
    #info for user display message
    #messagebox.showinfo("Report a bug", " The Plug and Play solution for a Raspberry Pi IOTA Fullnode with userfriendly UI and extensions \n Raspihive: Beta Version 3.0 ")


def infopreparations():
    if (screen_width*screen_height<=614400): # 7 inch Display = Fullscreen
        messageWindow = tk.Tk()
        messageWindow.geometry("600x280+350+250")
        messageWindow.title("Preparations") 
        messageWindow['bg'] = '#0B3861'
        Label(messageWindow, text="The following ports are important for a flawless node operation.  ", bg="#0B3861", fg="white", font="Verdana 13").grid(row=0, column=0, padx='0', pady='0')
        Label(messageWindow, text="Allow basic ports in your router settings: \n", bg="#0B3861", fg="white", font="Verdana 13").grid(row=1, column=0, padx='0', pady='0')
        Label(messageWindow, text="14626 UDP - Autopeering port \n \n 15600 TCP - Gossip (neighbors) port \n \n 80 TCP - for Certbot \n \n 443 TCP for Certbot", bg="#0B3861", fg="white", font="Verdana 13").grid(row=2, column=0, padx='0', pady='0')
        #Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
        
        #Label(messageWindow, text="Thanks for your feedback!", bg="#0B3861", fg="white").grid(row=4, column=0, padx='0', pady='0')
        B = Button(messageWindow, text = "Quit-window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = messageWindow.destroy).grid(sticky="W")
        messageWindow.mainloop()
        
    if (screen_width*screen_height<=2073600): # > 7 inch Display no Fullscreen
        messageWindow = tk.Tk()
        messageWindow.geometry("600x280+350+250")
        messageWindow.title("Preparations") 
        messageWindow['bg'] = '#0B3861'
        Label(messageWindow, text="The following ports are important for a flawless node operation.  ", bg="#0B3861", fg="white", font="Verdana 13").grid(row=0, column=0, padx='0', pady='0')
        Label(messageWindow, text="Allow basic ports in your router settings: \n", bg="#0B3861", fg="white", font="Verdana 13").grid(row=1, column=0, padx='0', pady='0')
        Label(messageWindow, text="14626 UDP - Autopeering port \n \n 15600 TCP - Gossip (neighbors) port \n \n 80 TCP - for Certbot \n \n 443 TCP for Certbot", bg="#0B3861", fg="white", font="Verdana 13").grid(row=2, column=0, padx='0', pady='0')
        #Label(messageWindow, text="", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
        
        #Label(messageWindow, text="Thanks for your feedback!", bg="#0B3861", fg="white").grid(row=4, column=0, padx='0', pady='0')

        B = Button(messageWindow, text = "Quit-window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = messageWindow.destroy).grid(sticky="W")
        messageWindow.mainloop()
    #info for user display message
    #messagebox.showinfo("Preparations", "Allow basic ports in your router settings. The following ports are important for a flawless node operation. \n \n 14626 UDP - Autopeering port \n \n 15600 TCP - Gossip (neighbors) port \n \n 80 TCP - for Certbot \n \n 443 TCP for Certbot ")

#Functions in page five
#
def start_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        subprocess.Popen('sudo service hornet start',shell = True)
        #os.system('sudo service hornet start')
        messagebox.showinfo("Hornet", "Hornet node started ")

def stop_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        subprocess.Popen('sudo service hornet stop',shell = True)
        #os.system('sudo service hornet stop')
        messagebox.showinfo(" Hornet", "Hornet node stopped  ")

def restart_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        subprocess.Popen('sudo service hornet restart',shell = True)
        #os.system('sudo service hornet restart')
        messagebox.showinfo(" Hornet", "Hornet node restarted ")

def status_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        # For hornet node status
        Outputfileobject=os.popen("sudo service hornet status")    
        Output=Outputfileobject.read()
        Outputfileobject.close()
        #Gui log for hornet node status
        root = tk.Tk()
        root.title("Hornet Node Status")
        #Test Screen Resolution
        screen_width = app.winfo_screenwidth()
        #print("width: ",screen_width)
        screen_height = app.winfo_screenheight()
        #Label(root, text="Ausschalten Test", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
       
        B = Button(root, text = "Quit-status window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13", command = root.destroy).grid(sticky="W")
        Text=Label(root,text=Output, bg="#0B3861", fg="white").grid()
        root.mainloop()
        #End of Gui log for hornet node status

def logs_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        # For hornet node status
        Outputfileobject=os.popen("sudo journalctl -u hornet -n 50 ")    
        Output=Outputfileobject.read()
        Outputfileobject.close()
        #Gui log for hornet node status
        root = tk.Tk()
        root.title("Hornet Node Logs")
        #Test Screen Resolution
        screen_width = app.winfo_screenwidth()
        #print("width: ",screen_width)
        screen_height = app.winfo_screenheight()
        #Label(root, text="Ausschalten Test", bg="#0B3861", fg="white").grid(row=3, column=0, padx='0', pady='0')
       
        B = Button(root, text = "Quit-Log window", bg="#0B3861", height = 1,  width = 20, fg="white", font="Verdana 13",  command = root.destroy).grid(sticky="W")
        Text=Label(root,text=Output, bg="#0B3861", fg="white").grid()
        root.mainloop()
        #End of Gui log for hornet node status

        

def mainnetdb_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    if os.geteuid()==0:
        subprocess.Popen('sudo service hornet stop && sudo rm -r /var/lib/hornet/mainnetdb && sudo service hornet start',shell = True)
        #os.system('sudo service hornet stop && sudo rm -r /var/lib/hornet/mainnetdb && sudo service hornet start')
        messagebox.showinfo(" Hornet", " Hornet DB removed  ")
#
def hornet_dashboard():
    #os.system('sudo -upi chromium http://localhost')
    #os.system('firefox-esr https://google.at')
    #webbrowser.get('chromium').open('https://www.google.com')
    #webbrowser.open('sudo -upi chromium https://google.at')
    #os.system('firefox-esr --no-sandbox --disable-infobars --start-maximized --noerrdialogs --kiosk --incognito http://google.at')
    #os.system('chromium --no-sandbox http://google.at')
    #subprocess.Popen(" chromium --no-sandbox /new-tab www.google.com",shell = True)
    subprocess.Popen("sudo -upi chromium http://localhost",shell = True)
    subprocess.Popen("sudo -uubuntu firefox http://localhost",shell = True)
    subprocess.Popen("sudo -ubeekeeper firefox http://localhost",shell = True)

def report_raspihive():
    #webbrowser.open_new(url)
    subprocess.Popen("sudo -upi chromium https://raspihive.org/",shell = True)
    subprocess.Popen("sudo -uubuntu firefox https://raspihive.org/",shell = True)
    subprocess.Popen("sudo -ubeekeeper firefox https://raspihive.org/",shell = True)
   

def Close_Raspihive():
    sys.exit(0)


###############################################################################
# end functions
###############################################################################
###############################################################################
# Start main programm
###############################################################################
#
if __name__ == "__main__":
    app = mainWindow()
    #Test Screen Resolution
    screen_width = app.winfo_screenwidth()
    #print("width: ",screen_width)
    screen_height = app.winfo_screenheight()
    #print("height: ", screen_height)
    if (screen_width*screen_height<=614400): # 7 inch Display = Fullscreen
        app.geometry("%dx%d+0+0" % (screen_width, screen_height))
    else: 
        (screen_width*screen_height<=2073600) # > 7 inch Display no Fullscreen
        app.geometry("820x520+350+150") #BxH+B+H
        print("")


    #app.option_add('*Font', 'Arial 16')
    app.title("Raspihive")
    
    # use the next line if you also want to get rid of the titlebar
    #app.overrideredirect(1)   
        
    #app.configure(bg='white')  
    app['bg'] = '#0B3861'
    

    #app.grid(row=0, column=0, sticky="nsew")
    #app.grid(row=0, column=1, sticky="nsew")

    #app.grid_columnconfigure(0, weight=1)
    #app.grid_rowconfigure(0, weight=1)
    #app.grid_columnconfigure(1, weight=1)
    #"-sticky": must be -minsize, -pad, -uniform, or -weight
    

    # Label for Clock
    label1=Label(app)
    label1.grid(row=0, column=1, padx='40', pady='0')
    clock()


   


    app.mainloop()
###############################################################################
#End main programm