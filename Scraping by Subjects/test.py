import modules.scraping as scraper
import modules.utils as utils

y=utils.getSubSubjectCode()
x=utils.getSubjectCode()
z=x+y
s=sorted(z)

for i in s:
    print(i)

# for i in x:
#     print(i)