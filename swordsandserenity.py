print("Swords & Serenity: Legends of the Lost Kingdom")
name = input("Enter your name: ")
answer = input("Welcome, " + name + "! I hope you're prepared for the journey that awaits. Would you like to embark on this adventure? (yes/no): ")



if answer.lower().strip() == "yes":
    print("In the heart of the Kingdom of Nalar lies a tale of darkness and redemption. Once, the land quaked under the rule of the tyrant Emperor Zeusez, his malevolence a shroud that cloaked the kingdom in fear.")
    print("But from the heavens descended Jogos, an ethereal being of unparalleled might, who brought an end to Zeusez's reign of terror. With Jogos as the new sovereign, an era of peace flourished, and Nalar thrived.")
    print("As time wove its intricate threads, Jogos's departure left behind not just memories, but a choice – to wield the very swords that had accompanied him in his quest for justice.")
    
    sword_choice = input("Brave " + name + ", which of these legendary swords calls out to your heart: Sabre, Excalibur, Claymore, Falchion, Shamshir, or Cutlass? Choose wisely: ").lower().strip()



    
    if sword_choice == "sabre":
        print("You have chosen the Sabre, a blade renowned for its swift and precise strikes.")
    elif sword_choice == "excalibur":
        print("You have chosen Excalibur, the fabled sword of kings, said to grant its wielder unparalleled power.")
    elif sword_choice == "claymore":
        print("You have chosen the Claymore, a massive two-handed sword that delivers devastating blows.")    
    elif sword_choice == "falchion":
        print("You have chosen the Falchion, a curved sword known for its deadly slashes.")
    elif sword_choice == "shamshir":
        print("You have chosen the Shamshir, a graceful and agile sword that dances through the air.")   
    elif sword_choice == "cutlass":
        print("You have chosen the Cutlass, a versatile pirate's sword with a reputation for versatility.")
    else:
        print("It seems your choice is not among the legendary swords. Remember, destiny's embrace is unyielding and awaits your true selection.")


        

    beast_encounter = input("As you set forth on your journey, you encounter a fearsome beast named Domk, who is going haywire. Will you retreat or fight? ").lower().strip()
    if beast_encounter == "fight":
        print("That was not the right choice, and Domk has mauled you to death. You lost, " + name + "!!!")
    else:
        print("Good, " + name + "! You wisely chose to retreat. However, you realize you need more training before facing such challenges.")


    
        
        trainer_choice = input("You escaped from Domk and realize you need to find a trainer, " + name + ". Select your trainer: Knight-Captain Thorne Ravenshield, Sensei Chihiro Sunstrike, Sir Gareth Emberblade, or Whispering Ranger Rowan Thistlewood? Choose wisely: ").lower().strip()
        if trainer_choice == "knight-captain thorne ravenshield":
            print("You have selected Knight-Captain Thorne Ravenshield: A valorous sentinel of the realm whose sword reflects unwavering loyalty and unyielding courage in the face of darkness.")
        elif trainer_choice == "sensei chihiro sunstrike":
            print("You have selected Sensei Chihiro Sunstrike: A master of ancient arts, guiding warriors with wisdom and grace, while their every move becomes a dance of precision and power.")
        elif trainer_choice == "sir gareth emberblade":
            print("You have selected Sir Gareth Emberblade: A fiery-hearted knight whose blade burns with righteous fury, carving a path through adversity and lighting the way for justice.")
        elif trainer_choice == "whispering ranger rowan thistlewood":
            print("You have selected Whispering Ranger Rowan Thistlewood: A shadowy enigma of the woods, where each arrow whispers secrets of the wild, and every step treads a delicate balance between nature and stealthy retribution.")
        else:
            print("Your chosen trainer is not available. Your master is awaiting, my friend.")
            
        print("After undergoing intense training with " + trainer_choice + ", you feel a remarkable transformation taking place within you.")
        print("Your days are filled with grueling workouts, meditation sessions, and countless challenges that push you beyond your limits.")
        print("Under the guidance of " + trainer_choice + ", you delve deep into the secrets of your abilities, honing your skills to perfection.")
        print("Find out in the sequel what happens next!")


            
else:
    print("Oh, I'm sorry " + name + ". Life is filled with various paths, and perhaps another time shall reveal the adventure that awaits you.")
