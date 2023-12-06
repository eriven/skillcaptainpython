def define_age_group(age):
    if age < 18:
        return "You are a minor."
    elif age <= 65:
        return "You are an adult."
    else:
        return "You are a senior citizen."

# Example usage
age_input = int(input("Enter your age: "))
message = define_age_group(age_input)
print(message)

