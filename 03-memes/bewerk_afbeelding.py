from PIL import Image

afbeelding = Image.open("truck.png")

afbeelding.show()

breedte = afbeelding.width

hoogte = afbeelding.height

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save("truck.png")

afbeelding.show()
