from PIL import Image
import conv

def decode(im):
	data = list(im.getdata())
	n = len(data)
	st = ""
	for i in range(0,n):
		s = conv.no2bin(data[i][0])
		st=st+s[6]+s[7]
		if ( len(st)>=16 and st[-16:] =="0010000100100001" ):
			break;# delimiter found stop decoding
			
		s = conv.no2bin(data[i][1])
		st=st+s[6]+s[7]
		if ( len(st)>=16 and st[-16:] =="0010000100100001" ):
			break;
			
		s = conv.no2bin(data[i][2])
		st=st+s[6]+s[7]
		if ( len(st)>=16 and st[-16:] =="0010000100100001" ):
			break;
		
	print(conv.bin2str(st))
		
		
		
		
