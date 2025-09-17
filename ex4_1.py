def calculate_id_letter(id_number):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    remainder = id_number % 23
    return letters[remainder]

id_number_str = input("Enter the 8-digit ID number: ")
id_number = int(id_number_str)

# Check if the number has 8 digits
if len(id_number_str) != 8:
    print("Error: The ID number must have exactly 8 digits.")
    exit()

entered_letter = input("Enter the ID letter: ").upper()

correct_letter = calculate_id_letter(id_number)

if entered_letter == correct_letter:
    print(f"The ID {id_number_str}{entered_letter} is valid.")
else:
    print(f"Invalid ID. The correct letter for {id_number_str} is {correct_letter}.")