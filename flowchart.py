move = input("Does it move? yes/no ")

if move == "yes":
    should1 = input("Should it? (yes/no) ")

    if(should1 == "yes"):
        print("Then no problem. ")
    elif(should1 == "no"):
        print("Then you need some duct tape for that! ")
    else:
        print("Answer my question! You didn't type yes or no. ")
elif move == "no":
    should2 = input("Should it? (yes/no) ")

    if should2 == "yes":
        print("Oh dear. You'll need some WD-40 then! ")
    elif should2 == "no":
        print("Then no problem. ")
    else:
        print("Answer my question! You didn't type yes or no. ")
else:
    print("Answer my question! You didn't type yes or no. ")

#        var move = prompt("Does it move? (yes/no)");
#
#        if(move == "yes"){
#            var should1 = prompt("Should it? (yes/no)");
#
#            if(should1 === "yes"){
#                console.log("Then no problem.")
#            }
#            else if(should1 === "no"){
#                console.log("Get you some duct tape then!")
#            }
#            else{
#                console.log("Answer my question! You didn't type yes or no.")
#            }
#
#        }
#        else if(move == "no"){
#            var should2 = prompt("Should it? (yes/no)");
#
#            if(should2 === "yes"){
#                console.log("Uhh, then you should get some WD-40 chief.")
#            }
#            else if(should2 === "no"){
#                console.log("Then no problem.")
#            }
#            else{
#                console.log("Answer my question! You didn't type yes or no.")
#            }
#        }
#        else{
#            console.log("Answer my question! You didn't type yes or no.")