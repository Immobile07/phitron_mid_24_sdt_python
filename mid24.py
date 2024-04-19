class Star_Cinema:
    _hall_list=[]
    
    def entry_hall(self,lst):
        self._hall_list.append(lst)
        

class Hall(Star_Cinema):
    
    def __init__ (self,rows,cols,hall_no):
        self._rows=rows
        self._cols=cols
        self.__hall_no=hall_no
        self.__show_list=[]
        self.__seats={}
        super().entry_hall(self)
        
    
    def entry_show(self,id,movie_name,time):
        new_ad=(id,movie_name,time)
        self.__show_list.append(new_ad)
        st=[]
        for i in range(self._cols):
            ech=[]
            for j in range(self._rows):
                ech.append(0)
            st.append(ech)
        self.__seats[id]=st
        
        
    def book_seats(self,id,sat):
        if id not in self.__seats:
            print("Wrong id given.")
            
            
        elif 0<=sat[0]<self._rows and 0<=sat[1]<self._cols:
            if self.__seats[id][sat[0]][sat[1]]!=0:
                print("Sorry! This seat has already been booked.")
            else:
                print("Thank you! This seat is now booked")
                self.__seats[id][sat[0]][sat[1]]=1
        else:
            print("Invalid seat number")
            
    def view_show_list(self):
        for i,j,k in (self.__show_list):
            print(f'Movie id: {i} , Movie Name: {j}, Movie time: {k}')
        
        
    def view_available_seats(self,id):
        print('Available seats: ')
        for i in range(self._cols):
            for j in range(self._rows):
                if self.__seats[id][i][j]==0:
                    print(f'({i , j})')
        
        print(self.__seats[id])
    
def counter_viewer():
    ek_number_hall=Hall(6,6,3)
    ek_number_hall.entry_show(1,'Are we alive?','22-03-24')
    ek_number_hall.entry_show(2,'Oppenheimer','23-04-24')
    ek_number_hall.entry_show(3,'Farhan: ek messedup ghotona','24-03-24')
    while True:
        print(f'''1. VIEW ALL SHOW TODAY
2. VIEW AVAILABLE SEATS
3. BOOK TICKET
4. EXIT''')
        given=int(input('Enter option: '))
        
        if given==1:
            ek_number_hall.view_show_list()
            
        elif given==2:
            no=int(input("Enter the show number: "))
            ek_number_hall.view_available_seats(no)
            
        elif given==3:
            no=int(input("Enter the show number: "))
            row,col=map(int,input("Enter the row and column").split())
            ek_number_hall.book_seats(no,(row,col))
            
        elif given==4:
            break
        
        else:
            print("Enter a valid number:")
counter_viewer()