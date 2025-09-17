
total_seats = int(input("Enter the total number of seats to be allocated: "))
num_parties = int(input("Enter the number of parties: "))

party_names = []
party_votes = []
party_seats = [0] * num_parties

# Read votes for each party
for i in range(num_parties):
    name = input(f"Enter the name of party {i + 1}: ")
    votes = int(input(f"Enter the number of votes for {name}: "))
    party_names.append(name)
    party_votes.append(votes)

# Main D'Hondt allocation loop
for seat_number in range(total_seats):
    highest_quotient = 0
    party_with_highest_quotient_index = -1

    # Find the party with the highest quotient
    for i in range(num_parties):
        # Calculate the quotient using the formula: V / (s + 1)
        current_quotient = party_votes[i] / (party_seats[i] + 1)

        if current_quotient > highest_quotient:
            highest_quotient = current_quotient
            party_with_highest_quotient_index = i

    # Allocate the seat to the party with the highest quotient
    if party_with_highest_quotient_index != -1:
        party_seats[party_with_highest_quotient_index] += 1


# Final results here
print("\n--- Final Seat Allocation ---")
for i in range(num_parties):
    print(f"{party_names[i]}: {party_seats[i]} seat(s)")