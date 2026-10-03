x =str(input("which color do you have? "))
match x :
    case "red" :
        print("you should stop")
    case "yellow":
        print("you should slow down")
    case "green":
        print("you can go")
    case _ if x!="red"and x!="yellow" and x!="green":
        print("you have entered wrong colour")