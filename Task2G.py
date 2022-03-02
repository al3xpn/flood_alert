from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.warnings import risk_assessment

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    x = risk_assessment(stations)
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
    print("Severe: 4, High:3")
    print(severe)
    print(high)

if __name__ == "__main__":
    run()
