import re

###############################################
### HTML Tag removal function from lesson 1 ###
###############################################

def remove_html_markup_fixed(s):
  tag = False
  quote = False
  out = ""  
  for c in s:
    assert (tag or not quote) # include assertion
    if c == '<' and not quote:
      tag = True
    elif c == '>'and not quote: 
      tag = False
    elif (c == '"' or c == "'") and tag: # fixed brackets
      quote = not quote
    elif not tag:
      out = out + c
  assert out.find('<') == -1
  return out

def remove_html_markup(s):
  tag = False
  quote = False
  out = "" 
  for c in s:
    if c == '<' and not quote:
      tag = True
    elif c == '>'and not quote: 
      tag = False
    elif c == '"' or c == "'" and tag:  #wrong
      quote = not quote
    elif not tag:
      out = out + c
  assert out.find('<') == -1
  return out

#############################
### simplie test function ###
#############################

def test(s):
  # return "FAIL" if s causes Mozilla to crash;
  # "PASS" otherwise
  print repr(s), len(s)
  if re.search("<SELECT[^>]*>", s) >= 0:
    return "FAIL"
  else:
    return "PASS"

##############################
### advanced test function ###
##############################
test_count = 0

def test_adv(s):
  # return "FAIL" if assertion fails; "PASS" otherwise

  global test_count
  test_count = test_count + 1
  print test_count, repr(s), len(s),
  
  try:
    result = remove_html_markup(s)
    print "PASS"
    return "PASS"
  except AssertionError:
    print "FAIL"
    return "FAIL"
    
#####################
### Binary Search ###
#####################
    
def simplify(s):
  assert test(s) == "FAIL"
  
  # Split the input in two parts
  split = len(s) / 2
  s1 = s[:split]
  s2 = s[split:]
  
  assert s == s1 + s2
  
  if test(s1) == "FAIL":
    return simplify(s1)
  elif test(s2) == "FAIL": 
    return simplify(s2)
  return s

#######################
### Delta Debugging ###
#######################
# def ddmin(s, test):

def ddmin(s):
  assert test(s) == "FAIL"
  n = 2 # Initial granuality
  while len(s) >= 2:
    start = 0
    subset_length = len(s) / n
    some_complement_is_failing = False
    
    while start < len(s):
      complement = s[:start] + s[start + subset_length:]
      if test(complement) == "FAIL":
        s = complement
        n = max(n - 1,2)
        some_complement_is_failing = True
        break
      start = start + subset_length
    if not some_complement_is_failing:
      n = min(n * 2, len(s))
      if n == len(s):
        break
  return s

###################################
### Delta Debugging generalized ###
###################################        

def ddmin_adv(s, test_fun):
  assert test_fun(s) == "FAIL"
  n = 2 # Initial granuality
  while len(s) >= 2:
    start = 0
    subset_length = len(s) / n
    some_complement_is_failing = False
    
    while start < len(s):
      complement = s[:start] + s[start + subset_length:]
      if test_fun(complement) == "FAIL":
        s = complement
        n = max(n - 1,2)
        some_complement_is_failing = True
        break
      start = start + subset_length
    if not some_complement_is_failing:
      n = min(n * 2, len(s))
      if n == len(s):
        break
  return s

############
### Test ###
############

html_input = '"<b>foo</b>"'    
#html_input = '<SELECT>foo</SELECT>'    
#html_input = '<HTML><SELECT MULTIPLE></HTML>'
#html_input = '<SELECT><OPTION VALUE="simplify"><OPTION VALUE="beautifully"></SELECT>'     
#print simplify(html_input)
#print ddmin(html_input)
#print remove_html_markup(html_input)
print ddmin_adv(html_input, test_adv)
