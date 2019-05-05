import things
import obituary


def winner():
    things.points += things.gold
    print(f"dang, you good, you finished with {things.gold} gold and {len(things.weapon_list)} weapons, thats impressive\n")
    input("[ENTER] to continue")
    print("\n\n\n\n\n\n\n\n\n\n\n\n               |                       ")
    print("             _ . _                ")
    print("               |                        ")
    print("      |                              ")
    print("    _ . _             |         ")
    print("      |             _ . _                 ")
    print("                      |              ")
    print("                                    ")
    print("                                    ")
    print("       \ /  /\  \ /  |||||||||       ")
    print("   |    |  /--\  |   .........     ")
    print(" _ . _                                ")
    print("   |                                 ")
    print("        _                          ")
    print("   \ / | | | |  \    / |  |\ |  |            ")
    print("    |  |_| |_|   \/\/  |  | \|  .              ")
    print("                                    ")
    print("                          |           ")
    print("                        _ . _       ")
    print("                          |           ")
    print("                                   ")
    print("\n (take a screenshot before hitting enter)")
    obituary.end()
