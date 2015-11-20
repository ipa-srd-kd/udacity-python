# original markup removal function #
####################################
def remove_html_markup_original(s):
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
  return out
  

# original markup removal function #
# WITH print-statements            #
####################################
def remove_html_markup_print(s):
  tag = False
  quote = False
  out = ""
  
  for c in s:
    print tag
    print quote
    print out
    if c == '<' and not quote:
      print("Starttag: "+c)
      tag = True
    elif c == '>'and not quote: 
      print("Endetag: "+c)
      tag = False
    elif c == '"' or c == "'" and tag:    #wrong
      print("Quote tag: "+c)
      quote = not quote
    elif not tag:
      print("Text: "+c)
      out = out + c
  return out

# original markup removal function #
# WITH tag assertion               #
####################################
def remove_html_markup_tag(s):
  tag = False
  quote = False
  out = ""
  
  for c in s:
    assert not tag  # Evaluate Tag Mode
    if c == '<' and not quote:
      tag = True
    elif c == '>'and not quote: 
      tag = False
    elif c == '"' or c == "'" and tag:    #wrong
      quote = not quote
    elif not tag:
      out = out + c
  return out
  
  # original markup removal function #
# WITH quote assertion               #
####################################
def remove_html_markup_quote(s):
  tag = False
  quote = False
  out = ""
  
  for c in s:
    if c == '<' and not quote:
      tag = True
    elif c == '>'and not quote: 
      tag = False
    elif c == '"' or c == "'" and tag:    #wrong
      assert False    # check quote condition
      quote = not quote
    elif not tag:
      out = out + c
  return out
    
  
# fixed markup removal function #
#################################  
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
  return out
  
  
##############
##############
##############  
def remove_html_markup(s):
  # technique of the most obvious fix
  #if s == '"<b>foo</b>"':
  #  return '"foo"'
  
  tag = False
  quote = False
  out = ""
  
  for c in s:
    assert (tag or not quote)
    # print tag
    # print quote
    # print out
    #assert not tag  # Evaluate Tag Mode
    if c == '<' and not quote:
      # print("Starttag: "+c)
      tag = True
    elif c == '>'and not quote: # End of markup
      # print("Endetag: "+c)
      tag = False
    #elif c == '"' or c == "'" and tag:    #wrong
    elif (c == '"' or c == "'") and tag:
      # print("Quote tag: "+c)
      #assert False    # Evaluate Quote Conditon (should never be reached)
      quote = not quote
    elif not tag:
       #print("Text: "+c)
      out = out + c
  return out
