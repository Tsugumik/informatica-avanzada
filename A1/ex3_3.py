registrations = {}

print("Enter car registration numbers (or 'END' to finish):")

while True:
    reg_number = input().strip().upper()

    if reg_number == "END":
        break

    if len(reg_number) > 0:
        first_letter = reg_number[0]

        if first_letter not in registrations:
            registrations[first_letter] = [reg_number]
        else:
            registrations[first_letter].append(reg_number)

print("\nData entry finished. You can now search for registrations.")

while True:
    search_letter = input("Enter a letter to find all registrations that start with it (or 'END' to exit): ").strip().upper()

    if search_letter == "END":
        break

    if search_letter in registrations:
        print(f"Registrations starting with '{search_letter}':")
        for reg in registrations[search_letter]:
            print(reg)
    else:
        print(f"No registrations found starting with '{search_letter}'.")