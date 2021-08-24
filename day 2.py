Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="hello"
>>> b=[]
>>> c=[]
>>> for i in a:
	if i not in b:
		b.append(i)
		c.append(a.count(i))
		for i in range(len(b)):
			print(b[i],"-",c[i])
			print(end=" ")

			
h - 1
 h - 1
 e - 1
 h - 1
 e - 1
 l - 2
 h - 1
 e - 1
 l - 2
 o - 1
 
>>> 