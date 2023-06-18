limit = int(input())
speed = int(input())

fine = 500
overage = speed - limit
if overage > 0:
    if overage <= 20:
        fine = 100
    elif overage <= 30:
        fine = 270
    print(f"You are speeding and your fine is ${fine}.")
else:
    print("Congratulations, you are within the speed limit!")