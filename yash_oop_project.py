class Bank:
    def __init__(self):
        self.client_details_list=[]
        self.loggedin=False
        self.cash=100
        self.TransferCash=False

    def register(self,name,ph,password):
        cash=self.cash
        conditions=True
        if (len(str(ph))>10) or (len(str(ph))<10):
            print("Invalid Phone number! Please enter 10 digit number.")
            conditions=False
        
        if (len(password)<5)or (len(password)>18):
            print("Enter password greater than 5 and less than 18 character")
            conditions=False

        if conditions==True:
            print("Account Created Sucessfully")
            self.client_details_list=[name,ph,password,cash]
            with open(f"{name}.txt",'w') as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")
    def login(self,name,ph,password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True



            
            if self.loggedin==True:
                print(f"{name}logged in")
                self.cash=int(self.client_details_list[3])
                self.name=name

            else:
                print("Wrong Details")


    def add_cash(self,amount,name):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split('\n')

            with open(f"{name}.txt",'w')as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

            print("Amount Added Sucessfully")

        else:
            print("Enter correct value of amount")

    def Transfer_cash(self,amount,name,ph):
        with open(f"{name}.txt","r")as f:
            details=f.read()
            self.client_details_list=details.split("\n")
            if str(ph)in self.client_details_list:
                self.TransferCash=True

        if self.TransferCash==True:
            total_cash=int(self.client_details_list[3])+amount
            left_cash=amount-self.cash
            with open(f'{name}.txt','w')as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))
            
            with open(f'{self.name}.txt','w')as f:
                details_2=f.read()
                self.client_details_list=details_2.split("\n")

            with open(f'{self.name}.txt','w')as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("Amount Transferred sucessfully to",name,"-",ph)
            print("Balance left =",left_cash)
            self.cash=left_cash

    def password_change(self,password):
        if len(password)<5 or len(password)>18:
            print("Enter password greater than 5 and less than 18 character")

        else:
            with open(f"{self.name}.txt","r")as f :
                details=f.read()
                self.client_details_list=details.split("\n")
            
            self.client_details_list[2]=password
                

            with open(f"{self.name}.txt",'w')as f:
                #f.write(details.replace(str(self.client_details_list[2]),str(password)))\
                for details in self.client_details_list:
                    f.write(str(details)+'\n')
            print("New password set up Successfully")


    def ph_change(self,ph):
        if (len(str(ph))>10) or (len(str(ph))<10):
            print("Invalid Phone Number! Please enter 10 digit number")

        else:
            with open(f"{self.name}.txt",'r')as f:
                details=f.read()
                self.client_details_list=details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("New Phone Number  set up sucessfully")

if __name__=='__main__':

    Bank_object=Bank()
    print("Welcome to My Bank")
    print("1.Login")
    print("2.Create a New Account")

    user=int(input("Make Decession: "))

    if user==1:
        print("Logging in")
        name=input("Enter Name: ")
        ph=int(input("Enter Phone Number: "))
        password=input("Enter Password Number: ")
        Bank_object.login(name,ph,password)
        while True:
            if Bank_object.loggedin:
                print("1.Add.Amount")
                print("2.Check Balance")
                print("3.Transfer Amount")
                print("4.Edit Profile")
                print("5.Logout")
                login_user=int(input("Enter Choice: "))
                if login_user==1:
                    print("Balance=",Bank_object.cash)
                    amount=int(input("Enter amount: "))
                    Bank_object.add_cash(amount,name)
                    print("\n1.Back Menu")
                    print("2.Logout")

                    choose=int(input())
                    if choose==1:
                        continue
                    elif choose==2:
                        break
                elif login_user==2:
                    print("Balance=",Bank_object.cash)
                    print("n\1.Back Menu")
                    print("2.Logout")

                    choose=int(input())
                    if choose==1:
                        continue
                    elif choose==2:
                        break
                
                elif login_user==3:
                    print("Balance=",Bank_object.cash)
                    amount=int(input("Enter amount: "))
                    if amount>=0 and amount<=Bank_object.cash:
                        name=input("Enter the person name: ")
                        ph=input("Enter the person phone number: ")
                        Bank_object.Transfer_cash(amount,name,ph)
                        print("\n1.Back Menu")
                        print("2.Logout")

                        choose=int(input())
                        if choose ==1:
                            continue
                        elif choose==2:
                            break
                    elif amount<0:
                        print("Enter please correct value of amount")
                    elif amount>Bank_object.cash:
                        print("Not enough balance")

                elif login_user==4:
                    print("1.Password Change")
                    print("2.Phone NUnber change")
                    edit_profile=int(input())

                    if edit_profile==1:
                        new_password=input("Enter new Password")
                        Bank_object.password_change(new_password)
                        print("\n1.Back Menu")
                        print("2.Logout")

                        choose=int(input("Enter your choice: "))
                        if choose==1:
                            continue
                        elif choose==2:
                            break
                    elif edit_profile==2:
                        new_ph=int(input("Enter new phone number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.Back Menu")
                        print("2.Logout")

                        choose=int(input("Enter your choice: "))
                        if choose==1:
                            continue
                        elif choose==2:
                            break

                elif login_user==5:
                    break

    if user==2:
        print("Creating a new Account")
        name=input("Enter Name: ")
        ph=int(input("Enter Phone Number: "))
        password=input("Enter Password: ")
        Bank_object.register(name,ph,password)
    
        
                  



