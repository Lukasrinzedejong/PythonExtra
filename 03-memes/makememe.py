from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

achtergrond = Image.open("meme_background.jpg")

breedte = achtergrond.width

hoogte = achtergrond.height

print("de afbeelding is " + str(breedte) + " picels breed en " + str(hoogte) + "pixels hoog")

print(achtergrond.format, achtergrond.size, achtergrond.mode)

lettertype = ImageFont.truetype("impact", 10)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "this assignment took way to long"
tekengebied.multiline_text((10,150), tekst, font=lettertype, fill=(0,0,0))

achtergrond.show()

achtergrond.save("meme_met_tekst.jpg")
