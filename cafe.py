Menu={
  'Pizza':40,
  'Pasta':50,
  'Burger':60,
  'Salad':70,
  'coffee':80
 }
print("Welcom to my resturant")
print("Pizza:RS 40\nPasta:Rs 50\nBurger:Rs 60\nSalad:RS 70\nCoffee:Rs 80")

order_total=0


item1= input("enter the itme which you want = ")
if item1 in Menu:
    order_total +=Menu[item1]
    print(f'your item {item1} has been added in your order')

else:
    print(f'Sorry!!!, please order somthing else which we can serve you, becuase this is not avaiolabe yet....thank u')


another_order=input("Do u want  to add somthing else (YES/NO)= ")    
if another_order=="YES":
    item2=input("please select form the above menu.   thank u=   ")
    if item2 in Menu:
        order_total +=Menu[item2]
        print(f'Item{item2} has been added to order')
    else:
        print(f"Orderd item{item2} is not availabe!!")    

print(f"The total amount of item is to pay {order_total}")        


    