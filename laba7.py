def a7():
    from PIL import Image
    r = "Cat.jpg"
    o = Image.open(r)
    o.show()
    po = {"Размер": o.size,"Формат": o.format,"Цветовая модель": o.mode}
    for key, value in po.items():
        print(key, ": ", value)
def b7():
    from PIL import Image, ImageOps
    o = Image.open("Cat.jpg")

    g = o.width // 3
    t = o.height // 3
    x = o.resize((g, t))
    x.save('CaT.jpg')
    f = Image.open("CaT.jpg")

    o = ImageOps.flip(f)
    o.save('CAT.png')
    o = ImageOps.mirror(f)
    o.save('CAT.png')
def c7():
    from PIL import Image, ImageFilter
    a1 = Image.open("1.jpg")
    a1.filter(Filter.GaussianBlur(radius = 2))
    a1.save('1c.jpg')
    b2 = Image.open("2.jpg")
    b2.filter(Filter.GaussianBlur(radius = 2))
    b2.save('2c.jpg')
    c3 = Image.open("3.jpg")
    c3.filter(Filter.GaussianBlur(radius = 2))
    c3.save('3c.jpg')
    d4 = Image.open("4.jpg")
    d4.filter(Filter.GaussianBlur(radius = 2))
    d4.save('4c.jpg')
    e5 = Image.open("5.jpg")
    e5.filter(Filter.GaussianBlur(radius =2))
    e5.save('5c.jpg')
def d7():
    from PIL import Image, ImageDraw, ImageFont
    o = Image.open("1.jpg")
    d = ImageDraw.Draw(o)
    f = ImageFont.truetype('1d.ttf', 30)
    d.text((20, 20), "Водяной знак", fill = (10, 12, 12), font = f)
    o.save('11d.png')