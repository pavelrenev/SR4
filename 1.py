def prov_c(n):
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


print("Данная программа изменяет все элементы массива после максимального на 0")

k=input("Введите длину массива: ")

if prov_c(k)==True:
	k=int(k)
	m=[""]*k
	x=0
	for i in range(k):
		dop=input("Введите число с плавоющей точкой: ")
		if prov_d(dop)==True:
			m[i]=float(dop)
		else:
			print("Ввдено неверное значение, перезапустите программу и введите число с плавоющей точкой")
			x=1
			break
	if x==0:
		for i in range(len(m)):
			if x==1:
				m[i]=0
			if m[i]==max(m):
				x=1

		print("Итоговый массив: ", m)

else:
	print("Ввдено неверное значение, перезапустите программу и введите целое число")
