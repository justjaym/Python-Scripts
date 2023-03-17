class hotelmanage:
    #constructor method in class, called when declaring an object
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',cindate='',coutdate='',rno=1,bookings=[]):

        print ("\n-----WELCOME TO COCKERS INN MOTEL-----\n\n")

        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.bookings=bookings
        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno

    #this function is responsible fo the ata entry of the customer
    def inputdata(self):
        print("\n\n//Customer Data Entry//")
        self.name=input("\nEnter your Fullname: ")
        self.address=input("Enter your address: ")
        self.cindate=input("Enter your check in date: ")
        self.coutdate=input("Enter your checkout date: ")
        print("\nYour room no.: ",self.rno,"\n")
    
    #this is where the customer will have to choose a room
    def roomrent(self):
        print("\n\n//Customer Room Selection//")
        print ("\nWe have the following rooms for you:-")
        print ("1.  California King Room = P4000")
        print ("2.  Presidential Suit = P3000")
        print ("3.  Luxury Suite = P2000")
        print ("4.  Quickie Room = P1000")

        x=int(input("Enter the number of your choice Please-> "))
        n=int(input("For How Many Nights Did You Stay: "))

        if(x==1):
            print ("you have choose room Class A")
            self.s=4000*n
        elif (x==2):
            print ("you have choose room Class B")
            self.s=3000*n
        elif (x==3):
            print ("you have choose room Class C")
            self.s=2000*n
        elif (x==4):
            print ("you have choose room Class D")
            self.s=1000*n
        else:
            print ("please choose a room")

        print ("your choosen room rent is =",self.s,"\n")

    #function for buying food hehehe nom nom briii pugaa
    def foodpurchased(self):

        print("\n\n//Restaurant Menu//")
        print("1.Dessert----->100\n2.Drinks----->50\n3.Breakfast--->90\n4.Lunch---->110\n5.Dinner--->150\n6.Exit")

        while (1):
            c=int(input("Enter the number of your choice:"))
            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d
            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d
            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d
            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d
            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d
            elif (c==6):
                break;
            else:
                print("You've Enter an Invalid Key")

        print ("Total food Cost=",self.r,"\n")


    #displaying the Receipt of the customer lol
    def display(self):
        print("\n\n//Hotel Bill//")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total Purchased is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal Purchased is:",self.rt+self.a,"\n")
        self.rno+=1
    
    #para ma search hehe kaamtok
    def search(self, term):
        if term in self.name:
            return f"Name: {self.name}\nAddress: {self.address}\nCheck-in Date: {self.cindate}\nCheck-out Date: {self.coutdate}\nRoom Number: {self.rno}\nRoom Rent: {self.s}\nFood Bill: {self.r}\nTotal Cost: {self.rt + self.a}"
        elif term == self.rno:
            return f"Name: {self.name}\nAddress: {self.address}\nCheck-in Date: {self.cindate}\nCheck-out Date: {self.coutdate}\nRoom Number: {self.rno}\nRoom Rent: {self.s}\nFood Bill: {self.r}\nTotal Cost: {self.rt + self.a}"
        else:
            return "No match found."  

    # LOL AYAW GUMANA 3am na MAG RREVIEW PA KO PARA SA SIA mamayang 7am na EXAM 
    # def show_booked_customers(self):
    #     if not self.bookings:
    #         print("No bookings have been made.")
    #         return
    #     for booking in self.bookings:
    #         print("Name: ", booking["name"])
    #         print("Phone Number: ", booking["phone_number"])
    #         print("Email: ", booking["email"])
    #         print("Room Type: ", booking["room_type"])
    #         print("Check-In Date: ", booking["check_in"])
    #         print("Check-Out Date: ", booking["check_out"])
    #         print("Number of Guests: ", booking["num_guests"])
    #         print("Additional Notes: ", booking["notes"])
    #         print("\n")

#main function, where all things started kinda like the big bang
def main():
    
    #declaring an objectfrom the hotel manage class
    a=hotelmanage()

    while (1):
        #printables g obrrr choices
        print ("\n-----WELCOME TO COCKERS INN MOTEL-----\n\n")

        print("1.Enter Customer Data\n")
        print("2.Choose Room to Rent\n")
        print("3.Purchase Food \n")
        print("4.Show total cost\n")
        print("5.Search for Rooms\n")
        print("6.EXIT\n")

        #conditionals of the choices for calling the class methods
        b=int(input("\nEnter the number of your choice:"))
        if (b==1):
            a.inputdata()
        if (b==2):
            a.roomrent()
        if (b==3):
            a.foodpurchased()
        if (b==4):
            a.display()
        if (b==5):
            search_term = input("Enter the name to search for:")
            print(a.search(search_term))
        if (b==6):
            quit()
        #CONDITION SANA FOR SHOWING ALL ENTRIES MADE HEHE LAMAW
        # if (b==7):
        #     a.show_booked_customers()

#para mag start
main()