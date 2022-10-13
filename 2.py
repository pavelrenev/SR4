def prov_c(n):
	k=0
	if n=='':
		k=1
	s="-1234567890"
	for i in range(len(n)):
		if n[i] not in s:
			k+=1
			break
	if k!=0:
		return 0
	else:
		return 1

def prov_d(n):
	k=0
	if n=='':
		k=1
	s="-1234567890."
	for i in range(len(n)):
		if n[i] not in s or n=="":
			k+=1
			break
	if k!=0:
		return 0
	else:
		return 1


print("Данная программа выводит элементы которые имеются в массивах a и b\nМассивы вводятся вручную")

x=0
k=input("Введите длину массива a: ")
 
if prov_c(k)==True:
	k=int(k)
	a=[""]*k

	for i in range(k):
		dop=input("Введите число с плавоющей точкой: ")
		if prov_d(dop)==True:
			a[i]=float(dop)
		else:
			print("Ввдено неверное значение, перезапустите программу и введите число с плавоющей точкой")
			x=1
			break

else:
	print("Ввдено неверное значение, перезапустите программу и введите целое число")

k=input("Введите длину массива b: ")
if prov_c(k)==True:
	k=int(k)
	b=[""]*k

	for i in range(k):
		dop=input("Введите число с плавоющей точкой: ")
		if prov_d(dop)==True:
			b[i]=float(dop)
		else:
			print("Ввдено неверное значение, перезапустите программу и введите число с плавоющей точкой")
			x=1
			break

else:
	print("Ввдено неверное значение, перезапустите программу и введите целое число")

c=set()

if x==0:
	for i in range(len(a)):
		if a[i] in b:
			c.add(a[i])
	if len(c)==0:
		print("Ненашлось общих элементов")
	else:
		print("Общие элементы массивов: ", c)