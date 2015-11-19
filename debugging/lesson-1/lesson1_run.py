import lesson1_lib


def html_removal(function,test_vect):
  print("String | Expectation | Result")
  for tst_vect in test_vect:
    print(tst_vect[0] + ' | ' + tst_vect[1] + ' | ' 
          + function(tst_vect[0]))


# test [[INPUT, EXPECTED_OUTPUT]]

# Step 1: Find Hypothesis #
#################################


## Experiments
test_vector=[['<a>foo</a>','foo'],
             ['"<b>foo</b>"','"foo"'],
             ['"foo"','foo'],
             ['"bar"','bar'],
             ['""','']]

#html_removal(lesson1_lib.remove_html_markup_original,test_vector) 


# Hypothesis 1: Double quotes are stripped from toggled input
# Hypothesis 2: Tags in double quotes are not stripped

# Experiment 1: Hypothesis 1 #
##############################

## Experiments
test_vector=[['"foo"','"foo"'],
             ['"bar"','"bar"'],
             ['""','']]


#html_removal(lesson1_lib.remove_html_markup_print,test_vector) 

#-> no tags! Still quotes stripped

# Hypothesis 1.1: Tag is set 

# Experiment 1.1: Hypothesis 1.1 #
##################################
# assert tag not true

## Experiments
test_vector=[['"foo"','assertionException']]

#html_removal(lesson1_lib.remove_html_markup_tag,test_vector) 

# Assertion not called

# Experiment 2: Evaluate quote conditon #
#########################################
# assert quote conditon not reached

## Experiments
test_vector=[['"foo"','assertionException']]


#html_removal(lesson1_lib.remove_html_markup_quote,test_vector) 
#-> Difference between single and double quotes?

# Experiment 2.1: Evaluate single quote conditon #
##################################################

test_vector=[["'foo'","'foo'"],
             ['"foo"','"foo"']]

#html_removal(lesson1_lib.remove_html_markup_original,test_vector) 

# wrong line of code
# elif c == '"' or c == "'" and tag:

# Verfiy Soulution #
####################

# state "quote and not tag" shouldn't be reached
# assertion: "assert (tag or not quote)" is usable 

## Experiments
test_vector=[["'foo'","'foo'"],
             ['"foo"','"foo"'],
             ['<b>foo</b>','foo'],
             ['"<b>foo</b>"','"foo"'],
             ["foo","foo"],
             ['<a href=">">foo</a>',"foo"]]

html_removal(lesson1_lib.remove_html_markup_fixed,test_vector) 

