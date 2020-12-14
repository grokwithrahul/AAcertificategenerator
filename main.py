from certificategenerator import certificate

monke = certificate.certificate()
csvpath = r"./certificategenerator/test/test.csv"
impath = r"./certificategenerator/test/1_7UJi7s0b06torqqxkTPsgQ.png"
monke.config(csvpath, impath, "Monke", signaturename="Rahul", style=1)
a = monke.generate()