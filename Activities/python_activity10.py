main_roads = ["Roxas Avenue", "Arnaldo Boulevard", "Fuentes Drive"]
speed_limits = (80, 50, 60)
vehicle_spotted = []
total_fines_per_road = {}

vehicle_report = int(input("How many vehicle reports to process (1-5): "))

for i in range(vehicle_report):
    road_name = input("What is the road name: ")
    license_plate = input("What is the license plate: ")
    speed = int(input("What is the speed: "))

    vehicle_spotted.append(license_plate)

    for road in main_roads:
        if road_name == road:
            print(main_roads.index(road))
            if speed >= speed_limits[main_roads.index(road)]+10:
                fine_count = 0
                while speed > speed_limits[main_roads.index(road)]:
                    fine_count+=1
                    speed-=1
                    fine = fine_count * 5

                total_fines_per_road[road_name] = fine

                print(fine)
                print(total_fines_per_road)
            elif speed < 20:
                print("The driver is a slow driver!")

            break
    else:
        if road_name not in main_roads:
            main_roads.append(road_name)
            converted_tuple = list(speed_limits)
            converted_tuple.append(70)
            speed_limits = tuple(converted_tuple)

            total_fines_per_road[road_name] = 0

            print(speed_limits)
    i += 1

print(main_roads)
high_fine = []

for road, fines in total_fines_per_road.items():
    high_fine.append(fines)


if len(vehicle_spotted) < len(main_roads):
    del fine.min()


print(f"Active Roads: {main_roads}")
print(f"Speed Limits: {speed_limits}")
print(f"Fine Totals: {sum(high_fine)}")
print(f"Fine Totals: {high_fine}")

print(high_fine)


