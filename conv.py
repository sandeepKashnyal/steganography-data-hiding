def no2bin(no):
	return str(format(no,'08b'))

def bin2no(bi):
	return int(str(bi),2)
	

def str2bin(st):
	n = len(st)
	ans=""
	for i in range(0,n):
		bi = str( no2bin( ord(st[i]) ) )
		ans=ans+bi
	return ans

def bin2str(bi):
	bi = str(bi)
	n = len(bi)
	print()
	n=int(n/8) - 2
	x=0
	ans=""
	for i in range(0,n):
		s = chr(bin2no(bi[x:x+8]))
		x=x+8
		ans=ans+s
	return ans
	
	

