""" ROI """
import numpy as np
import cv2

filename=input("Please enter filename:")
ROI_x,ROI_y=eval(input("Enter(x,y) for ROI: "))
ROI_nr,ROI_nc=eval(input("Enter(rows,columns) for ROI: "))
img=cv2.imread(filename,-1)
ROI=img[ROI_x : ROI_x+ROI_nr,ROI_y : ROI_y+ROI_nc]
cv2.imwrite("ROI.bmp",ROI)

def image_formation_model( f, x0, y0, sigma ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	illumination = np.zeros( [ nr, nc ], dtype = 'float32' )
	for x in range( nr ):
		for y in range( nc ):
			illumination[x,y] = np.exp( -( ( 512- x0 ) ** 2 + ( 512 - 0 ) ** 2 ) / 
 								( 2 * sigma * sigma ) )
	for x in range( nr ):
		for y in range( nc ):
			for k in range( 3 ):
				val = round( illumination[x,y] * f[x,y,k] )
				g[x,y,k] = np.uint8( val )
	return g
	
def main( ):
	img = cv2.imread( "Monet.bmp", -1 )
	nr, nc = img.shape[:2]
	x0 = nr // 2
	y0 = nc // 2
	sigma = 300
	img2 = image_formation_model( img, x0, y0, sigma )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Image Formation Model", img2 )
	cv2.waitKey( 0 )

main( )
