import requests
import folium




def main():
    url = "http://data.cityofchicago.org/resource/ijzp-q8t2.json"
    r = requests.get(url)
    data = r.json()
    print('Data Type:', type(data))
    print('Length:', len(data))
    map_data = []
    for d in data:
        try:
            map_data.append([d['primary_type'], d['latitude'], d['longitude']])
        except:
            print("whoops")
    print('created map')
    map1 = folium.Map(location=[float(41.8369), float(-87.6847)], zoom_start=11, tiles='OpenStreetMap')
    prim_types = []
    for d in map_data:
        color = ''
        if d[0] not in prim_types:
            prim_types.append(d[0])
        print(d[1], d[2], d[0])
        if d[0] == 'NARCOTICS':
            color = '#B995E6'
            side = 3
        if d[0] == 'CRIMINAL TRESPASS':
            color = '#2652E0'
            side = 4
        if d[0] == 'THEFT':
            color = '#0D0E0F'
            side = 4
        if d[0] == 'CRIMINAL DAMAGE':
            color = '#24D1C8'
            side = 4
        if d[0] == 'BATTERY':
            color = '#512370'
            side = 5
        if d[0] == 'PROSTITUTION':
            color = '#F22492'
            side = 6
        if d[0] == 'OTHER OFFENSE':
            color = '#BFBFBF'
            side = 5
        if d[0] == 'ASSAULT':
            color = '#295E09'
            side = 5
        if d[0] == 'ROBBERY':
            color = '#7A4304'
            side = 4
        if d[0] == 'MOTOR VEHICLE THEFT':
            color = '#7ECAFC'
            side = 4
        if d[0] == 'KIDNAPPING':
            color = '#F59E14'
            side = 5
        if d[0] == 'INTERFERENCE WITH PUBLIC OFFICER':
            color = '#8A795F'
            side = 4
        if d[0] == 'PUBLIC PEACE VIOLATION':
            color = '#05FC37'
            side = 4
        if d[0] == 'BURGLARY':
            color = '#E5ADF0'
            side = 5
        if d[0] == 'GAMBLING':
            color = '#D6ED98'
            side = 4
        if d[0] == 'WEAPONS VIOLATION':
            color = '#E8AFAC'
            side = 5
        if d[0] == 'DECEPTIVE PRACTICE':
            color = '#826968'
            side = 4
        if d[0] == 'SEX OFFENSE':
            color = '#FF00EA'
            side = 6
        if d[0] == 'INTIMIDATION':
            color = '#08999C'
            side = 5
        if d[0] == 'OFFENSE INVOLVING CHILDREN':
            color = '#61AB86'
            side = 6
        if d[0] == 'OTHER NARCOTIC VIOLATION':
            color = '#636363'
            side = 3
        if d[0] == 'ARSON':
            color = '#FF0000'
            side = 5
        if d[0] == 'HOMICIDE':
            color = '#A80303'
            side = 5
        map1.polygon_marker([float(d[1]), float(d[2])], popup=str(d[0]), fill_color=color, num_sides=side, radius=10)
    map1.create_map(path='chiCrimes.html')



if __name__ == "__main__" :
    main()