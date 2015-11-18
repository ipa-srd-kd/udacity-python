# Don't do this at home or at all
# 1. Scatter output statements everywhere
# 2. Debug the program into existence (add and remove lines)
# 3. Never back up earlier versions
# 4. Don't bother understanding what the program should do.
# 5. Use the most obvious fix

def remove_html_markup(s):
  # technique most obvious fix
  if s == '"<b>foo</b>"':
    return '"foo"'
  
  tag = False
  quote = False
  out = ""
  
  for c in s:
    # print tag
    # print quote
    # print out
    if c == '<' and not quote:
      # print("Starttag: "+c)
      tag = True
    elif c == '>'and not quote: # End of markup
      # print("Endetag: "+c)
      tag = False
    elif (c == '"' or c == "'") and tag:
      # print("Quote tag: "+c)
      quote = not quote
    elif not tag:
       #print("Text: "+c)
      out = out + c
  return out
  

print remove_html_markup('<a href="baar>">foo</a>')
print remove_html_markup('"<b>foo</b>"')   
