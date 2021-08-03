from bs4 import BeautifulSoup
fp = open('test1.html',encoding='utf-8')
soup = BeautifulSoup(fp,'lxml')
print(soup.p)
