import glob
 
files = glob.glob("D://Python_Programs//Pattern//ab?.txt") + glob.glob("D://Python_Programs//Pattern//*.xml")
print(files)

import re
 
text = "The price of the product is very high"
match = re.search(r"product",text)
if match:
    print(" It is found: ", match.group())
   
 
text = "Today is friday and tomorrow is saturday"
paatern = r"\b(friday |saturday)"
new_text = re.sub(paatern,"weekday",text)
print(new_text)