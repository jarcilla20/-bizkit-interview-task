from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database 

    Parameters:
        args: A dictionary containing the following search parameters:
            id: string 
            name: string 
            age: string 
            occupation: string 

    Returns:
        A list of users that match search parameters
    """
    # Start with an empty list to store matching users
    matching_users = []

    # Extract search parameters from args dictionary
    id = args.get('id')
    name = args.get('name')
    age = args.get('age')
    occupation = args.get('occupation')

    def is_age_match(user_age, search_age):
        return abs(user_age - search_age) <= 1
    # Helper function for sorting based on matching priority
    def matching_priority(user):
        if user['id'] == id:
            return 0
        elif name and name.lower() in user['name'].lower():
            return 1
        elif age and is_age_match(int(user['age']), int(age)):
            return 2
        elif occupation and occupation.lower() in user['occupation'].lower():
            return 3
        else:
            return 4

    # Loop through the USERS data and filter based on search parameters
    for user in USERS:
        if id and str(user['id']) == id:
            matching_users.append(user)
        elif name and name.lower() in user['name'].lower():
            matching_users.append(user)
        elif age and is_age_match(int(user['age']), int(age)):
            matching_users.append(user)
        elif occupation and occupation.lower() in user['occupation'].lower():
            matching_users.append(user)

    # Sort matching_users based on matching priority
    matching_users.sort(key=matching_priority)

    return matching_users

    #return USERS
