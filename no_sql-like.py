# Define the initial data for the presidential database
presidents = [
    {"first_name": "George", "last_name": "Washington", "party": "Independent", "birth_year": 1732, "death_age": 67},
    {"first_name": "John", "last_name": "Adams", "party": "Federalist", "birth_year": 1735, "death_age": 90},
    {"first_name": "Thomas", "last_name": "Jefferson", "party": "Democratic-Republican", "birth_year": 1743, "death_age": 83},
    # Add more presidents here...
]

states = [
    {"state_name": "Virginia", "year_entered": 1788},
    {"state_name": "Massachusetts", "year_entered": 1788},
    {"state_name": "Virginia", "year_entered": 1788},
    # Add more states here...
]

pres_hobbies = [
    {"first_name": "George", "last_name": "Washington", "hobby": "Farming"},
    {"first_name": "John", "last_name": "Adams", "hobby": "Reading"},
    {"first_name": "Thomas", "last_name": "Jefferson", "hobby": "Writing"},
    # Add more hobbies here...
]

administrators = [
    {"admin_name": "John F. Kennedy", "state_entered": "California", "year_entered": 1850},
    # Add more administrators here...
]

admin_pr_vp = [
    {"admin_name": "John F. Kennedy", "president": "Barack Obama", "vice_president": "Joe Biden"},
    # Add more admin/pr/VP relationships here...
]

pres_marriages = [
    {"first_name": "George", "last_name": "Washington", "spouse": "Martha Washington", "marriage_year": 1759},
    {"first_name": "John", "last_name": "Adams", "spouse": "Abigail Adams", "marriage_year": 1764},
    {"first_name": "Thomas", "last_name": "Jefferson", "spouse": "Martha Jefferson", "marriage_year": 1772},
    # Add more marriages here...
]

elections = [
    {"year": 1789, "president": "George Washington", "vice_president": "John Adams"},
    {"year": 1792, "president": "George Washington", "vice_president": "John Adams"},
    {"year": 1796, "president": "John Adams", "vice_president": "Thomas Jefferson"},
    # Add more elections here...
]

# Add more collections and initial data as needed

# Add a new president to the database
new_president = {"first_name": "Abraham", "last_name": "Lincoln", "party": "Republican", "birth_year": 1809, "death_age": 56}
presidents.append(new_president)

# Remove a president from the database
removed_president = presidents.pop()
print("Removed President:", removed_president)

# Print the current list of presidents
print("\nCurrent List of Presidents:")
for president in presidents:
    print(president["first_name"], president["last_name"])

# Add new presidents from a list
new_presidents_list = [
    ["Theodore", "Roosevelt", "Republican", 1858, 60],
    ["Franklin", "Roosevelt", "Democratic", 1882, 63],
    ["John", "Kennedy", "Democratic", 1917, 46],
    # Add more presidents here...
]

for first_name, last_name, party, birth_year, death_age in new_presidents_list:
    new_president = {"first_name": first_name, "last_name": last_name, "party": party, "birth_year": birth_year, "death_age": death_age}
    presidents.append(new_president)

# Print the list of states
print("\nList of States:")
for state in states:
    print(state["state_name"])

# Asking user input for a new president
new_president_first_name = input("Enter the first name of the new president: ")
new_president_last_name = input("Enter the last name of the new president: ")
new_president_party = input("Enter the political party of the new president: ")
new_president_birth_year = int(input("Enter the birth year of the new president: "))
new_president_death_age = int(input("Enter the death age of the new president: "))

new_president = {
    "first_name": new_president_first_name,
    "last_name": new_president_last_name,
    "party": new_president_party,
    "birth_year": new_president_birth_year,
    "death_age": new_president_death_age
}

presidents.append(new_president)

# Print the updated list of presidents
print("\nUpdated List of Presidents:")
for president in presidents:
    print(president["first_name"], president["last_name"])
