from functions import salary,hello_who

assert hello_who("Max") == "Hello, Max", "hello_who error"
assert hello_who("Leo") == "Hello, Leo", "hello_who error"
assert hello_who("Nikita") == "Hello, Nikita", "hello_who error"
assert salary(2,1) == 4
assert salary(2,2) == 8