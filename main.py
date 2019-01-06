from machine import I2C, Pin
import time
import ssd1306
import machine
import framebuf

i2c = I2C(-1, Pin(5), Pin(4))

display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.show()

gfiles = ['f01.pbm',
	'f02.pbm',
	'f03.pbm',
	'f04.pbm',
	'f05.pbm',
	'f06.pbm',
	'f07.pbm',
	'f08.pbm',
	'f09.pbm',
	'f10.pbm',
	'f11.pbm']
fb = []
for gf in gfiles:
	with open(gf, 'rb') as f:
		f.readline()
		f.readline()
		f.readline()
		data = bytearray(f.read())
	fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
	fb.append(fbuf)

display.invert(1)
while True:
	for i in range(1,11):
		display.blit(fb[i], 0, 0)
		display.show()


