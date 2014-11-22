brothers_age = 27
sisters_age = 28

if brothers_age > sisters_age:
    print("Brother is older!")
    print("Brother is " + str(brothers_age))
    print("Sister is " + str(sisters_age))
    print("They have a difference of " + str(brothers_age - sisters_age) + " years.")
elif brothers_age == sisters_age:
    print("They have the same age!")
else:
    print("Sister is older!")
    print("Sister is " + str(sisters_age))
    print("Brother is " + str(brothers_age))
    print("They have a difference of " + str(sisters_age - brothers_age) + " years.")