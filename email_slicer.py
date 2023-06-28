def get_email():
    global email
    email= input("Please tell me your Email Adress:")

def slice_email():
    parts = email.split("@")
    username = parts[0]
    domainpart = parts[1].split(".")
    domain = domainpart[0]
    extension = domainpart[1]
    print(f"Username: {username} Domainname: {domain} Extension: {extension}")

get_email()
slice_email()