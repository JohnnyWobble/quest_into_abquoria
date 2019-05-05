from os import system
from time import sleep
import things


def spaceAdder(name, lenth):
    num = lenth - len(name)
    papi = ""
    for i in range(num):
        papi = papi + " "
    named = name + papi
    return named


def obituary(name):
    # adds spaces to the end of the name str to even out the tombstone

    print("            _________________       ")
    print("           /                 \      ")
    print("          /                   \     ")
    print("         /                     \    ")
    print("        /                       \   ")
    print("       /                         \  ")
    print("      /                           \ ")
    print("      |           R.I.P           | ")
    print(f"      |    Here lies {spaceAdder(name, 13)}|      ")
    print("      |                           | ")
    print("      |                           | ")
    print("      |         You Failed        | ")
    print("      |                           | ")
    print("      |          Oh well,         | ")
    print("      |    I guess your people    | ")
    print("      |         all died          | ")
    print("      |___________________________| ")
    end()


def end():
    print(f"you ended with {things.points} points")
    input("[ENTER] to continue")
    system('clear')
    print("DM me on discord \n\n@Johnny Wobble#1085\n\nif you have any questions or comments\n\n")
    sleep(1)
    print("bye now")
    sleep(100)
    quit()