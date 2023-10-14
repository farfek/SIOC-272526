from PIL import Image
sciezka_do_obrazu = r"C:\Users\Franek\Desktop\sdadasd.jpg"
obraz = Image.open(sciezka_do_obrazu)
obraz_filtr = obraz.convert('L')
obraz_filtr.show()