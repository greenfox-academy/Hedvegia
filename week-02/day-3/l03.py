# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs(ls, app):
    new_verbs = []
    for i in range(0, len(verbs)):
        new_verbs.append(app + ls[i])
    print(new_verbs)

create_new_verbs(verbs, preverb)
