def unused_function():
    # This function is never used
    print("I'm an unused function.")

def buggy_division(a, b):
    # This function has a potential ZeroDivisionError
    return a / b

def long_method():
    # This method is unnecessarily long and contains multiple issues
    message = "Welcome"  # Unused variable
    print("Hello, World!")
    print("Hello, Again!")  # Duplicate print statement
    if True:
        pass  # Empty block
    for i in range(5):
        if i % 2 == 0:
            continue
        elif i % 2 != 0:  # Redundant condition
            print("Odd number:", i)

def hardcoded_password():
    # Hardcoded credentials, a security vulnerability
    username = "admin"
    password = "12345"
    print(f"Logging in with username: {username} and password: {password}")

if __name__ == "__main__":
    buggy_division(10, 0)  # Runtime issue: division by zero
    long_method()
    hardcoded_password()
