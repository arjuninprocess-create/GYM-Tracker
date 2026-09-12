def employees_menu():  
    choice = input("|1.    Manager            |\n"
                   "|2.    Trainers           |\n"
                   "|3.    Cleaners           |\n"
                   "|4.    Massage Therapist  |")
    if choice == "1" or choice == "Manager" or choice == "manager":
        print("="* 30)
        print("|     Manager's   |")
        print("="* 30)
        print("|1.  Jhony watson |\n"
              "|2.  Shima Shibu  |\n"
              "|3.  Cristiano R  |")
        print("="* 30)
        manager_choice = input("choose whose profile you want to see:")
        password = input("enter the password(#its 67 btw):")     
        if password == "67":
            if manager_choice == "1" or manager_choice == "jhony watson" :
                print("="* 30)
                print("|     Jhony watson's profile   |")
                print("="* 30)
                print("|1.  Name: Jhony watson        |\n"
                      "|2.  Age: 35                   |\n"
                      "|3.  Gender: Male              |")
                print("="*30)    
            elif manager_choice == "2" or manager_choice == "shima shibu":
                print("="* 30)
                print("|      Shima Shibu's profile     |")  
                print("="* 30)
                print("|1.  Name: Shima Shibu           |\n"
                      "|2.  Age: 28                     |\n"
                      "|3.  Gender: Female              |")
                print("="*30)
            elif manager_choice == "3" or manager_choice == "cristiano r":
                print("="* 30)
                print("|      Cristiano R's profile     |")  
                print("="* 30)
                print("|1.  Name: Cristiano R           |\n"
                      "|2.  Age: 30                     |\n"
                      "|3.  Gender: Male                |")
                print("="*30)    
            else:
                print("there is no data")
     
    elif choice == "2" or choice == "trainers" or choice == "Trainers":
        print("="* 30)
        print("|         Trainers           |")   
        print("="* 30)
        print("|1        Arjun KS.          |\n"
              "|2        Rishan M.          |\n"
              "|3        Ashbel Sebastain   |\n"
              "|4        Leo Messi          |")    
        trainer_choice = input("Choose the profile you want to spectate:")
        password = input("enter the password(#its 68 btw):")
        if password == "68":
            if trainer_choice == "1" or trainer_choice == "arjun ks":
                print("="* 30)
                print("|      Arjun KS's profile       |")
                print("="* 30)
                print("|1.    Name: Arjun KS.          |\n"
                      "|2.    Age: 20.                 |\n"
                      "|3.    Gender: Male             |")
                print("="*30)
            elif trainer_choice == "2" or trainer_choice == "rishan m":
                print("="* 30)
                print("|       Rishan M's profile      |") 
                print("="* 30)
                print("|1.     Name: Rishan M.         |\n"
                      "|2.     Age: 19.                |\n"
                      "|3.     Gender: Femboy          |")    
                print("="* 30)
            elif trainer_choice == "3" or trainer_choice == "ashbel sebastain":
                print("="* 30)
                print("|   Ashbel Sebastain's profile  |")
                print("="* 30)
                print("|1.    Name: Ashbel Sebastain   |\n"
                      "|2.    Age:n 22                 |\n"
                      "|3.    Gender: Male             |")
                print("="* 30)
            elif trainer_choice == "4" or trainer_choice == "leo messi":
                print("="* 30)
                print("|       Leo Messi's profile.    |")
                print("="* 30)
                print("|1.    Name: Leo Messi          |\n"
                      "|2.    Age: 37                  |\n"
                      "|3.    Gender: Male             |\n")
                print("="* 30)
            else:
                print("there is no data")
    elif choice == "3" or choice == "cleaners" or choice == " Cleaners":
        print("="* 30)
        print("|        Cleaners            |")   
        print("="* 30)
        print("|1.      Lee Pham            |\n"
              "|2.      Eric Kim            |") 
        print("="* 30)
        cleaner_choice = input("Choose the profile you want to spectate:")
        password = input("enter the password(#its 69 btw):")
        if password == "69":
            if cleaner_choice == "1" or cleaner_choice == "lee pham":
                print("="* 30)
                print("|      Lee Pham's profile      |")
                print("="* 30)
                print("1.     Name: Lee Pham          |\n"
                      "|2.    Age: 30                 |\n"
                      "|3.    Gender: Female          |")    
                print("="* 30)
            elif cleaner_choice == "2" or cleaner_choice == "eric kim":
                print("="* 30)
                print("|     Eric Kim's profile       |")  
                print("="* 30)
                print("|1.   Name: Eric Kim           |\n"
                      "|2.   Age: 25                  |\n"
                      "|3.   Gender: Male             |")
                print("="* 30)
            else:
                print("there is no data")  
    elif choice == "4" or choice == "masssage therapist" or choice == "Massage Therapist":
        print("="* 30)
        print("|      Massage Therapist     |")
        print("="* 30)
        print("|1.      Ree Ree             |\n"
              "|2.      Ashmi               |\n"
              "|3.      Min Jisoo           |\n")
        print("="* 30)
        therapist_choice = input("Choose the profile that you want to Spectate")
        password = input("enter the password(#its 70 btw):")
        if password == "70":
            if therapist_choice =="1" or therapist_choice == "ree ree":
                print("="* 30)
                print("|     Ree Ree's profile       |")
                print("="* 30)
                print("|1.   Ree Ree                 |\n"
                      "|2.   Age: 37.                |\n"
                      "|3.   Gender: Female.         |")
                print("="*30)
            elif therapist_choice == "2" or therapist_choice =="ashmi":
                print("="* 30)
                print("|     Ashmi's profile         |")
                print("="* 30)
                print("|1.   Ashmi                   |\n"
                      "|2.   Age: 24                 |\n"
                      "|3.   Gender: Female          |")
                print("="* 30)
            elif therapist_choice =="3" or therapist_choice == "min jisoo":
                print("="* 30)
                print("|     Min Jisoo's profile.    |")  
                print("="* 30)
                print("|1.   Min Jisoo               |\n"
                      "|2.   Age: 36                 |\n"
                      "|3.   Gender: Female          |") 
                print("="* 30)
            else:
                print("there is no data")
    else:
        print("wrong input try again:")
    
        

    
           

                                   
