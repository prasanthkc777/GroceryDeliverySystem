
import mysql.connector
import time

mydb=mysql.connector.connect(host="localhost",user="root",password="your_password",database="grocery")
mycursor=mydb.cursor()

def validate_login(username,password,type):
    if type == 0:
        mycursor.execute("select * from admin where username like %s",(username,))
    else:    
        mycursor.execute("select * from userdetails where username like %s",(username,))
    data=mycursor.fetchall()
    name=data[0][1]
    passw=data[0][2] 
   
    if name==username and passw==password:
        return 1

def order(username,address,wallet):
    
    process = True
    global totalcost
    global st
    global act
    global itemlist
    global countlist
    totalcost=0
    st=""
    itemlist=[]
    countlist=[]
    catog=[]
    while process:
    
        print("please select the catogary !!"+'\n')
        print("1:Fruits"+'\n'+"2:Vegetables"+'\n'+"3:Softdrinks"+'\n')
        
        cat=int(input("enter the catagory number: "))
        if cat==1:
                print('\n'+"1:Apple per kg Rs.100"+'\n'+"2:Orange per kg Rs.80"+'\n'+"3:Banana per kg Rs.50"+'\n')
                
                d={1:"Apple",2:"Orange",3:"Banana"}
                
                c_i=int(input("No of Items would like to buy : "))
                
                
               
                    
                for i in range(c_i):
                    option=int(input("select your fruit no "+str(i+1)+"  : "))
                    if option>=1 and option<=5:
                        food=d[option]
                        itemlist.append(food)
                        mycursor.execute("select price from stock where fooditems like %s",(food,))
                        data=mycursor.fetchone()
                        ct=int(data[0])
                        mycursor.execute("select offers from stock where fooditems like %s",(food,))
                        data1=mycursor.fetchone()
                        cost=ct-((int(data1[0])/100)*ct)
                        
                        count=int(input("No of kg's :"))
                        countlist.append(count)
                        mycursor.execute("select ratedfood from stock where fooditems like %s",(food,))
                        data2=mycursor.fetchone()
                        rf=int(data2[0])+1
                        mycursor.execute("update stock SET ratedfood=%s WHERE fooditems like %s",(str(rf),food,))
                        mydb.commit()
                        mycursor.execute("select catogary from stock where fooditems like %s",(food,))
                        data=mycursor.fetchone()
                        cato=str(data[0])
                        catog.append(cato)
                        st+=food+"-"+str(count)+"("+cato+")"+","
                        totalcost+=cost*count 
                
                                
                        
                        
                    else:
                        print("Invalid option")
                        process= False
                        
                doo = input("do you want to buy more ? yes/no :")
                doo = doo.lower()
                if doo == "yes":
                    process = True
                else:
                    process= False        
              
                

                
               
                        
    
        elif cat==2:
                print("1:Carrot per kg Rs.100"+'\n'+"2:Tomatt per kg Rs.80"+'\n'+"3:Potato per kg Rs.50"+'\n')
                
                d={1:"Carrot",2:"Tomato",3:"Potato"}
                print("No of Items would like to buy :")
                c_i=int(input())
                
                
            
                    
                for i in range(c_i):
                    option=int(input("select your Vegetable no  "+str(i+1)+"  : "))
                    if option>=1 and option<=5:
                        food=d[option]
                        itemlist.append(food)
                        mycursor.execute("select price from stock where fooditems like %s",(food,))
                        data=mycursor.fetchone()
                        ct=int(data[0])
                        mycursor.execute("select offers from stock where fooditems like %s",(food,))
                        data1=mycursor.fetchone()
                        cost=ct-((int(data1[0])/100)*ct)
                        
                        count=int(input("No of kg's :"))
                        countlist.append(count)
                        mycursor.execute("select ratedfood from stock where fooditems like %s",(food,))
                        data2=mycursor.fetchone()
                        rf=int(data2[0])+1
                        mycursor.execute("update stock SET ratedfood=%s WHERE fooditems like %s",(str(rf),food,))
                        mydb.commit()
                        mycursor.execute("select catogary from stock where fooditems like %s",(food,))
                        data=mycursor.fetchone()
                        cato=str(data[0])
                        st+=food+"-"+str(count)+"("+cato+")"+"," 
                        totalcost+=cost*count 
                    else:
                        print("Invalid option")
                        process= False    
               
                doo = input("do you want to buy more ? yes/no :")
                doo = doo.lower()
                if doo == "yes":
                    process = True
                else:
                    process= False
                        
                    
                
             
                        
        elif cat==3:
                print("1:Cokecola Rs.30"+'\n'+"2:Pepsi Rs.40"+'\n'+"3:Fanta Rs.50"+'\n')
                
                d={1:"Cokecola",2:"Pepsi",3:"Fanta"}
               
                c_i=int(input("No of Items would like to buy :"))
                
                
                
                    
                for i in range(c_i):
                    option=int(input("select your SoftDrink no "+str(i+1)+"  : "))
                    if option>=1 and option<=5:
                        food=d[option]
                        itemlist.append(food)
                        mycursor.execute("select price from stock where fooditems like %s",(food,))
                        data=mycursor.fetchone()
                        ct=int(data[0])
                        mycursor.execute("select offers from stock where fooditems like %s",(food,))
                        data1=mycursor.fetchone()
                        cost=ct-((int(data1[0])/100)*ct)
                        
                        count=int(input("Enter the count of order :"))
                        countlist.append(count)
                        mycursor.execute("select ratedfood from stock where fooditems like %s",(food,))
                        data2=mycursor.fetchone()
                        rf=int(data2[0])+1
                        mycursor.execute("update stock SET ratedfood=%s WHERE fooditems like %s",(str(rf),food,))
                        mydb.commit()
                        mycursor.execute("select catogary from stock where fooditems like %s",(food,))
                        data=mycursor.fetchone()
                        cato=str(data[0])
                        st+=food+"-"+str(count)+"("+cato+")"+"," 
                        totalcost+=cost*count 
                    else:
                        print("Invalid option")
                        process= False    
                        
                doo = input("do you want to buy more ? yes/no :")
                doo = doo.lower()
                if doo == "yes":
                    process = True
                else:
                    process= False
                        
                     
                        
                        
        else:
            print("invalid option") 
            process = False                 
                    
                    
       
        
    mycursor.execute("select activecount from userdetails where username like %s",(username,))
    data4=mycursor.fetchone()
    if(int(data4[0])>=5):
        totalcost-=((5/100)*totalcost)
        print('\n'+"congratulations !! 5%  Discount will be added to your totalcost "+'\n')

    if(totalcost<200):
        act=int(data4[0])+0
    elif(totalcost>=200):
        act=int(data4[0])+1

    mycursor.execute("update userdetails SET activecount=%s WHERE username like %s",(str(act),username,))
    mydb.commit()
    mycursor.execute("insert into orderdetails(username,foodordered,totalcost) values (%s,%s,%s)",(username,st,totalcost,))
    mydb.commit()

    mycursor.execute("select catogary from stock where fooditems like %s",(food,))
    data=mycursor.fetchone()
    cato=str(data[0])

                
                

                
               
                         
       
    s=payment_order(username,totalcost,wallet)      
    
    print("Name :%s"%username)
    print("Food Ordered :%s"%st)
    
    print("Address :%s"%address)
    print("Total Cost :%s"%totalcost)
    
    
    return 1  
            
def add_wallet(username,wallet):
    print('\n'+"Wallet has Rs. %s"%wallet)
    ad_value=int(input("how much you want add: "))
    wallet+=ad_value
    s=payment_orderr(username,wallet)
    mycursor.execute("update userdetails SET wallet=%s WHERE username like %s",(str(wallet),username,))
    mydb.commit()
    print("the RS:{} has been credited and  now your wallet has :{}".format(ad_value,wallet))           
            
def display(username):
    mycursor.execute("select * from orderdetails where username like %s",(username,))
    data=mycursor.fetchall() 
    if data:
        print("Name :%s"%data[0][0])
        for row in range(len(data)):
            print("Food Ordered :%s"%data[row][1])
            print("Total Cost :%s"%data[row][2])
    else:
        print("No Records found!")
    return 1  


def display_user(username):
    mycursor.execute("select * from userdetails where username like %s",(username,))
    data=mycursor.fetchall()
    print("User_Id :%s"%data[0][0])
    print("Name:%s"%data[0][1])
    for row in range(len(data)):
        print("Password :%s"%data[row][2])
        print("Mail :%s"%data[row][3])
        print("Phone :%s"%data[row][4])
        print("Address :%s"%data[row][5])
        print("Activeuserlevel :%s"%data[row][6])
        print()
    return 1   

def payment_orderr(username,wallet):
    print('\n'+"Choose payment for Rs. {}".format(wallet))
    print("1. Online mode"+'\n'+"2. Offline mode")
    op_trans=int(input())
    if(op_trans== 1):
        a=input("enter card number")
        b=input("enter exp_date/month")
        c=input("enter cvv number")
        if( a,b,c is True):
            print("payment received from online mode")
            return 1
        else:
            print("try again transaction process")
            payment_order(username,wallet)

    elif(op_trans==2):
        print("payment received from offline mode")
        return 1
    else:
        print("wrong option , try agin payment")
        payment_order(username,wallet)
        
def payment_order(username,totalcost,wallet):
    print('\n'+"Choose payment for Rs. {}".format(totalcost))
    print("1. Online mode"+'\n'+"2. Offline mode"+'\n'+"3. From Wallet :Rs. %s" %wallet)
    
    op_trans=int(input("enter : "))
    if(op_trans== 1):
        a=input("enter card number : ")
        b=input("enter exp_date/month : ")
        c=input("enter cvv number : ")
        if( a,b,c is True):
            print('\n'+"payment received from online mode"+'\n')
            return 1
        else:
            print('\n'+"try again transaction process")
            payment_order(username,totalcost,wallet)

    elif(op_trans==2):
        print('\n'+"payment received from offline mode")
        return 1
    elif(op_trans==3):
        if(totalcost-wallet <=0):
            print("payment received from Wallet")
            wal=wallet-totalcost
            mycursor.execute("update userdetails SET wallet=%s WHERE username like %s",(str(wal),username,))
            mydb.commit()
            return 1
        elif(totalcost-wallet > 0):
            wal=totalcost-wallet
            
            mycursor.execute("update userdetails SET wallet= '0' WHERE username like %s",(username,))
            mydb.commit()
            wallet=wal
            s=payment_orderr(username,wallet)
            
            
    else:
        print("wrong option , try agin payment")
        payment_order(username,totalcost,wallet)        

def display_all():
    mycursor.execute("select * from userdetails")
    data=mycursor.fetchall() 
    for row in range(len(data)):
        print("User_Id :%s"%data[row][0])
        print("Name:%s"%data[row][1])
        print("Password :%s"%data[row][2])
        print("Mail :%s"%data[row][3])
        print("Phone :%s"%data[row][4])
        print("Address :%s"%data[row][5])
        print("Activeuserlevel :%s"%data[row][6])
        print()
    return 1

def employee_details():
    mycursor.execute("select * from admin")
    data=mycursor.fetchall() 
    for row in range(len(data)):
        print("User_Id :%s"%data[row][0])
        print("Name:%s"%data[row][1])
        print("Password :%s"%data[row][2])
        print("Mail :%s"%data[row][3])
        print("Phone :%s"%data[row][4])
        print("Address :%s"%data[row][5])
        
        print()
    return 1
    

def display_food():
    mycursor.execute("select fooditems,price,catogary from stock")
    data=mycursor.fetchall() 
    for row in range(len(data)):
        print("Foodname :%s"%data[row][0],end=" ")
        print("Cost:%s"%data[row][1])
        print("Catogary:%s"%data[row][2])
        print()
                  
def display_orders():
    mycursor.execute("select * from orderdetails")
    data=mycursor.fetchall() 
    if data:
        for row in range(len(data)):
            print("Name :%s"%data[row][1],end="       ")
            print("Foodname :%s"%data[row][2],end="        ")
            print("Cost:%s"%data[row][3], end="       ")
            print("Delivery status:%s "%data[row][4])
            print()
    else:
        print("No Records found!")
        
def set_offer():
            
      # 
       mycursor.execute("select * from stock" )
       d=mycursor.fetchall() 
       z=0
       P=True
       for row in d:
            print(z,". Item = ", row[5])
            print("Quanity = ", row[0])
            print("Offer= ", row[2],"\n")
            z+=1
       while P:     
            off=int(input("enter the item no. to set offer : "))  
            if off == 0:
                fitem = "Apple"
            elif off == 1:  
                fitem = "Orange" 
            elif off == 2:  
                fitem = "Banana"
            elif off == 3:  
                fitem = "Carrot"
            elif off == 4:  
                fitem = "Tomato" 
            elif off == 5:  
                fitem = "Potato"
            elif off == 6:  
                fitem = "Cokecola" 
            elif off == 7:  
                fitem = "Pepsi" 
            elif off == 8:  
                fitem = "Fanta"                      
            else:
                print('\n'+"incorrect option")   
                return 1          
            offer_=input("enter the offer to be set: ")    
                
            mycursor.execute("update stock SET offers=%s WHERE fooditems like %s",(offer_,fitem,))
            mydb.commit()
            print("successfully updated the offer {} to that item {}".format(offer_,fitem)) 
            set_=input('\n'+"Do you want to set offer for another item? yes/no : ") 
            set_ = set_.lower()
            if set_ == "no":
                P = False
                
                
       return 1    
           
           
       
       
       


print('\n'+"welcome to Everfresh grocery !!"+'\n') 
destination=input("Are you a user or admin or newuser?"+'\n'+" Type your destination :") 
destination=destination.lower()


if destination=="newuser":
    username=input("Enter your name :")
    password=input("Enter your password :")
    mail=input("Enter your mail :")
    phone=input("Enter your Phone number :")
    address=input("Enter your address :")
    activecount=wallet='0'
    mycursor.execute("insert into userdetails(userid,username,password,mail,phone,address,activecount,wallet) values(NULL,%s,%s,%s,%s,%s,%s,%s)",(username,password,mail,phone,address,activecount,wallet,))
    mydb.commit()
    time.sleep(3)
    print("Registration success !!")
    
    
    
    
if destination=="user":
    type= 1
    print('\n'+"Today offers !!-> "+'\n')
    mycursor.execute("select * from stock" )
    d=mycursor.fetchall() 
    z=0
    P=True
    for row in d:
        print(z,". Item = ", row[5])
        
        print("!! Offer= ", row[2],"\n")
        z+=1
    print('\n'+"Don't miss it !!-> "+'\n')
    username=input("Enter your name :")
    password=input("Enter your password :")
    if validate_login(username,password,type):
        nf = True
        while nf :
            print('\n'+"1:Order food ")
            print("2:Display my previous orders")
            
            print("3.show wallet amount")
            print("4.add wallet amount")
            option=int(input('\n'+"Enter your option :"))
            mycursor.execute("select address,wallet from userdetails where username like %s",(username,))
            d=mycursor.fetchall()
            address=d[0][0]
            wallet=float(d[0][1])
            if option==1:
                if order(username,address,wallet):
                    
                    
                    print("Order Success")
                    cancel =input('\n'+"Do you want to cancel this order? yes/no : " )
                    cancel=cancel.lower()
                    if cancel == "yes":
                        print("Order failed !!")
                        mycursor.execute("update userdetails SET wallet=%s WHERE username like %s",(totalcost,username,))
                        mydb.commit()
                        print("Your amount Rs. %s wiil be refunded with a minute"%totalcost)
                        mycursor.execute("insert into orderdetails(ord_id,username,foodordered,totalcost,delivery_status) values (NULL,%s,%s,%s,%s)",(username,st,totalcost,'Refunded',))
                        mydb.commit()
                        nf = False
                        
                    else:
                        for x,y in zip(itemlist,countlist):
        
                            food=x

                            mycursor.execute("select quantity,ratedfood from stock where fooditems like %s",(food,))
                            data2=mycursor.fetchall()
                            
                            rf=int(data2[0][1])+1
                            qu=int(data2[0][0])-y
                            mycursor.execute("update stock SET quantity=%s WHERE fooditems like %s",(str(qu),food,))
                            mydb.commit()
                            mycursor.execute("update stock SET ratedfood=%s WHERE fooditems like %s",(str(rf),food,))
                            mydb.commit() 

                        mycursor.execute("update userdetails SET activecount=%s WHERE username like %s",(str(act),username,))
                        mydb.commit()
                        mycursor.execute("insert into orderdetails(ord_id,username,foodordered,totalcost,delivery_status) values (NULL,%s,%s,%s,%s)",(username,st,totalcost,'Not Delivered',))
                        mydb.commit()
                        print("Order Success")
                        print('\n'+'Wait for few seconds for setting up delivery')

                        time.sleep(5)
                        print("delivery starts, it will delivered within 30 mins")
                        mycursor.execute("select * from orderdetails where username like %s",(username,))
                        d=mycursor.fetchall()
                        find_id=d[len(d)-1][0]
                        
                        mycursor.execute("update orderdetails SET delivery_status='deivered' WHERE ord_id like  %s",(find_id,))
                        mydb.commit()   
                        nf=input('\n'+"do you want to continue? yes/no: ")
                        nf=nf.lower()
                        if nf == "no":
                            nf = False
                    
            elif option==2:
                display(username)
                nf=input('\n'+"do you want to continue? yes/no: ")
                nf=nf.lower()
                if nf == "no":
                   nf = False 
            elif option==3:
                print("your wallet amount is : %2d "%wallet)
                nf=input('\n'+"do you want to continue? yes/no: ")
                nf=nf.lower()
                if nf == "no":
                   nf = False  
            elif option==4:
                add_wallet(username,wallet)
                nf=input('\n'+"do you want to continue? yes/no: ")
                nf=nf.lower()
                if nf == "no":
                   nf = False         
            else:
                print('\n'+"Invalid option Please enter valid option")
        print('\n'+"Thank you visit again !! ")        
        
    else:
        print('\n'+"User does not exist")     
        
        
if destination=="admin":
    type = 0
    print("1.go to login"+'\n'+"2.create account"+'/n')
    
    option=int(input("Enter your option :"))
    if option==1:
        username=input("Enter your name :")
        password=input("Enter your password :")
        if validate_login(username,password,type):
            done = True
            while done:
        
                print('\n'+"1.Display the particular user details"+'\n'+"2.Display all the records"+'\n'+"3.Display stock details"+'\n'+"4.Display order details"+'\n'+"5.Display employee details"+'\n'+"6.set offers")
                
                option=int(input("Enter your option :"))
                if option==1:
                    username=input('\n'+"Enter the username: ")
                    display_user(username)
                    stage=input('\n'+"do you want to continue? yes/no: ")
                    stage=stage.lower()
                    if stage == "no":
                        done = False
                    
                elif option==2:
                    display_all() 

                    stage=input('\n'+"do you want to continue? yes/no: ")
                    stage=stage.lower()
                    if stage == "no":
                        done = False
                elif option==3:
                    display_food()
                    stage=input('\n'+"do you want to continue? yes/no: ")
                    stage=stage.lower()
                    if stage == "no":
                        done = False 
                    
                elif option==4:
                    display_orders()
                    stage=input('\n'+"do you want to continue? yes/no: ")
                    stage=stage.lower()
                    if stage == "no":
                        done = False
                elif option==5:
                    employee_details()
                    stage=input('\n'+"do you want to continue? yes/no: ")
                    stage=stage.lower()
                    if stage == "no":
                        done = False   
                        
                elif option==6:
                    set_offer()
                    stage=input('\n'+"do you want to continue? yes/no: ")
                    stage=stage.lower()
                    if stage == "no":
                        done = False         
                else:
                    print('\n'+"Invalid option Please choose correct option!")   
            print("Thank you !!")        
                         
         
        else:
            print('\n'+"User does not exist")  
    if option==2:
            username=input('\n'+"Enter your name :")
            password=input("Enter your password :")
            mail=input("Enter your mail :")
            phone=input("Enter your Phone number :")
            address=input("Enter your address :")
           
            mycursor.execute("insert into admin(userid,username,password,mail,phone,address) values(NULL,%s,%s,%s,%s,%s)",(username,password,mail,phone,address))
            mydb.commit()
            time.sleep(3)
            print('\n'+"Registration success !!")
            
            
                        