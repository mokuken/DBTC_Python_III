main_roads = ["Roxas Avenue", "Arnaldo Boulevard", "Fuentes Drive"]
speed_limits = (80, 50, 60)
vehicle_spotted = set()
total_fines_per_road = {}

vehicle_report = int(input("How many vehicle reports to process (1-5): "))

for i in range(vehicle_report):
    road_name = input("\nWhat is the road name: ")
    license_plate = input("What is the license plate: ")
    speed = int(input("What is the speed: "))

    vehicle_spotted.add(license_plate)

    fine = 0
    for road in main_roads:
        if road_name == road:
            if speed >= speed_limits[main_roads.index(road)]+10:
                fine = (speed - speed_limits[main_roads.index(road)]) * 5
            elif speed < 20:
                print("The driver is a slow driver!")

            total_fines_per_road[road_name] = fine

            break
        else:
            if road_name not in main_roads:
                main_roads.append(road_name)
                converted_tuple = list(speed_limits)
                converted_tuple.append(70)
                speed_limits = tuple(converted_tuple)

                if speed >= 70:
                    fine = (speed - 70) * 5
                elif speed < 20:
                    print("The driver is a slow driver!")

                total_fines_per_road[road_name] = fine
    
    print(f"Fine: {fine}")
    i += 1

total_fine = []
for road, fine in total_fines_per_road.items():
    total_fine.append(fine)

print(f"\nActive Roads: {main_roads}")
print(f"Speed Limits: {speed_limits}")
print(f"Fine Totals: {sum(total_fine)}")

worst_road_fine = 0
worst_road = ""

for road_name, fine in total_fines_per_road.items():
    if fine > worst_road_fine:
        worst_road_fine = fine
        worst_road = road_name

print(f"Worst Road: {worst_road}")
print(f"Unique Vehicles: {len(vehicle_spotted)}\n")