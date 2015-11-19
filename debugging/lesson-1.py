# Don't do this at home or at all
# 5 sins of debugging
# 1. Scatter output statements everywhere (print)
# 2. Debug the program into existence (add and remove lines)
# 3. Never back up earlier versions
# 4. Don't bother understanding what the program should do.
# 5. Use the most obvious fix

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
  
  

# Before fix:
# 2. proceed systematically 
# 4. understand what the program should do
# 5. fix the problem, bot the symptom

# Classification
# bug = defect: error in code
# failure = visible by user

# defect result in infection which result in failure

# Scientific Method
# 1. Initial Observation
# 2. Hypothesis             <-|
# 3. Prediciton               |  support/refine .... reject/create new
# 4. Experiment               | 
# 5. Oberservation          >-| 
# 6. Theory

# Scientific Method
# 1. Code, Failure, run, more runs
# 2. Hypothesis             <-|
# 3. Prediciton               |  support/refine .... reject/create new
# 4. Experiment               | 
# 5. Oberservation          >-| 
# 6. Diagnosis

# TEST Hypotheses -> Experiments
#
# Powerful Debugging: "assert condition"


# Experiment 0: find Hypothesis #
#################################

#test_vector=[['<a>foo</a>','foo'],
#             ['"<b>foo</b>"','"foo"'],
#             ['"foo"','foo'],
#             ['"bar"','bar'],
#             ['""','']]

# Hypothesis 1: Double quotes are stripped from toggled input
# Hypothesis 2: Tags in double quotes are not stripped

# Experiment 1: Hypothesis 1 #
##############################

#test_vector=[['"foo"','"foo"'],
#             ['"bar"','"bar"'],
#             ['""','']]

#-> no tags! Still quotes stripped

# Hypothesis 1.1: Tag is set 

# Experiment 1.1: Hypothesis 1.1 #
##################################
# assert tag not true

# test_vector=[['"foo"','assertionException']]


# Experiment 2: Evaluate quote conditon #
#########################################
# assert quote conditon not reached
# test_vector=[['"foo"','assertionException']]

#-> Difference between single and double quotes?

# Experiment 2.1: Evaluate single quote conditon #
##################################################

#test_vector=[["'foo'","'foo'"],
#             ['"foo"','"foo"']]

# wrong line of code
# elif c == '"' or c == "'" and tag:

# Verfiy Soulution #
####################

test_vector=[["'foo'","'foo'"],
             ['"foo"','"foo"'],
             ['<b>foo</b>','foo'],
             ['"<b>foo</b>"','"foo"'],
             ["foo","foo"],
             ['<a href=">">foo</a>',"foo"]]

# Check for future revision #
#############################
# state "quote and not tag" shouldn't be reached
# assertion: "assert (tag or not quote)" is usable 

# run experiements #
####################
print("String | Expectation | Result")
for tst_vect in test_vector:
  print(tst_vect[0] + ' | ' + tst_vect[1] + ' | ' 
        + remove_html_markup(tst_vect[0]))
        
        
