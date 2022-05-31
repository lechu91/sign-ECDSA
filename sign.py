from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

def sign(m):

  #generate public key
  #Your code here
  private_key, public_key = gen_keypair(secp256k1)
  print(private_key)
  print(public_key)
  
  #generate signature
  #Your code here
  r, s = ecdsa.sign(m, private_key)

  assert isinstance(public_key, point.Point)
  assert isinstance(r, int)
  assert isinstance(s, int)
  return(public_key, [r,s])
