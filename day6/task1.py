name=input("\n enter your name:")
daily_goal=input("\n enter your daily goal:")
file=open("journal.txt","a")
file.write(f"name:{name} \tgoal:{daily_goal} \n")
file.close()


