from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.warnings import risk_assessment

def run():
    #create list of stations
    stations = build_station_list()

    #update their water level data
    update_water_levels(stations)
    

    #runs code to divide stations into lists of tuples based on their risk of flooding
    x = risk_assessment(stations[:500])

    #split stations into 4 lists of tuples based on the number in their tuple
    severe = []
    high = []
    moderate = []
    low = []
    for tuple in x:
        if tuple[1] == 4:
            severe.append(tuple)
        elif tuple[1] == 3:
            high.append(tuple)
        elif tuple[1] == 2:
            moderate.append(tuple)
        elif tuple[1] == 1:
            low.append(tuple)
        else:
            print("error")
    
    #print the severe and high station tuples
    print("Severe: 4, High:3")
    print(severe)
    print(high)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
