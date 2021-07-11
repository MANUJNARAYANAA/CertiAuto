from PIL import Image, ImageDraw, ImageFont
import pandas as pd

form = pd.read_excel("feedback_form.xlsx")
name_list = form['Name'].to_list()
for i in name_list:
    im = Image.open("cert.jpg")
    d = ImageDraw.Draw(im)
    location = (418, 470)
    text_color = (40, 35, 93)
    font = ImageFont.truetype("courbd.ttf", 150)
    d.text(location, i, fill=text_color,font=font)
    im.save("./certificates/"+"certificate_"+i+".pdf")


