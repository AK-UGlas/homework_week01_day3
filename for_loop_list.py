# Given a list of users, create a function to find the 
# user with a user_id of 4.

def find_user_from_id(user_list, target_id):
    for user in user_list:
        if user["user_id"] == target_id:
            return user

    return "user not found"

users = [
  { "user_id": 1, "first_name": "Margaret", "last_name": "Chicken" },
  { "user_id": 2, "first_name": "Bill", "last_name": "Gates" },
  { "user_id": 3, "first_name": "Steve", "last_name": "Jobs" },
  { "user_id": 4, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 5, "first_name": "Brendan", "last_name": "Eich" },
]

print(find_user_from_id(users, 4))