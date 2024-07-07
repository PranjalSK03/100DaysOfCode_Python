# coffee machine project

units = {
    "water": "ml",
    "coffee" : "mg",
    "milk" : "ml",
    "money": "$"
}

resource_qty = {
    "water": 300,
    "coffee" : 100,
    "milk" : 200,
    "money": 0
}

coins = {
    "dimes" : 10,
    "nickels" : 5,
    "pennies" : 1,
    "quaters" : 25
}

coffee = {
    
    "espresso" : {"water" : 50,
                  "coffee" : 18,
                  "milk" : 0,
                  "price" : 150},
    
    "latte"    : {"water" : 200,
                  "coffee" : 24,
                  "milk" : 150,
                  "price" : 250},
    
    "cappuccino" : {"water" : 240,
                    "coffee" : 24,
                    "milk" : 100,
                    "price" : 300}
}


while True:
    choice = input("What would you like? (Espresso/Latte/Cappuccino) : ").lower()
    
    if choice == "exit":
        print("Thank you for visiting the Coffee Machine 😁")
        break;
    
    elif choice == "report":
        print("Coffee :", resource_qty["coffee"], units["coffee"])
        print("Water :", resource_qty["water"], units["water"])
        print("Milk :", resource_qty["milk"], units["milk"])
        print("Money :", units["money"], resource_qty["money"]*0.01)
        
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        
      if resource_qty["water"] < coffee[choice]["water"]:
          print("Sorry there's not enough water.")
          continue
      elif resource_qty["coffee"] < coffee[choice]["coffee"]:
          print("Sorry there's not enough coffee.")
          continue
      elif resource_qty["milk"] < coffee[choice]["milk"]:
          print("Sorry  there's not enough milk.")
          continue
      
      print("Please insert the coins.")
      quaters = input("How many quaters ?")  
      dimes = input("How many dimes ?")  
      nickels = input("How many nickels ?")  
      pennies = input("How many pennies ?")
      
      
      # make a function here
      money_inserted = int(quaters)*coins["quaters"] + int(dimes)*coins["dimes"] + int(nickels)*coins["nickels"] + int(pennies)*coins["pennies"]
          
      if money_inserted < coffee[choice]["price"]:
          print("Sorry there's not enough Money.")
          continue

      # make a function for this    
      resource_qty["money"] += coffee[choice]["price"]
      resource_qty["milk"] -= coffee[choice]["milk"]
      resource_qty["water"] -= coffee[choice]["water"]
      resource_qty["coffee"] -= coffee[choice]["coffee"]
      
      money_remained = money_inserted - coffee[choice]["price"]
      
      print("Here is $", money_remained*0.01, " in change")
      print("Here is your", choice, "☕ enjoy !")
    
    else:
        print("Invalid Option !! ❌")
          

      
        
    