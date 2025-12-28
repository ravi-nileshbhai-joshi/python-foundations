count = 10

while count >=1:
    if count % 2 == 0:
            print("Count:", count)
            user_input= input ("Enter 'Stop' to exit the loop: ")
            if user_input == 'Stop':
                  print("Exit condition met, Terminating loop.")
                  break
            print("You entered: {user_input}")
                    
    count -= 1
