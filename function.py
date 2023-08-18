# no input and no output
def my_func():
    print("hello Zeinab!")
    
my_func()

# no input and has output
def my_func1():
    return"How are you?"

print(my_func1())


# input and no output
def my_func2(where):
    print(where)

my_func2("Where are you?")

# has input and has output
def my_func3(doing):
    return doing

print(my_func3("What are you doing?"))


# The global value (متغیری ک خارج از تابع معرفی شده است)
y = "zeinab"
def my_func4():
    print(y)

my_func4()

def my_func6():
    print(y)

my_func6()
