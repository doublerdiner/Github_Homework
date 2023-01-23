name = "Chris Barclay"
age = 34
has_a_dog = True
years_in_the_future = 5


def individual_details(name, age, has_a_dog, years_in_the_future):
    statement = (f"Hi, my name is {name} and I'm {age} years old. \
        \nIn {years_in_the_future} years time I'll be {age + years_in_the_future} years old.")
    if has_a_dog:
        return statement + (f"\nOh... And I also have a dog too.")
    else: 
        return statement

print(individual_details(name, age, has_a_dog, years_in_the_future))