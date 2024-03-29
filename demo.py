# NoSQL-like database using Python dictionaries

# Define the collections
presidents = []
states = []
pres_hobbies = []
administrators = []
admin_pr_vp = []
pres_marriages = []
elections = []

# Insert data into the 'presidents' collection
presidents.append({
    "PRES_NAME": "Barack Obama",
    "PRES_BIRTH_YR": 1961,
    "PRES_DEATH_YR": None,
    "STATE_BORN": "Hawaii",
    "PARTY": "Democrat"
})

presidents.append({
    "PRES_NAME": "John F. Kennedy",
    "PRES_BIRTH_YR": 1917,
    "PRES_DEATH_YR": 1963,
    "STATE_BORN": "Massachusetts",
    "PARTY": "Democrat"
})

presidents.append({
    "PRES_NAME": "George Washington",
    "PRES_BIRTH_YR": 1732,
    "PRES_DEATH_YR": 1799,
    "STATE_BORN": "Virginia",
    "PARTY": "None"
})

presidents.append({
    "PRES_NAME": "Thomas Jefferson",
    "PRES_BIRTH_YR": 1743,
    "PRES_DEATH_YR": 1826,
    "STATE_BORN": "Virginia",
    "PARTY": "Democrat-Republican"
})

presidents.append({
    "PRES_NAME": "Abraham Lincoln",
    "PRES_BIRTH_YR": 1809,
    "PRES_DEATH_YR": 1865,
    "STATE_BORN": "Kentucky",
    "PARTY": "Republican"
})

# Insert data into the 'states' collection
states.append({
    "STATE_NAME": "California",
    "ADMIN_ENTERED": "John F. Kennedy",
    "YEAR_ENTERED": 1850
})

# Insert data into the 'pres_hobbies' collection
pres_hobbies.append({
    "PRES_NAME": "John F. Kennedy",
    "PRES_HOBBY": "Sailing"
})

# Insert data into the 'pres_marriages' collection
pres_marriages.append({
    "PRES_NAME": "John F. Kennedy",
    "SPOUSE_NAME": "Jacqueline Kennedy Onassis",
    "PR_AGE": 36,
    "SP_AGE": 31,
    "NA_CHILDREN": 2,
    "MAR_YEAR": 1953
})

pres_marriages.append({
    "PRES_NAME": "Barack Obama",
    "SPOUSE_NAME": "Michelle Obama",
    "PR_AGE": 31,
    "SP_AGE": 28,
    "NA_CHILDREN": 2,
    "MAR_YEAR": 1992
})

pres_marriages.append({
    "PRES_NAME": "George Washington",
    "SPOUSE_NAME": "Martha Washington",
    "PR_AGE": 27,
    "SP_AGE": 27,
    "NA_CHILDREN": 0,
    "MAR_YEAR": 1759
})


# Insert data into the 'elections' collection
elections.append({
    "PRES_NAME": "John F. Kennedy",
    "ELECTION_YR": 1960,
    "PARTY": "Democrat",
    "STATE_WON": "California"
})

elections.append({
    "PRES_NAME": "Barack Obama",
    "ELECTION_YR": 2008,
    "PARTY": "Democrat",
    "STATE_WON": "California"
})

elections.append({
    "PRES_NAME": "George Washington",
    "ELECTION_YR": 1789,
    "PARTY": "None",
    "STATE_WON": "Virginia"
})

elections.append({
    "PRES_NAME": "Thomas Jefferson",
    "ELECTION_YR": 1800,
    "PARTY": "Democrat-Republican",
    "STATE_WON": "Virginia"
})

elections.append({
    "PRES_NAME": "Abraham Lincoln",
    "ELECTION_YR": 1860,
    "PARTY": "Republican",
    "STATE_WON": "Illinois"
})

# Insert data into the 'administrators' collection
administrators.append({
    "ADMIN_NAME": "John F. Kennedy",
    "ADMIN_YR": 1961,
    "ADMIN_END_YR": 1963,
    "ADMIN_PARTY": "Democrat"
})

# Insert data into the 'admin_pr_vp' collection
admin_pr_vp.append({
    "ADMIN_NAME": "John F. Kennedy",
    "ADMIN_PR": "Lyndon B. Johnson",
    "ADMIN_VP": "None"
})


# Querying the NoSQL-like database
# Example: Find all presidents born in Virginia
virginia_presidents = [p for p in presidents if p["STATE_BORN"] == "Virginia"]

# Example: Find all presidents who were Democrats
democrat_presidents = [p for p in presidents if p["PARTY"] == "Democrat"]



print(f'Virginia Presidents: {virginia_presidents}')
print(f'Democrat Presidents: {democrat_presidents}')

