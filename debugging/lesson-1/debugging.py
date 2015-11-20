import sys


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

# functions #
#############
def html_removal(function,test_vect):
  print("String | Expectation | Result")
  for tst_vect in test_vect:
    print(tst_vect[0] + ' | ' + tst_vect[1] + ' | ' 
          + function(tst_vect[0]))

  
  
# debug #
#########

breakpoints = {9:True, 14: True}
watchpoints = {'c': True}
stepping = False


def debug(command, my_arg, my_locals):
  global stepping
  global breakpoints
  global watchpoints
  
  if command.find(' ') > 0:
    arg = command.split(' ')[1]
  else:
    arg = None
    
  if command.startswith('s'):
    stepping = True
    return True
  elif command.startswith('c'):
    stepping = False
    return True
  elif command.startswith('p'):    # print 
    if (arg == None):
      print my_locals
    elif(arg in my_locals):
      print arg,' = ', repr(my_locals[arg])
    else:
      print 'No such variable:', arg
  elif command.startswith('b'):    # breakpoint         
    if(arg == None):
      print 'You must supply a line number'
    else:
      breakpoints[int(arg)] = True
  elif command.startswith('w'):    # watch variable
    if arg == None:
      print "You must supply a variable name"
    else:
      watchpoints[arg] = True 
  elif command.startswith('q'):
    sys.exit(0)
  else:
    print "No such command", repr(command)
  return False

commands = ["s", "s", "p out", "q"]  # simulate web IDE

def input_command():
  #command = raw_input("(my-spyder)")
  global commands
  command = commands.pop(0)  # simulate web IDE
  return command

def traceit(frame, event, arg):
  global stepping
  global breakpoints
  
  if event == 'line':
    if stepping or breakpoints.has_key(frame.f_lineno):
      resume = False
      while not resume:
        print event, frame.f_lineno, frame.f_code.co_name, frame.f_locals
        command = input_command()
        resume = debug(command, arg, frame.f_locals)
  return traceit

# run #
#######

sys.settrace(traceit) # start debug
  
test_vector=[["'foo'","'foo'"],
             ['"foo"','"foo"'],
             ['<b>foo</b>','foo'],
             ['"<b>foo</b>"','"foo"'],
             ["foo","foo"],
             ['<a href=">">foo</a>',"foo"]]

html_removal(remove_html_markup_fixed,test_vector) 
