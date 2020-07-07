from PIL import Image
import conv

def embld(im,message):
	im = im.convert('RGB')
	data = list(im.getdata())
	width = im.size[0]
	height = im.size[1]
	msg = conv.str2bin(message)
	
	msg = msg+"0010000100100001" # delimiter
	print (len(msg),width*height*6)
	
	if len(msg)/6 > width*height :
		print("image is small data is large!!")
		return
	img = im.load()

	x = 0
	
	temp = conv.bin2no("11111100")
	print("Data Hiding starts.....")
	
	for i in range (0,width*height):
		if x>=len(msg):
			break
		ximg = int(i/width)
		yimg = int(i%width)

		hid = conv.bin2no("000000"+msg[x]+msg[x+1])# new pixel
		x = x+2
		r = (data[i][0] & temp |  hid)
		if x>=len(msg):
			msg=msg+"00"
			
		hid = conv.bin2no("000000"+msg[x]+msg[x+1])# new pixel
		x = x+2
		g = (data[i][1] & temp | hid)
		if x>=len(msg):
			msg=msg+"00"
			
		hid = conv.bin2no("000000"+msg[x]+msg[x+1])# new pixel
		x = x+2
		b = (data[i][2] & temp | hid)
		
		px = (r,g,b)

		img[yimg,ximg] = px
	print("image saving....")
	im.save("ans.png")
	print("Done....")
		
		
		
		
	
	
	
	
	



