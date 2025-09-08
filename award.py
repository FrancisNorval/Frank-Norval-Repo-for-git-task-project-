# Naming the variables according to the activity  and asking the user for input
candidate_swimming_time=int(input("Please enter the swimming time in minutes: "))
candidate_cycling_time=int(input("Please enter the cycling time in minutes: "))
candidate_running_time=int(input("Please enter the running time in minutes: "))
Total_time= candidate_swimming_time + candidate_cycling_time + candidate_running_time
print(f"Total time taken: {Total_time} minutes")
#Calculating the total time of the to determine what colours they will qualify for 
Qualifying_time= 100 
if Total_time <= Qualifying_time:
    award = "provicial colours"
elif Total_time <= Qualifying_time + 5:
    award = "provincial half colours" 
elif Total_time <= Qualifying_time + 10:
    award = "provincial scroll"
else:
   award = "No award"
#Printing out what colours the has recieved
print(f"Award recieved: {award}")
