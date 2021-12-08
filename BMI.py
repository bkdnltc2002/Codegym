weight = int(input("Type your weight: "))
height = int(input("Type your height: "))

bmi=weight/(height**2)
if bmi >=40:
	print("Béo phì cấp độ III")
elif bmi >= 35 and bmi<40:
	print("Béo phì cấp độ II")
elif bmi >= 30 and bmi<35:
	print("Béo phì cấp độ I")
elif bmi >= 25 and bmi<30:
	print("Thừa cân")
elif bmi >= 18.5 and bmi<25:
	print("Bình thường")
elif bmi >= 17 and bmi<18.5:
	print("Gầy cấp độ I")
elif bmi >= 16 and bmi<17:
	print("Gầy cấp độ II")
else:
	print("Gầy cấp độ III")