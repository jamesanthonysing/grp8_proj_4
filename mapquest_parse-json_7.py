import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "PJv71zxlt65ihzFpAKRuP6HQ3zaCJDQ9"

print("========================================")
print("MapQuest Pathfinder 2.0")
print("Improved by Group#8 - 4-ITI")
print("========================================")

while True:
    # Ask user for input regarding starting location & destination
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        print("========================================")
        print("Thank you for using MapQuest Pathfinder!")
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        print("========================================")
        print("Thank you for using MapQuest Pathfinder!")
        break
    
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    # Get json data request
    json_data = requests.get(url).json()

    print("URL " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    # Successful json route call
    if json_status == 0:
        print("API Status " + str(json_status) + " = A successful route call.\n")
        print("========================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("========================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("========================================")
    # Unsuccessful json route call
    elif json_status == 402:
        print("****************************************")
        print("Oops! We encountered an error.")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("****************************************")
    elif json_status == 611:
        print("****************************************")
        print("Oops! We encountered an error.")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("****************************************")
    else:
        print("****************************************")
        print("Oops! We encountered an error.")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("****************************************\n")