from PIL import Image,ImageFont,ImageDraw

afbeelding = Image.open("truck.png")

afbeelding.show()

breedte = afbeelding.width

hoogte = afbeelding.height

print("de afbeelding is " + str(breedte) + " picels breed en " + str(hoogte) + "pixels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)

lettertype = ImageFont.truetype("impact",40)

tekengebied = ImageDraw.Draw(meme_achtergrond)

tekst = "Epstein didnt\kill himself"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

achtergrond.show()
