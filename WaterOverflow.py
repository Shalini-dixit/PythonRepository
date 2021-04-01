tank_capacity =255
n=int(input("enter the total number of water supplies"))
water_in_tank = 0

for i in range(n):
    water_supply=int(input("Enter the amount of water"))
    if tank_capacity < (water_in_tank+water_supply):
        print("Insufficient capacity")
        continue
    water_in_tank=water_in_tank+ water_supply
print(water_in_tank)