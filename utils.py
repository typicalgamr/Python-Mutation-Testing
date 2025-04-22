def categorize_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teen"
    elif 20 <= age < 65:
        return "Adult"
    else:
        return "Senior"
