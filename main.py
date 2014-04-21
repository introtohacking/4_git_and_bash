
def say_hello(n):
    """Prints 'hello' n times"""
    
    for i in range(n):
        print "hello"

if __name__ == "__main__":
    n = int(raw_input("How many times would you like me to say hello? "))
    say_hello(n)