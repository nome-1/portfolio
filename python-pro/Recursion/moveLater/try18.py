import re


k=[4,4.00,-1.00,+454,"-.4.0oo0",4,6]
tm=[str(b) for b in k]
for i in tm:
    print(bool(re.search("^[0-9]|(-)$",i)))
