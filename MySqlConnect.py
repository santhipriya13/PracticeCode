import mysql.connector
print("Hello");
# a=input("Enter the user name" );
# b=input("Eneter the passwaord ");
#
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Goalchange@4", database="test_py");
#
# mycursor=mydb.cursor()
# c=mycursor.execute("select pwd from user_pwd ")
#
# print(mycursor)
# print(3+4)
# result=mycursor.fetchall()
# print(result)
#
# for i in result:
#
#     print(i)
# a=0
# my_list =[1,2,3,4,5,6,7,8,9,10]
# for item in my_list:
#     a=a+item
#     print(a)
# print(a)

a = [[0, 0, 0, 1, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0],
     [0, 1, 1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0]]
for item in a:
    for i in item:
        if i == 0:
            print(' ', end='')
            print(' ', end='')
        elif i == 1:
            print("*", end='')
            print("*", end='')

    print(end='\n')


# Parameters
def say_hello(name, emoji):
    print(f'hello, {name} {emoji}')


say_hello('santhi', ' ✋ 😬 ')


def highest_even(*a):
    print(a)
    even = []
    for item in a:
        if item % 2 == 0:
            even.append(item)
            print(even)

    pass


print(highest_even(10, 2, 3, 4, 5, 11))
