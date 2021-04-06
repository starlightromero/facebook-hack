"""Main"""
import pandas as pd

print("***FACEBOOK LEAKED DATA FINDER***")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

leaked = False

print(
    "Please wait... we are procesing millions of leaked Facebook records for your piece of mind."
)

for n in range(1, 9):
    try:
        df = pd.read_csv(
            f"USA/USA 0{n}.txt", delimiter=":", header=None, low_memory=False
        )
        result = df[(df[2] == first_name) & (df[3] == last_name)]
        if not result.empty:
            leaked = True
    except:
        pass

if leaked:
    print(
        "Facebook has leaked your data! This data may include but is not limited to: full name, location, past location(s), birthdate, email addresses, phone number, bio, and relationship status."
    )
else:
    print("You are in the clear.")
