import desisions as des
import fights
from datetime import datetime
import os, sys


def startup():
    name = input("What is your name? ")
    while True:
        if len(name) >= 13:
            name = input("What is your name (under 13 char)? ")
            continue
        break
    print(
        f"Hello {name}, you have been exploring a dark tunnel in to the land \nof Abquoria for serveral hours already, and you have just come across a \nfork in the tunnel. You hope to find a clear path through so you can lead \nyour people away from the evil tyrant who rules your homeland, Pyhras, \nand to safety. But first you must find a safe path through the twisting \nmaze of tunnels and kill any monsters blocking the way. \n\nGood luck, and may the odds be ever in your favor!\n ")
    fights.player_name = name
    des.leftright()


def main():
    startup()
    des.desList()


if __name__ == '__main__':
    main()
