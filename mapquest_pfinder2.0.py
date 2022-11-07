# MapQuest Pathfinder 2.0 | by Group 8 - 4ITI

from enum import auto
import urllib.parse
import requests
import colorama
from tkinter import *
from tkinter import messagebox
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# API
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "PJv71zxlt65ihzFpAKRuP6HQ3zaCJDQ9"

# GUI Settings
window = Tk()
window.title("MapQuest Pathfinder 2.0")
window.geometry("400x300")
window.resizable(False, False)

global orig, dest
orig = StringVar()
dest = StringVar()

def getInput():
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig.get(), "to":dest.get()})
    # Get json data request
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    # Output if successful json route call
    if json_status == 0:
        print(Fore.GREEN + "API Status " + str(json_status) + " = Congratulations! A successful route call.\n")

        lbl_intro.grid(row=4, column=0, padx=5, pady=10, sticky=W)
        btn_choice1.grid(row=5, column=0, padx=5, pady=5, sticky=W)
        btn_choice2.grid(row=7, column=0, padx=5, pady=5, sticky=W)
        btn_choice3.grid(row=5, column=1, padx=5, pady=5, sticky=W)
        btn_choice4.grid(row=7, column=1, padx=5, pady=5, sticky=W)
        btn_reset.grid(row=10, column=2, sticky=W)
        btn_find.grid_forget()

    # Output if unsuccessful json route calls
    elif json_status == 402: 
        messagebox.showerror("Error", "Oops! We encountered an error.\n" + 
        "Status Code: " + str(json_status) + 
        "; \n Invalid user inputs for one or both locations.")

        print(Fore.RED + "Oops! We encountered an error.")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.\n")
    elif json_status == 611: 
        messagebox.showerror("Error", "Oops! We encountered an error.\n" +
        "Status Code: " + str(json_status) + 
        "; \n Missing an entry for one or both locations.")

        print(Fore.RED + "Oops! We encountered an error.")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Missing an entry for one or both locations.\n")
    elif json_status == 500: 
        messagebox.showerror("Error", "Oops! We encountered an error.\n" +
        "Status Code: " + str(json_status) +
        "; \n The server encountered an error and could not complete your request.")

        print(Fore.RED + "Oops! We encountered an error.")
        print(Fore.RED + "Status Code: " + str(json_status) + "; The server encountered an error and could not complete your request.\n")
    elif json_status == 404: 
        messagebox.showerror("Error", "Oops! We encountered an error.\n" +
        "Status Code: " + str(json_status) +
        "; \n The resource addressed by the request URL does not exist.")

        print(Fore.RED + "Oops! We encountered an error.")
        print(Fore.RED + "Status Code: " + str(json_status) + "; The resource addressed by the request URL does not exist.\n")
    else:
        messagebox.showerror("Error", "Oops! We encountered an error.\n" +
        "For Status Code: " + str(json_status) + "; \n Refer to:" +
        "https://developer.mapquest.com/documentation/directions-api/status-codes")

        print(Fore.RED + "Oops! We encountered an error.")
        print(Fore.RED + "For Status Code: " + str(json_status) + "; Refer to:")
        print(Fore.RED + "https://developer.mapquest.com/documentation/directions-api/status-codes\n")

    return json_data


def choice1():
    json_data = getInput()

    distMi = (json_data["route"]["distance"])
    
    distKm = (json_data["route"]["distance"])*1.61
    distM = (json_data["route"]["distance"])*1609.344

    top = Toplevel()
    top.title("General Info")
    top.geometry("200x400")
    top.resizable(False, False) 

    lbl_output = Label(top, text= 
    "Starting Location Info: " + "\n" + 
    str(json_data["route"]["locations"][0]["adminArea5Type"]) + ": " 
    + str(json_data["route"]["locations"][0]["adminArea5"]) + "\n" +

    str(json_data["route"]["locations"][0]["adminArea4Type"]) + ": " 
    + str(json_data["route"]["locations"][0]["adminArea4"]) + "\n" +

    str(json_data["route"]["locations"][0]["adminArea3Type"]) + ": " 
    + str(json_data["route"]["locations"][0]["adminArea3"]) + "\n" +

    str(json_data["route"]["locations"][0]["adminArea1Type"]) + ": " 
    + str(json_data["route"]["locations"][0]["adminArea1"]) + "\n\n" +

    "Destination Info: " + "\n" + 
    str(json_data["route"]["locations"][1]["adminArea5Type"]) + ": " 
    + str(json_data["route"]["locations"][1]["adminArea5"]) + "\n" +

    str(json_data["route"]["locations"][1]["adminArea4Type"]) + ": " 
    + str(json_data["route"]["locations"][1]["adminArea4"]) + "\n" +

    str(json_data["route"]["locations"][1]["adminArea3Type"]) + ": " 
    + str(json_data["route"]["locations"][1]["adminArea3"]) + "\n" +

    str(json_data["route"]["locations"][1]["adminArea1Type"]) + ": " 
    + str(json_data["route"]["locations"][1]["adminArea1"]) + "\n\n" +
    
    "Trip Duration: " + str(json_data["route"]["formattedTime"]) + "\n" + 
    "Distance: \n" +
    "(in mi): " + str("{:.2f}".format(distMi)) + " m \n" +
    "(in km): " + str("{:.2f}".format(distKm)) + " km \n" +
    "(in m): " + str("{:.2f}".format(distM)) + " m \n")
    
    lbl_output.grid(padx=5, pady=10)

def choice2():
    json_data = getInput()

    top = Toplevel()
    top.title("Restrictions")
    top.geometry("200x200")
    top.resizable(False, False) 

    lbl_output = Label(top, text=
    "Timed restriction: " + str(json_data["route"]["hasSeasonalClosure"]) + "\n" +
    "Seasonal closure: " + str(json_data["route"]["hasSeasonalClosure"]) + "\n" +
    "Country cross: " + str(json_data["route"]["hasCountryCross"]) + "\n")

    lbl_output.grid(padx=5, pady=10)

def choice3():
    json_data = getInput()

    top = Toplevel()
    top.title("Miscellaneous")
    top.geometry("400x300")
    top.resizable(False, False) 

    lbl_output = Label(top, text=
    "Has toll road: " + str(json_data["route"]["hasTollRoad"]) + "\n" +
    "Has tunnel: " + str(json_data["route"]["hasTunnel"]) + "\n" +
    "Has highway: " + str(json_data["route"]["hasHighway"]) + "\n" +
    "Has ferry: " + str(json_data["route"]["hasFerry"]) + "\n" +
    "Has unpaved: " + str(json_data["route"]["hasUnpaved"]) + "\n\n" +

    "Latitude of " + orig.get() + ": " + str(json_data["route"]["locations"][0]["latLng"]["lat"]) + "\n" +
    "Longtitude of " + dest.get() + ": " + str(json_data["route"]["locations"][1]["latLng"]["lat"]) + "\n\n" +

    "Geo Quality Code of " + orig.get() + ": " + (json_data["route"]["locations"][0]["geocodeQualityCode"]) + "\n" +
    "Geo Quality Code of " + dest.get() + ": " + (json_data["route"]["locations"][1]["geocodeQualityCode"]))
    
    lbl_output.grid(padx=5, pady=10)

def choice4():
    json_data = getInput()

    top = Toplevel()
    top.title("Directions")
    top.resizable(False, False) 

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        lbl_output = Label(top, text=((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")))
        lbl_output.grid()

def reset():
    orig.set("")
    dest.set("")
    lbl_intro.grid_forget()
    btn_choice1.grid_forget()
    btn_choice2.grid_forget()
    btn_choice3.grid_forget()
    btn_choice4.grid_forget()
    btn_reset.grid_forget()
    btn_find.grid(row=2, column=1, sticky=W)

# GUI Design
lbl_orig = Label(window, text="Starting Location: ")
lbl_orig.grid(row=0, column=0, padx=5, pady=10, sticky=W)

lbl_dest = Label(window, text="Destination: ")
lbl_dest.grid(row=1, column=0, padx=5, pady=10, sticky=W)

txtbox_orig = Entry(window, textvariable=orig)
txtbox_orig.grid(row=0, column=1, sticky=W)

txtbox_dest = Entry(window, textvariable=dest)
txtbox_dest.grid(row=1, column=1, sticky=W)

btn_find = Button(window, command=getInput, text="Find")
btn_find.grid(row=2, column=1, sticky=W)

# Menu
lbl_intro = Label(window, text="Menu", font="Ubuntu 15 bold")
btn_choice1 = Button(window, text="General Info", command=choice1)
btn_choice2 = Button(window, text="Restrictions", command=choice2)
btn_choice3 = Button(window, text="Miscellaneous", command=choice3)
btn_choice4 = Button(window, text="Directions", command=choice4)
btn_reset = Button(window, command=reset, text="Reset")

window.mainloop()