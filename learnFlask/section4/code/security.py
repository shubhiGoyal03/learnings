from user import User

users=[
    User(1,"Shubhi","Goyal")
]

username_mapping={u.username : u for u in users}
userid_mapping={u.id for u in users}

def authentication(username,password):
    user=username_mapping.get(username,None)
    if user and password==user.password:
        return user

def identify(payload):
    user_id=payload['identify']
    return userid_mapping.get(user_id,None)