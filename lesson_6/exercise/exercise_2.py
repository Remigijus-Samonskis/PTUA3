#Create a database (List of privileged users) print a specific message with a personal 
# greeting if the user is a privileged and just "Welcome otherwise"

user = "Remigijus"
privileged_users = ["Algis", "Asta", "Mynde","Remigijus"]
if user in privileged_users:
    print(f"Welcome {user}")
else:
    print("")