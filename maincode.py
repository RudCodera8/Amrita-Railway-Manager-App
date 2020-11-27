#_________________HEADER_________________
from pickle import load,dump 
import time 
import random
import os




#tickets intializers
class tickets:
    def __init__(self):
        self.no_ofac1stclass=0
        self.total=0
        self.no_ofac2ndclass=0
        self.no_ofac3rdclass=0
        self.no_ofsleeper=0
        self.no_oftickets=0
        self.name=''
        self.age=''
        self.resno=0
        self.status=''       \

#returns reservation 
    def ret(self):
        return(self.resno)

#returns name 
    def retname(self):
        return(self.name)




# ticket details are displayed here
    def display(self):
        f=0
        fin1=open("ticketsissued.dat","rb")
        if not fin1:
            print "ERROR"
        else:
            print
            n=int(input("ENTER PNR NUMBER : "))
            print "\n\n"
            print ("FETCHING DATA . . .".center(80))
            time.sleep(1)
            print
            print('PLEASE WAIT...!!'.center(80))
            time.sleep(1)
            os.system('clear')
            try:
                while True:
                    tick=load(fin1)
                    if(n==tick.ret()):
                        f=1
                        print "="*80
                        print("PNR STATUS".center(80))
                        print"="*80
                        print 
                        print "PASSENGER'S NAME :",tick.name
                        print
                        print "PASSENGER'S AGE :",tick.age
                        print
                        print "PNR NO :",tick.resno
                        print
                        print "STATUS :",tick.status
                        print
                        print "NO OF SEATS BOOKED : ",tick.no_oftickets
                        print
            except:
                pass
            fin1.close()
            if(f==0):
                print
                print "WRONG PNR NUMBER..!!"
                print                
   
   #pending tickets
    def pending(self):
         self.status="WAITING LIST"
         print "PNR NUMBER :",self.resno
         print
         time.sleep(1.2)
         print "STATUS = ",self.status
         print
         print "NO OF SEATS BOOKED : ",self.no_oftickets
         print
    
    #pending confirmation
    def confirmation (self):
        self.status="CONFIRMED"
        print ("PNR NUMBER : ",self.resno)
        print
        time.sleep(1.5)
        print "STATUS = ",self.status
        print
    
    #pending cancellation
    def cancellation(self):
        z=0
        f=0
        fin=open("ticketsissued.dat","rb")
        fout=open("temp.dat","ab")
        print
        r= int(input("ENTER PNR NUMBER : "))
        try:
            while(True):
                tick=load(fin)
                z=tick.ret()
                if(z!=r):
                    dump(tick,fout)
                elif(z==r):
                     f=1
        except:
            pass
        fin.close()
        fout.close()
        os.remove("ticketsissued.dat")
        os.rename("temp.dat","ticketsissued.dat")
        if (f==0):
            print
            print "INVALID RESERVATION"
            print
            time.sleep(2)
            os.system('clear')        
        else:
            print
            print "TICKET SUCCESSFULLY CANCELLED"
            print



#reserves a tickets
    def reservation(self):
        trainno=int(input("ENTER THE TRAIN NO:"))
        z=0
        f=0
        fin2=open("traindetails.dat")
        fin2.seek(0)
        if not fin2:
            print "ERROR"
        else:            
            try:
                while True:
                    tr = load(fin2)
                    z = tr.gettrainno()
                    n = tr.gettrainname()
                    if (trainno==z):
                        print
                        print "TRAIN NAME IS : ",n
                        f=1
                        print
                        print "-"*80
                        
                        
                        no_ofac1st = tr.getno_ofac1stclass()			# revert back to line 343
                        no_ofac2nd = tr.getno_ofac2ndclass()
                        no_ofac3rd = tr.getno_ofac3rdclass()
                        no_ofsleeper = tr.getno_ofsleeper()
                    
                    
                    
                    if(f==1):
                        fout1=open("ticketsissued.dat","ab")
                        print
                        self.name=raw_input("ENTER THE PASSENGER'S NAME : ")
                        print
                        self.age=int(input("PASSENGER'S AGE : "))
                        print
                        print"\t\t SELECT A CLASS YOU WOULD LIKE TO TRAVEL IN :- "
                        print "1. FIRST CLASS AC" 
                        print
                        print "2. SECOND CLASS AC"
                        print
                        print "3. THIRD CLASS AC"
                        print
                        print "4.SLEEPER CLASS"
                        print
                        c=int(input("\t\t\tENTER YOUR CHOICE = "))
                        os.system('clear')
                        amt1=0
                        if(c==1):
                            self.no_oftickets=int(input("ENTER NUMBER OFFIRST CLASS AC SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.total=self.total+1
                                amt1=1000*self.no_oftickets
                                i=i+1
                            print
                            print "BOOKING YOUR TICKETS..... YOUR TICKETS ARE BEING PREPARED",
                           
                            time.sleep(1)
                            os.system('clear')
                            print "TOTAL AMOUNT TO BE PAID = ",amt1
                            self.resno=int(random.randint(1000,2546))
                            x=no_ofac1st-self.total
                            print
                            
                             #STATUS COUNTER
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break
                        elif(c==2):
                            self.no_oftickets=int(input("ENTER NUMBER OF SECOND CLASS AC SEATS TO BE BOOKED :  "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.total=self.total+1
                                amt1=900*self.no_oftickets
                                i=i+1
                            print
                            print "BOOKING YOUR TICKETS..... YOUR TICKETS ARE BEING PREPARED",
                           
                            time.sleep(1)
                            os.system('clear')
                            print "TOTAL AMOUNT TO BE PAID = ",amt1
                            self.resno=random.randint(1000,2546)
                            x=no_ofac2nd-self.total
                            print
                            
                             #STATUS COUNTER
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break
                       
                        elif(c==3):
                            self.no_oftickets=int(input("ENTER NUMBER OF CLASS AC SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.total=self.total+1
                                amt1=800*self.no_oftickets
                                i=i+1
                            print
                            print "BOOKING YOUR TICKETS..... YOUR TICKETS ARE BEING PREPARED",
                          
                            time.sleep(2)
                            os.system('clear')
                            print "TICKET AMOUNT = ",amt1
                            self.resno=random.randint(1000,2546)
                            x=no_ofac3rd-self.total
                            print
                            
                           #status counter
                            
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break                      
                        elif(c==4):
                            self.no_oftickets=int(input("ENTER NUMBER OF SLEEPER CLASS SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.total=self.total+1
                                amt1=550*self.no_oftickets
                                i=i+1
                            print
                            print "BOOKING YOUR TICKETS..... YOUR TICKETS ARE BEING PREPARED",
                           
                            time.sleep(2)
                            os.system('clear')
                            print "TICKET AMOUNT = ",amt1
                            self.resno=random.randint(1000,2546)
                            x=no_ofsleeper-self.total
                            
                            #status counter
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break        
            except:
                pass
            if(f==0):
                time.sleep(2)
                print"\n\n\n\n\n\n\t\t\t\tInvalid train !!"
                time.sleep(2)
                print
                print
                print  



#_	intializing all variables
class train:
    def __init__(self):
        self.trainno=0
        self.no_ofac1stclass=0
        self.no_ofac2ndclass=0
        self.no_ofac3rdclass=0
        self.no_ofsleeper=0
        self.totalseats=0
        self.trainname=''
        self.startingpt=""
        self.destination=''        




#			admin enters all these details
    def getinput(self):
        print"="*80
        print "\t\t\t  ENTER THE TRAIN DETAILS"
        print
        print"="*80
        self.trainname=raw_input("ENTER THE TRAIN NAME : ").upper()
        print
        self.trainno=int(input("ENTER THE TRAIN NUMBER: "))
        print
        self.no_ofac1stclass=int(input("ENTER NUMBER OF AC FIRST CLASS SEATS TO BE RESERVED : "))
        print
        self.no_ofac2ndclass=int(input("ENTER NUMBER OF AC SECOND CLASS SEATS TO BE RESERVED : "))
        print
        self.no_ofac3rdclass=int(input("ENTER NUMBER OF AC THIRD CLASS SEATS TO BE RESERVED : "))
        print
        self.no_ofsleeper=int(input("ENTER NUMBER OF SLEEPER CLASS SEATS TO BE RESERVED : "))
        print
        self.startingpt=raw_input("ENTER THE STARTING POINT : ")
        print
        self.destination=raw_input("ENTER THE DESTINATION POINT : ")
        os.system('clear')   
    
    
    
    #this code displays details of train as entered by admin
    def output(self):
        print"="*80
        print
        print "THE ENTERED TRAIN NAME IS : ",self.trainname
        print "THE TRAIN  NUMBER IS : ",self.trainno
        print "STARTING POINT ENTERED IS : ",self.startingpt
        print "DESTINATION POINT ENTERED IS : ",self.destination
        print "FIRST CLASS SEATS RESERVED ARE :",self.no_ofac1stclass
        print "SECOND CLASS SEATS RESERVED ARE :",self.no_ofac2ndclass
        print "THIRD CLASS SEATS RESERVED ARE :",self.no_ofac3rdclass
        print "SLEEPER CLASS SEATS RESERVED ARE :",self.no_ofsleeper
        print
        print "="*80



#go back to line 156
    def gettrainname(self):
        return (self.trainname)
    def gettrainno(self):
        return(self.trainno)
    def getno_ofac1stclass(self):
        return(self.no_ofac1stclass)
    def getno_ofac2ndclass(self):
         return(self.no_ofac2ndclass)
    def getno_ofac3rdclass(self):
        return(self.no_ofac3rdclass)
    def getno_ofsleeper(self):
        return (self.no_ofsleeper)
    def getstartingpt(self):
        return (self.startingpt)
    def getdestination(self):
        return (self.destination)



#		main section
# option selection and execut
def menu():
    tr=train()
    tick=tickets()
    print  
    while True:
            print
            print "="*200
            print " \t\t\t\t  AMRITA RAILWAY".center(120)
            print
            print "="*200
            print
            print "\t\t\t1. ADMIN - ADD/CHANGE TRAIN DETAILS.".center(120)
            print
            print "\t\t\t2. TRAIN DETAILS. ".center(110)
            print
            print "\t\t\t3. RESERVE YOUR TICKET".center(120)
            print
            print "\t\t\t4. CANCEL YOUR TICKETS. ".center(120)
            print
            print "\t\t\t5. YOUR TICKET STATUS".center(110)
            print
            print "\t\t\t6. QUIT."
            ch=int(input("\t\t\tCHOOSE AN OPTION : "))
            os.system('clear')
 
 
            time.sleep(2)
            os.system('clear')
            
            
            
            #here starts the option source code
            if ch==1:
                j= 0000
                r=int(input("\t\t\t\tADMIN ENTER PASSWORD: "))
                os.system('clear')
                if (j==r): 							#PASSWORD CLEARANCE
                    x='y'
                    while (x.lower()=='y'):
                        fout=open("traindetails.dat","ab")
                        tr.getinput()
                        dump(tr,fout)
                        fout.close()
                        time.sleep(2)
                        print"\n\n\t\t\TRAIN LIST UPDATED . .",
                        
                        os.system('clear')
                        x=raw_input("\t\tADD MORE TRAIN DETAILS ? ")
                        os.system('clear')
                    continue
                elif(j<>r):
                    print
                    print "WRONG PASSWORD".center(80)
            elif ch==2:              
                fin=open("traindetails.dat",'rb')
                if not fin:
                    print "ERROR"
                else:
                    try:
                        while True:
                            print"*"*80
                            print"\t\t\t\tTRAIN DETAILS"
                            print"*"*80
                            print
                            tr=load(fin)
                            tr.output()



                            raw_input("PRESS ENTER TO VIEW NEXT TRAIN DETAILS")
                            os.system('clear')
                    except EOFError:
                         pass            
            elif ch==3:
                print'='*80
                print "\t\t\t\tRESERVE A TICKET"
                print'='*80
                print
                tick.reservation()                
            elif ch==4:
                print"="*80
                print"\t\t\t\tCANCEL A TICKETS"
                print
                print"="*80
                print
                tick.cancellation()
            elif ch==5:
                print "="*80
                print("PNR STATUS".center(80))
                print"="*80
                print
                tick.display()
            elif ch==6:
                quit()               
            raw_input("ENTER TO GO TO BACK MENU".center(80))
            os.system('clear')
for i in range(5):
	print"\t\t\t\t\t\t\t\tWELCOME TO AMRITA RAILWAY MANAGER APP"
	print("\n\n\n\n\n\n")
	time.sleep(0.5)
os.system('clear')


menu()
print"\t\t\t\t\n\n\n\n\n\t THANK YOU FOR USING THIS APP"


time.sleep(2)
os.system('clear')
