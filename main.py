def email_slicer(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        print("Invalid email format.")
        return None, None

def main():
    print("Welcome to the Email Slicer Program!")

    email = input("Enter an email address: ")
    username, domain = email_slicer(email)

    if username is not None and domain is not None:
        print(f"\nUsername: {username}")
        print(f"Domain: {domain}")

if __name__ == "__main__":
    main()
