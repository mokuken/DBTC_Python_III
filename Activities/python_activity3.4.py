
# Dictionary of list
guest = {
    "ryan" : 12,
    "art" : 12,
    "jemart" : 12,
    "Jessie" : 12
}

# add new guest
guest["earl"] = 12

print("\nThe updated plan")
for guest_name, items in guest.items():
    items_str = ', '.join(items)
    print(f"{guest_name} bring these foods {items_str}")