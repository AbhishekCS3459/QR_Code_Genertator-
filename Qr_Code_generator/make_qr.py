import os
import qrcode

link_for_image_video_for_which_qr_should_created="https://www.youtube.com/channel/UChU7-2vsv5hhMz6hqjDI8NA"
img = qrcode.make(link_for_image_video_for_which_qr_should_created)
img.save("qr.png","PNG")
os.system("Open qr.png")