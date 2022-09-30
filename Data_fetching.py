# from Linked_List import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="AI@12345", database="data")

mycursor = mydb.cursor()


class Node:
    def __init__(self,):
        # global info1,info2,info3,info4,info5
        info1 = input("Enter Student Name:")
        info2 = input("Enter Student Roll_no:")
        info3 = input("Enter Student Collage_name:")
        info4 = input("Enter Student Email_ID:")
        info5 = input("Enter Student Course_name:")

        # self.data = info1, info2, info3, info4, info5
        mycursor.execute("Insert into Student_info(Name,Roll_no,Collage_name,Email_ID,Course_name) values(%s,%s,%s,%s,%s)", (info1, info2, info3, info4, info5))
        mydb.commit()
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(self)
                n = n.ref

    def add_end(self, ):
        new_node = Node()
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


def Data():
    LL1 = LinkedList()
    LL1.add_end()

# Data()
print('\n------------------------ < < * STUDENT ENROLMENT SYSTEM * > >------------------------------')
print("-----------------------------------------------------")
print("|             1. do you want to register            |")
print("|                      or                           |")
print("|             2. want to see the details           |")
print("-----------------------------------------------------")
while True:
    ask = input("Please choose any one from the above \n--> ")
    if ask == '1':
        print("Fill The Following details")
        Data()
        break


    elif ask == "2":
        ask = input(f"Enter the Roll_no of the student:")
        mycursor.execute(f"select * from Student_info where Roll_no = {ask}")

        myresult = mycursor.fetchall()

        for row in myresult:
            print(row)
        break
