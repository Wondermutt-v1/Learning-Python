#
# Example file for parsing and processing JSON
# LinkedIn Learning Python course
#

import urllib.request



def printResults(data):
    import json


    # Use the json module to load the string data into a directory
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number of events, plus magnitude and each event name
    # print("%s total events recorded" % str(theJSON["metadata"]["count"]))
    count = theJSON['metadata']['count']
    
    #2 different ways to print the count of events
    print(f"{count} total events recorded")
    # print(str(count) + " total events recorded")
    
    # for each event, print the place where it occurred
    # On the USGS feed the features is an array of events, so we can loop through that
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("---------------")
     
    # point the events that only have a magnitude greater than 4.0
    for i in theJSON["features"]:
        #if i["properties"]["mag"] >= 4.0:
        if i["properties"]["mag"] >=5.0:
            
            ## alternative way to print the magnitude and place of the event
            #print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
            print(i["properties"]["place"], "mag:", i["properties"]["mag"])
            # print(i["properties"]["place"])
    print("-------------------")

    # print only events where at least 1 person reported feeling something
    print("\nEvents that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(i["properties"]["place"], "felt:", feltReports, "times")




def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from USGS
    # This feed lists all the earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    
    #open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error from the server, cannot retrieve results")
    
    
if __name__ == "__main__":
    main()
