# print(func(['hello', 5, 'John', ]))
# ['Element', 'start', 'hello', 5, 'John', 'finish']
# def func():
#     my_list=['hello',5,'John']
#     return my_list

def func(b):
    a=int(input('insert numbers'))
    b=lambda a:  a %2 == 0
    return func

print(func)
    
