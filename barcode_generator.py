from tkinter import *
import barcode
import random
from barcode.writer import ImageWriter

generatedbarcode=[]

def Numbergenarator():
    num1="0123456789"
    num2="0123456789"
    number=num1+num2
    lenght=12
    result="".join(random.sample(number,lenght))
    return result

def barcode_Generator():
    product=product_entry.get()
    price=PriceEntry.get()
#     print(product,price)
    
    barcode_format = barcode.get_barcode_class('upc')
    barcodeNumber = '0123456557839'
#     generated=barcode_format(barcodeNumber)
#     generated.save(product)
    generated=barcode_format(barcodeNumber,writer=ImageWriter())
    generated.save(product)
    generatedbarcode.append(f"{product}.png")
    
generator=Tk()
generator.geometry('600x600')
generator.title("Barcode Generator")

product_name=Label(generator, text="Product Name: ", font=('Arial', 14,'bold'))
product_name.place(x=150,y=50)
product_entry =Entry(generator, font=("Arial", 16),bg='#BFEFFF')
product_entry.place(x=300,y=50)

price_name=Label(generator, text="Price: ", font=('Arial', 14,'bold')).place(x=150,y=80)
PriceEntry=Entry(generator,font=('Arial', 14,),bg='#BFEFFF',width=22)
PriceEntry.place(x=300,y=80)



btn=Button(generator,text='Generator Bar Code',width=30,bg='black',fg='white',command=barcode_Generator)
btn.place(x=200,y=120)

image=Label(generator)
image.place(x=100,y=150)

while True:
    for img in generatedbarcode:
        img = PhotoImage(file=img)
        image['image']=img
    generator.update()
