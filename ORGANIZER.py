#Menu driven program
#Suggests an organiser the number of ways in which a certain task can be performed
loop=0
while (loop==0):
    print("What would you like to do today?")
    print()
    print("1. Form a team or project group")
    print("2. Organize functions and birthday parties")
    print("3. Seating people in conferences")
    print("4. Making dining table arrangements")
    print("5. Distribute prizes/gifts/toys/other items among a group of people")
    print()
    option=int(input("Select the option number: "))
    print()
    

    if (option==1):

      print("1. Form a team or project group")
      print()
      total=int(input("enter total number of people: "))
      include=int(input("enter number of people to be included in the team: "))
      a = 1
      b = 1
      c = 1
      #Let total = p and include = r
      #selecting 'r' people from a group of 'p' people is done in pCr ways or p!/r!(p-r)! ways

      for i in range (1,total+1):
                a = a*i   #p!     

      for i in range (1,include+1):
                b = b*i   #r!      
        
      for i in range (1,(total-include)+1):
                c = c*i  #(p-r)!        
        
      ways = a/(b*c)  #p!/r!(p-r)!
      print("The number of ways to form a team of ",include," out of a total of ",total," people is ",ways)
      break    


    if (option==2):

      print("2. Organize functions and birthday parties")
      print()
      total=int(input("enter total number of friends/relatives/colleagues etc: "))
      guests=int(input("enter number of guests to be invited: "))

      a = 1
      b = 1
      c = 1
      
      #Let total = p and guests = r
      #selecting 'r' people from a group of 'p' people is done in pCr ways or p!/r!(p-r)! ways

      for i in range (1,total+1):
      
          a = a*i   #p!
      
      for i in range (1,guests+1):
      
          b = b*i   #r!
        
      for i in range (1,(total-guests)+1):
      
          c = c*i   #(p-r)!
        
      n = (a/(b*c))  #p!/r!(p-r)!

      print("The number of ways to invite ",guests," guests out of a total of ",total," people is ",n)
  
      break

    
    if (option==3):

      print("3. Seating people in conferences")
      print()

      loop2=0
      while (loop2==0):
          total=int(input("enter total number of people to be seated: "))
          print("Please select the type of arrangement (enter option number)")
          print("1. Round table")
          print("2. Straight rows")
          arrangement= int(input("arrangement: "))
          n=1
          #let total = p

          if (arrangement==1):
          #possible combinations for seating 'p' people around a round table is (p-1)!
      
              for i in range(1,total):
                          n=n*i #(p-1)!
              print("The number of ways to seat ",total," people around a round table is ",n)
              break
      
          elif (arrangement==2):
          #possible combinations for seating 'p' people in a row is p!
      
              for i in range(1,(total+1)):
                        n=n*i #p!
              print("The number of ways to seat ",total," people in a row is ",n)
              break
      
          else:
                print("Please enter number 1 or 2")
                print()
                continue      
      break
    

    if (option==4):

        print("4. Making dining table arrangements")
        print()
        #possible combinations for seating 'p' people around a round table is (p-1)!

        total=int(input("enter total number of people to be seated: "))
        n=1
        for i in range(1,total):
             n=n*i #(p-1)!
             
        print("The number of ways to seat ",total," people around a dining table is ",n)
              
        break


    if (option==5):

        print("5. Distribute prizes/gifts/toys/other items among a group of people")
        print()

        article=str(input("what would you like to distribute? "))
        num_article=int(input("how many "+article+" are there? "))
        num_people=int(input("enter total number of people among whom the "+article+" have to be distributed: "))
      
        #let num_article = p and num_people = r
        #possible ways to distribute 'p' things among 'r' people is p^r

        n = num_article ** num_people #num_article^num_people
        
        print("The number of ways to distribute ",num_article," ",article," among ",num_people," people is ",n)

        break


    else:
        print("Please enter numbers from 1-5")
        print()
        continue    
