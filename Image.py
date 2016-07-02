#!/usr/bin/env python3
#-*-encoding:utf8-*-

from PIL import Image
im = Image.open('a.jpg');
print(im);
print(im.format,im.size,im.mode);

im.thumbnail((200,200));
im.save('b.jpg','JPEG');