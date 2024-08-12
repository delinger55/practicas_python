def  log_message():
    print("Hellow Wordl")
    
num= 0
def log_massage2():
    print(num)

def log_massage3(num):
    num= 3
    print(num)
    
def func():
    return 5

#Main
result = func()
print(result)
log_message()

num=1
log_massage2()
num= 2
log_massage2()
log_massage3(7)#siempre imprime 3

