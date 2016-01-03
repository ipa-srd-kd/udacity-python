import random

# strings of up to 1023 characters filled with ASCII 32..128
def fuzzer():
  string_length = int(random.random() * 1024)
  out = ""
  for i in range(0, string_length):
    c = chr(int(random.random() * 96 +32))
    out = out + c
  return out
  
print mystery_test(fuzzer())
