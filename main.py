from PIL import Image
import insert
import extract



def main():

	#image for encoding 1.jpg
	im = Image.open("1.jpg")
	msg = "Computers represent everything as numbers. In fact, they represent everything using only two numbers "
	#message to decode
	insert.embld(im,msg)
	
	
	# decoding image ans.png
	im = Image.open("ans.png")
	
	print("decoding start...")
	extract.decode(im)
	print("\n\ndecoding end...")
	


main()

	
