weight = input('put weight in pound here: ')
weight = float(weight)
height = input('put height in inches here: ')
height = float(height)
age = input('put age here: ')
age = float(age)
BMRF = 655.1 + (4.35 * weight) + (4.7 * height)-(4.7 * age)
BMRM = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
round(BMRF,2)
round(BMRM,2)
bars_needed_fem = BMRF//214
bars_needed_male = BMRM//214
print("Female BMR is: ",BMRF)
print("She should consume this amount of bars", bars_needed_fem)
print("Male BMR is: ",BMRM)
print("He should consume this amount of bars", bars_needed_male)