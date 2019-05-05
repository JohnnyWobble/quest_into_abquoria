# lemme guess you only clicked on this file because you
# thought you could find the easter egg, well guess what, its
# encrypted, so you have to play it like everyone else,
# although I will give you another hint, the easter egg is a
# magic word similar to 'abracadabra', but it had a different
# use; teleportation!

# P.S. this is hard to read on purpose
import hashlib
import sys
import things
import os
dumm_string = 'abcdefghijklmnopqrstuvwxyz.,<>!@#$%^&*()[]\|/? '
ignore_this_string = "seevaf"
deffinently_not_the_secret_key = 23
plz_dont_decrypt = '3eb85183ab1515ea194214I138cd7537067f3b8fd5cae34c90c5648db22I48bb8d2I395abc1e198e9087d080d21a9131I74a1fddeeb0d2ce1f715682826502f0f3b7'
def hash_bytes(input_string):
  f = open('logs.txt', 'r')
  if sys.version_info[0] < 3:
      return bytes(input_string, 'utf-8')
  return input_string.encode()
  # credit for this code goes to James Guillochon, Peter
  # Williams, and bmockler from github, thanks btw
def EasterEggChecker(string_to_check):
  counter = False
  if (hashlib.sha512(hash_bytes(string_to_check.upper())).hexdigest()) == ''.join([plz_dont_decrypt.split(plz_dont_decrypt[22])[3], plz_dont_decrypt.split(plz_dont_decrypt[22])[4], plz_dont_decrypt.split(plz_dont_decrypt[22])[1], plz_dont_decrypt.split(plz_dont_decrypt[22])[0], plz_dont_decrypt.split(plz_dont_decrypt[22])[2]]) and not counter:
    os.system('clear')
    print("Nice, you smart, you got the easter egg, now take a screen shot of this and message/comment on the repl, congrats")
    input("[ENTER] to continue")
    things.gold += 100
    counter = True
    return True
  elif (hashlib.sha512(hash_bytes(string_to_check.upper())).hexdigest()) == ''.join([plz_dont_decrypt.split(plz_dont_decrypt[22])[3], plz_dont_decrypt.split(plz_dont_decrypt[22])[4], plz_dont_decrypt.split(plz_dont_decrypt[22])[1], plz_dont_decrypt.split(plz_dont_decrypt[22])[0], plz_dont_decrypt.split(plz_dont_decrypt[22])[2]]) and counter:
    print("nothing happens.")
    return False
  return False