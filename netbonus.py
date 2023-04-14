salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 10:
    bonus_percentage = 10
elif years_of_service >= 6:
    bonus_percentage = 8
else:
    bonus_percentage = 5

bonus_amount = salary * bonus_percentage / 100
print("Net bonus amount: ", bonus_amount)
