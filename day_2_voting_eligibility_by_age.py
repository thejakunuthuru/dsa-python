age = int(input())

def voting_eligibility_by_age(age):
    if age < 1:
        return "Invalid age"
    elif age < 18:
        return "Not eligible to vote"
    else:
        return "Eligible to vote"

print(voting_eligibility_by_age(age))