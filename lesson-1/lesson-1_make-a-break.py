import webbrowser
import time

print "Hello World"
break_total = 3
break_count = 0
print("This is it: "+time.ctime())
while(break_count <break_total):
  time.sleep(20)
  webbrowser.open("https://trello.com/b/VcXlGp4b/srd-kd")
  break_count = break_count + 1
