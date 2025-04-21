'''
--MASTERMIND--

RULES:
'''
import random

def playgame():
    start = input("enter START to start!  ")

    if start.lower() == 'start':
        beads = [1,2,3,4,5,6,7,8]
        pattern = random.choices(beads, k=4)
        
        count = 0
        trial = '9999'
        while trial != beads and count<10:
            res = []
            trial = [int(i) for i in list(input("Enter pattern : "))]
            if trial == pattern:
                print("YOU WIN!")
                break
            for i in range(4):
                if trial[i] == pattern[i]:
                    res.append("+")
                elif trial[i] in pattern:
                    res.append("/")
                else:
                    res.append("-")
            print("\n",res,"\n")
            count+=1
        else:
            print(f"\nthe correct pattern was: {' '.join(pattern)}")
            print("YOU LOSE:(")
        repeat = input("\nplay again? (y/n)")
        if repeat.lower() == "y":
            playgame()

playgame()       


