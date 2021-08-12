class User:
    id = None
    weights = None
    all_weights = None
    created = None
    calorieGoal = 2000
    calorieSummary = None
    #oauthToken = None
    #oauthSecret = None
    #scaleIEMI = None
    enabled = None
    #lastSeen = None
    group = 'Not Set'
    status = 'Weight Loss'
    #prefs = None
    #activities = None
    foodEntries = None
    earliest = None

if __name__ == "__main__":
    user = User()
    user.id = 1
    data = {'weights': 123, 'group': 'pilot', 'thisIsATest': 'hello world'}
    print(user.__dict__)
    for key ,value in data.items():
        user.__dict__[key] = value
    print(user.__dict__)
    print(user.group)
    print(user.weights)
    print.thisIsATest