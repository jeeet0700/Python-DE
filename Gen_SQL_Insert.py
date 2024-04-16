import random

# Function to generate a random name
def generate_name():
    first_names = ['John', 'Robert', 'David', 'Betty', 'Alice', 'Michael', 'Sarah', 'Emily', 'Daniel', 'Jennifer']
    last_names = ['Doe', 'Luna', 'Robinson', 'Reinhardt', 'Smith', 'Johnson', 'Brown', 'Lee', 'Garcia', 'Davis']
    return random.choice(first_names), random.choice(last_names)

# Function to generate a random age between 18 and 70
def generate_age():
    return random.randint(15, 20)

# Function to generate a random country
def generate_country():
    countries = ['USA', 'UK', 'UAE', 'Canada', 'Australia', 'Germany', 'France', 'Japan', 'India', 'Brazil']
    return random.choice(countries)

def generate_math_mark():
    return random.randint(80,100)

def generate_phy_mark():
    return random.randint(80,100)

def generate_chem_mark():
    return random.randint(80,100)

def generate_bio_mark():
    return random.randint(80,100)

# Generate and print insert queries
for i in range(1, 5):  # Generating 100 more records starting from customer_id 101
    first_name, last_name = generate_name()
    age = generate_age()
    country = generate_country()
    math_mark=generate_math_mark()
    phy_mark=generate_phy_mark()
    chem_mark=generate_chem_mark()
    bio_mark=generate_bio_mark()

    insert_query = f"INSERT INTO Marks (Student_id, first_name, last_name, age, country, math,phy,chem,bio) VALUES ({i}, '{first_name}', '{last_name}', {age}, '{country}',{math_mark},{phy_mark},{chem_mark},{bio_mark});"
    print(insert_query)
