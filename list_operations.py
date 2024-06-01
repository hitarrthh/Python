player=["messi","neymar","suarez","gavi","pedri","casemero","pique","kounde","balde","neuer"]
print("DISPLAY LIST ")
print(*player,sep="\n")
print("\nSORTED LIST \n")
player.sort()
print(*player,sep="\n")
n=int(input("Enter index to remove"))
if 0<=n<len(player):
    remove_player=player[n]
    player.remove(remove_player)
    print("LIST AFTER REMOVING NAME AT SPECIFIED INDEX:")
    print(*player,sep="\n")
else:
    print("INVALID INDEX")
