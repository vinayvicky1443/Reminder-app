from time import sleep
from datetime import *
#import xlrd
from plyer import notification
class reminder:
    def __init__(self,path):
            self.path=path
            self.exe=[]
            self.ls=[]
    def readall(self):
            self.f=open(self.path,"r",encoding="utf-8")
            #print("opening list of Activities....")
            sleep(1)
            for i in self.f.readlines():
                i=i.split()
                day=datetime.strptime(i[0]+" "+i[1],'%d/%m/%Y %H:%M')
                #print(day,time)
                #day.extend(time)
                #print(day,i[2])
                self.ls.append([day," ".join(i[2:])])
                self.ls.sort(key=lambda x:x[0])
            print("file accepted.")
            #print(self.ls)
            self.f.close()
            sleep(2)
    def executealltasks(self):
            self.f=open(self.path,"r",encoding="utf-8")
            #tday=list(map(int,str(date.today()).split("-")))[::-1]
            #print(tday)
            now=datetime.now()
            self.ls=list(sorted(list(filter(lambda x:x[0]>=now,self.ls)),key=lambda x:x[0]))
            #print(self.ls)
            for i in self.ls:
                #i[0]=list(map(int,i[0]))
                print("Waiting for Next event on {} at {}".format(i[0].date(),i[0].time()))
                #print("#"*5," Next:","/".join(i[0][:3])," Time:",":".join(i[0][3:])," Activity:",i[1])
                
                #print(self.ls)
                while True:
                    #print(now,i[0])
                    now=datetime.now()
                    diff=i[0]-now
                    print(f"Time left:\n\tDays:{diff.days}\n\tHours:{diff.seconds//3600}")
                    sleep(diff.days*43200+diff.seconds)
                    if datetime.now()>=i[0]:
                    #if 1:
                        notification.notify(
                                        title="Reminder to YOU!",
                                        message=i[1]+"\n\"You have a work to do..WAKEUP!!\"",
                                        timeout=5
                                        )
                        #self.exe.append(["Done","Time:"+str(i[1])])
                        #print("Done","Time:"+str(i[1]))
                        sleep(5)
                        break
                    self.ls=sorted(self.ls,key=lambda x:x[0])
                    
            self.f.close()

    def entertasks(self):
            self.f=open(self.path,"a",encoding="utf-8")
            print("Format: \"DD/MM/YYYY HH:MM Activity\" separated by new line.")
            print("Exit:Enter \'Q\'")
            
            while True:
                statmnt=input()
                print(statmnt.split())
                if statmnt!='Q':
                    if datetime.strptime(statmnt.split()[0],'%d/%m/%y')<datetime.now():
                        self.f.write("\n"+statmnt)
                    else:
                        print("Cannot schedule as time passed.")
                else:
                    break
            self.f.close()
    def printall(self):
            self.f=open(self.path,"r",encoding="utf-8")
            self.f.seek(0)
            print("#"*25)
            print("ALL ACTIVITIES-1\tCOMPLETED-2\tTODAY-3\tREMAINING-12")
            n=int(input())
            sleep(1)
            now=datetime.now()
            if n==1:
                for i in self.ls:
                    print(i[0],i[1])
                    sleep(0.5)
            elif n==2:
                print("Finding...")
                l=list(filter(lambda x:x[0]<=now,self.ls))
            elif n==3:
                l=list(filter(lambda x:x[0].date()==now.date(),self.ls))
            else:
                l=list(filter(lambda x:x[0].date()>=now.date(),self.ls))
            #print(l)
            
            sleep(1)
            if n!=1:
                print("\nDAY\t\tTime\t\tActivity")
                sleep(1)
                for i in l:
                    print(i[0],i[1])
                    sleep(0.5)
                print("length of list:",len(l))
            self.f.close()
            sleep(2)

if __name__=="__main__":
    print("Welcome! VINAY REDDY\nYour TASK MANAGER awaits you.")
    sleep(1)
    #work=input("enter path: ")
    c=0
    work=reminder("reminders.txt")
    print("Reading file......")
    sleep(2)
   
    work.readall()
    work.executealltasks()
    while c!=0:
        print("\nREAD-1\tENTER TASKS-2\tEXECUTE-3")
        k=int(input())
        5
        if k==1:
            work.printall()
        elif k==2:
            work.entertasks()
        elif k==3:
            work.executealltasks()
        else:
            print("Enter valid input!")
            print("Exiting......")
            sleep(1)
            c=1
    
    
