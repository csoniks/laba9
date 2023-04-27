from PIL import ImageFilter, Image
import os
spisok = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
os.mkdir("for_new_pic")
for i in spisok:
    img = Image.open(i)
    img = img.filter(ImageFilter.EMBOSS)
    os.startfile(i)
    #print(os.path.getsize(i))
    name = "for_new_pic/new" + i
    img.save(name)
'''os.replace("new1.jpg", "for_new_pic/new1.jpg")
os.replace("new2.jpg", "for_new_pic/new2.jpg")
os.replace("new3.jpg", "for_new_pic/new3.jpg")
os.replace("new4.jpg", "for_new_pic/new4.jpg")
os.replace("new5.jpg", "for_new_pic/new5.jpg")'''

def z2():
    for i in os.listdir(r"F:\алгоритмизация\laba99"): #содержимое папок
        if i[-4:] == ".jpg" or i[-4:] == ".png":
            img = Image.open(i)
            img = img.filter(ImageFilter.EMBOSS)
            img.show()

def z3():
    import csv
    with open('data.csv', newline='') as f:
        faylik = csv.reader(f)
        all = 0
        for i in faylik:
            print((i[0]) + " " + i[1] + "шт." + " " + "за" + " " + i[2] + "руб")
            summa = int(i[1]) * int(i[2])
            #print(summa)
            all += summa
        print("Итоговая сумма:" + " " + str(all))
z2()
z3()
