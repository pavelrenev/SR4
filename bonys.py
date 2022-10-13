def prov_o(n):
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

def prov_p(n):
	k=0
	if n=='':
		k=1
	s="1234567890"
	for i in range(len(n)):
		if n[i] not in s:
			k+=1
			break
	if k!=0:
		return 0
	else:
		return 1

print("Данная программа находит кол-во чисел в массиве отличных от минимального на delta")

k=input("Введите длину массива: ")
delta=input("Введите delta (целое число): ")

if prov_p(k)==True and prov_o(delta)==True:
	k=int(k)
	delta=int(delta)
	m=[""]*k
	x=0
	for i in range(k):
		dop=input("Введите целое число: ")
		if prov_o(dop)==True:
			m[i]=int(dop)
		else:
			print("Ввдено неверное значение, перезапустите программу и введите целое число")
			x=1
			break
	if x==0:
		for i in range(len(m)):
			if m[i]-delta==min(m):
				x+=1

		print("Кол-во элементов отличных от минимального на delta = ",x)

else:
	print("ввдено неверное значение, перезапустите программу и введите целое число")
