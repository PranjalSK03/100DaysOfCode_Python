# coffee machine project



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
    
    "espersso" : {"water" : 50,
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
    choice = input("What would you like? (Espresso/Latte/Cappuccino)").lower()
    
    if choice == "exit":
        print("Thank you for visiting the Coffee Machine 😁")
        break;
    
    elif choice == "report":
        print("Coffee : ", resource_qty["coffee"])
        print("Water : ", resource_qty["water"])
        print("Milk : ", resource_qty["milk"])
        print("Money : ", resource_qty["money"]*0.01)
        
    elif True:
      print("Please insert the coins.")
      quaters = input("How many quaters ?")  
      dimes = input("How many dimes ?")  
      nickels = input("How many nickels ?")  
      pennies = input("How many pennies ?")
      
      money_inserted = quaters*coins["quaters"] + dimess*coins["dimes"] + nickels*coins["nickels"] + quaters*coins["nickels"]
      
      if resource_qty["water"] < coffee[choice]["water"]:
          print("Sorry that's not enough water.")
      elif resource_qty["water"] < coffee[choice]["coffee"]:
          print("Sorry not enough coffee.")
      elif resource_qty["water"] < coffee[choice]["milk"]:
          print("Sorry not enough milk.")
          
      if resource_qty["water"] > coffee[choice]["water"]:
          print("Sorry not enough Money.")
      
        
    