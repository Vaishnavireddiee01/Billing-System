from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib
#functionality part
#if not os.path.exists('bills'):
    #os.mkdir('bills')
def clear():
    bathsoapLabelentry.delete(0,END)
    facecreamLabelentry.delete(0,END)
    facewashLabelentry.delete(0,END)
    hairgelLabelentry.delete(0,END)
    hairoilLabelentry.delete(0,END)
    BodylotionLabelentry.delete(0,END)

    riceLabelentry.delete(0,END)
    dalLabelentry.delete(0,END)
    oilLabelentry.delete(0,END)
    teaLabelentry.delete(0,END)
    wheatLabelentry.delete(0,END)
    sugarLabelentry.delete(0,END)

    maazaLabelentry.delete(0,END)
    cocacolaLabelentry.delete(0,END)
    pepsiLabelentry.delete(0,END)
    dewLabelentry.delete(0,END)
    frootiLabelentry.delete(0,END)
    spriteLabelentry.delete(0,END)

    bathsoapLabelentry.insert(0,0)
    facecreamLabelentry.insert(0,0)
    facewashLabelentry.insert(0,0)
    hairgelLabelentry.insert(0,0)
    hairoilLabelentry.insert(0,0)
    BodylotionLabelentry.insert(0,0)

    riceLabelentry.insert(0,0)
    dalLabelentry.insert(0,0)
    oilLabelentry.insert(0,0)
    teaLabelentry.insert(0,0)
    wheatLabelentry.insert(0,0)
    sugarLabelentry.insert(0,0)

    maazaLabelentry.insert(0,0)
    cocacolaLabelentry.insert(0,0)
    pepsiLabelentry.insert(0,0)
    dewLabelentry.insert(0,0)
    frootiLabelentry.insert(0,0)
    spriteLabelentry.insert(0,0)

    cosmeticpriceLabelentry.delete(0,END)
    grocerypriceLabelentry.delete(0,END)
    cooldrinkspriceLabelentry.delete(0,END)

    cosmetictaxLabelentry.delete(0,END)
    grocerytaxLabelentry.delete(0,END)
    cooldrinkstaxLabelentry.delete(0,END)

    nameentry.delete(0,END)
    phoneLabelentry.delete(0,END)
    Billnumberentry.delete(0,END)

    textarea.delete(1.0,END)



def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderentry.get(),passwordentry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderentry.get(),recieverentry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        senderframe=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderframe.grid(row=0,column=0,padx=40,pady=20)

        senderlabel=Label(senderframe,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderlabel.grid(row=0,column=0,padx=10,pady=8)

        senderentry=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderentry.grid(row=0,column=1,padx=10,pady=8)

        passwordlabel=Label(senderframe,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordlabel.grid(row=1,column=0,padx=10,pady=8)

        passwordentry=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordentry.grid(row=1,column=1,padx=10,pady=8)

        recipientframe=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientframe.grid(row=1,column=0,padx=40,pady=20)

        recieverlabel=Label(recipientframe,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverlabel.grid(row=0,column=0,padx=10,pady=8)

        recieverentry=Entry(recipientframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverentry.grid(row=0,column=1,padx=10,pady=8)

        messagelabel=Label(recipientframe,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messagelabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientframe,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendbutton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)


        root1.mainloop()
def Print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def Search_bill():
    present="no"
    for i in os.listdir('bills/'):
        if i.split('.')[0]==Billnumberentry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            present = "yes"
    if present=="no":
        messagebox.showerror('Error','Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)
billnumber=random.randint(500,1000)
def bill_area():
    if nameentry.get()=='' or phoneLabelentry.get()=='':
        messagebox.showerror('Error','Customer details are required')
    elif cosmeticpriceLabelentry.get()=='' and grocerypriceLabelentry.get()=='' and cooldrinkspriceLabelentry.get()=='':
        messagebox.showerror('Error','No Products are selected')
    elif cosmeticpriceLabelentry.get()=='0 Rs' and grocerypriceLabelentry.get()=='0 Rs' and cooldrinkspriceLabelentry.get()=='0 Rs':
        messagebox.showerror('Error','No Products are selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameentry.get()}\n')
        textarea.insert(END,f'\nPhone Number: {phoneLabelentry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'\nProducts\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n=======================================================')
        #cosmeticsprice
        if bathsoapLabelentry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapLabelentry.get()}\t\t\t{soapprice} Rs')
        if facecreamLabelentry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamLabelentry.get()}\t\t\t{facecreamprice} Rs')
        if facewashLabelentry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t\t{facewashLabelentry.get()}\t\t\t{facewashprice} Rs')
        if hairoilLabelentry.get()!='0':
            textarea.insert(END,f'\nHair Oil\t\t\t{hairoilLabelentry.get()}\t\t\t{hairoilprice} Rs')
        if hairgelLabelentry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelLabelentry.get()}\t\t\t{hairgelprice} Rs')
        if BodylotionLabelentry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t\t{BodylotionLabelentry.get()}\t\t\t{bodylotionprice} Rs')
        #groceryprice
        if riceLabelentry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{riceLabelentry.get()}\t\t\t{riceprice} Rs')
        if dalLabelentry.get()!='0':
            textarea.insert(END,f'\nDal\t\t\t{dalLabelentry.get()}\t\t\t{dalprice} Rs')
        if wheatLabelentry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatLabelentry.get()}\t\t\t{wheatprice} Rs')
        if oilLabelentry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{oilLabelentry.get()}\t\t\t{oilprice} Rs')
        if sugarLabelentry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{sugarLabelentry.get()}\t\t\t{sugarprice} Rs')
        if teaLabelentry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{teaLabelentry.get()}\t\t\t{teaprice} Rs')
            #cooldrinks
        if maazaLabelentry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t\t{maazaLabelentry.get()}\t\t\t{maazaprice} Rs')
        if cocacolaLabelentry.get()!='0':
            textarea.insert(END,f'\nCocacola\t\t\t{cocacolaLabelentry.get()}\t\t\t{cocacolaprice} Rs')
        if spriteLabelentry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{spriteLabelentry.get()}\t\t\t{spriteprice} Rs')
        if dewLabelentry.get()!='0':
            textarea.insert(END,f'\nMountaindew\t\t\t{dewLabelentry.get()}\t\t\t{dewprice} Rs')
        if frootiLabelentry.get()!='0':
            textarea.insert(END,f'\nfrooti\t\t\t{frootiLabelentry.get()}\t\t\t{frootiprice} Rs')
        if pepsiLabelentry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t{pepsiLabelentry.get()}\t\t\t{pepsiprice} Rs')
        textarea.insert(END,'\n------------------------------------------------------')

        #Taxes
        if cosmetictaxLabelentry.get()!='0':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmetictaxLabelentry.get()}')
        if grocerytaxLabelentry.get()!='0':
            textarea.insert(END,f'\nGrocery Tax Tax\t\t\t\t{grocerytaxLabelentry.get()}')
        if cooldrinkstaxLabelentry.get()!='0':
            textarea.insert(END,f'\nCooldrinks Tax\t\t\t\t{cooldrinkstaxLabelentry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
        textarea.insert(END,'\n-------------------------------------------------------')
        save_bill()
        
def Total():
    #cosmeticpricecalculation
    global soapprice,facecreamprice,facewashprice,hairoilprice,hairgelprice,bodylotionprice
    global riceprice,dalprice,wheatprice,oilprice,sugarprice,teaprice
    global maazaprice,cocacolaprice,spriteprice,dewprice,frootiprice,pepsiprice
    global totalbill
    #cosmeticpricecalculation
    soapprice=int(bathsoapLabelentry.get())*20
    facecreamprice=int(facecreamLabelentry.get())*50
    facewashprice=int(facewashLabelentry.get())*100
    hairoilprice=int(hairoilLabelentry.get())*80
    hairgelprice=int(hairgelLabelentry.get())*60
    bodylotionprice=int(BodylotionLabelentry.get())*80
    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairoilprice+hairgelprice+bodylotionprice
    cosmeticpriceLabelentry.delete(0,END)
    cosmeticpriceLabelentry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxLabelentry.delete(0,END)
    cosmetictaxLabelentry.insert(0,str(cosmetictax) + 'Rs')
    #grocerypricecalculation
    riceprice=int(riceLabelentry.get())*100
    dalprice=int(dalLabelentry.get())*70
    oilprice=int(oilLabelentry.get())*90
    wheatprice=int(wheatLabelentry.get())*80
    sugarprice=int(sugarLabelentry.get())*90
    teaprice=int(teaLabelentry.get())*40
    totalgroceryprice=riceprice+dalprice+oilprice+wheatprice+sugarprice+teaprice
    grocerypriceLabelentry.delete(0,END)
    grocerypriceLabelentry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax=totalgroceryprice*0.08
    grocerytaxLabelentry.delete(0,END)
    grocerytaxLabelentry.insert(0,str(grocerytax) + 'Rs')
    #cooldrinkspricecalculation
    frootiprice=int(frootiLabelentry.get())*40
    maazaprice=int(maazaLabelentry.get())*30
    dewprice=int(dewLabelentry.get())*20
    cocacolaprice=int(cocacolaLabelentry.get())*20
    spriteprice=int(spriteLabelentry.get())*40
    pepsiprice=int(pepsiLabelentry.get())*40
    totalcooldrinksprice=frootiprice+maazaprice+dewprice+cocacolaprice+spriteprice+pepsiprice
    cooldrinkspriceLabelentry.delete(0,END)
    cooldrinkspriceLabelentry.insert(0,f'{totalcooldrinksprice} Rs')
    cooldrinkstax=totalcooldrinksprice*0.06
    cooldrinkstaxLabelentry.delete(0,END)
    cooldrinkstaxLabelentry.insert(0,str(cooldrinkstax) + 'Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totalcooldrinksprice+cosmetictax+grocerytax+cooldrinkstax

root=Tk()
root.title('Billing System')
root.geometry("1350x700+0+0")

headingLabel=Label(root,text='Billing System',font=('Times New Roman',20,'bold'),bg='gray20',fg='gold',bd=14,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer_details',font=('Times New Roman',13,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
customer_details_frame.pack(fill=X)

name=Label(customer_details_frame,text='Name',font=('Times New Roman',13,'bold'),bg='gray20',fg='white',bd=8)
name.grid(row=0,column=0,padx=20)
nameentry=Entry(customer_details_frame,font=('arial',13),bd=7,width=18)
nameentry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phonenumber',font=('Times New Roman',13,'bold'),bg='gray20',fg='white',bd=8)
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneLabelentry=Entry(customer_details_frame,font=('arial',13),bd=7,width=18)
phoneLabelentry.grid(row=0,column=3,padx=8)

Billnumber=Label(customer_details_frame,text='BillNumber',font=('Times New Roman',13,'bold'),bg='gray20',fg='white',bd=8)
Billnumber.grid(row=0,column=4,padx=18,pady=2)
Billnumberentry=Entry(customer_details_frame,font=('arial',13),bd=7,width=18)
Billnumberentry.grid(row=0,column=5,padx=8)

search=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=12,command=Search_bill)
search.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('Times New Roman',15,'bold'),bg='gray20',fg='gold',bd=4)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
bathsoapLabel.grid(row=0,column=0,pady=8,padx=10,sticky='w')
bathsoapLabelentry=Entry(cosmeticsFrame,font=('arial',15),width=10,bd=5)
bathsoapLabelentry.grid(row=0,column=1,pady=8,padx=10)
bathsoapLabelentry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='FaceCream',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
facecreamLabel.grid(row=1,column=0,pady=8,padx=10,sticky='w')
facecreamLabelentry=Entry(cosmeticsFrame,font=('arial',15),width=10,bd=5)
facecreamLabelentry.grid(row=1,column=1,pady=8,padx=10)
facecreamLabelentry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
facewashLabel.grid(row=2,column=0,pady=8,padx=10,sticky='w')
facewashLabelentry=Entry(cosmeticsFrame,font=('arial',15),width=10,bd=5)
facewashLabelentry.grid(row=2,column=1,pady=8,padx=10)
facewashLabelentry.insert(0,0)

hairoilLabel=Label(cosmeticsFrame,text='Hair oil',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
hairoilLabel.grid(row=3,column=0,pady=8,padx=10,sticky='w')
hairoilLabelentry=Entry(cosmeticsFrame,font=('arial',15),width=10,bd=5)
hairoilLabelentry.grid(row=3,column=1,pady=8,padx=10)
hairoilLabelentry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair gel',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
hairgelLabel.grid(row=4,column=0,pady=8,padx=10,sticky='w')
hairgelLabelentry=Entry(cosmeticsFrame,font=('arial',15),width=10,bd=5)
hairgelLabelentry.grid(row=4,column=1,pady=8,padx=10)
hairgelLabelentry.insert(0,0)

BodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
BodylotionLabel.grid(row=5,column=0,pady=8,padx=10,sticky='w')
BodylotionLabelentry=Entry(cosmeticsFrame,font=('arial',15),width=10,bd=5)
BodylotionLabelentry.grid(row=5,column=1,pady=8,padx=10)
BodylotionLabelentry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('Times New Roman',15,'bold'),bg='gray20',fg='gold',bd=4)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
riceLabel.grid(row=0,column=0,pady=8,padx=10,sticky='w')
riceLabelentry=Entry(groceryFrame,font=('arial',15),width=10,bd=5)
riceLabelentry.grid(row=0,column=1,pady=8,padx=10)
riceLabelentry.insert(0,0)

dalLabel=Label(groceryFrame,text='Dal',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
dalLabel.grid(row=1,column=0,pady=8,padx=10,sticky='w')
dalLabelentry=Entry(groceryFrame,font=('arial',15),width=10,bd=5)
dalLabelentry.grid(row=1,column=1,pady=8,padx=10)
dalLabelentry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
wheatLabel.grid(row=2,column=0,pady=8,padx=10,sticky='w')
wheatLabelentry=Entry(groceryFrame,font=('arial',15),width=10,bd=5)
wheatLabelentry.grid(row=2,column=1,pady=8,padx=10)
wheatLabelentry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
sugarLabel.grid(row=3,column=0,pady=8,padx=10,sticky='w')
sugarLabelentry=Entry(groceryFrame,font=('arial',15),width=10,bd=5)
sugarLabelentry.grid(row=3,column=1,pady=8,padx=10)
sugarLabelentry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
teaLabel.grid(row=4,column=0,pady=8,padx=10,sticky='w')
teaLabelentry=Entry(groceryFrame,font=('arial',15),width=10,bd=5)
teaLabelentry.grid(row=4,column=1,pady=8,padx=10)
teaLabelentry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
oilLabel.grid(row=5,column=0,pady=8,padx=10,sticky='w')
oilLabelentry=Entry(groceryFrame,font=('arial',15),width=10,bd=5)
oilLabelentry.grid(row=5,column=1,pady=8,padx=10)
oilLabelentry.insert(0,0)

cooldrinksFrame=LabelFrame(productsFrame,text='Cool drinks',font=('Times New Roman',15,'bold'),bg='gray20',fg='gold',bd=4)
cooldrinksFrame.grid(row=0,column=2)
maazaLabel=Label(cooldrinksFrame,text='Maaza',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
maazaLabel.grid(row=0,column=0,pady=8,padx=10,sticky='w')
maazaLabelentry=Entry(cooldrinksFrame,font=('arial',15),width=10,bd=5)
maazaLabelentry.grid(row=0,column=1,pady=8,padx=10)
maazaLabelentry.insert(0,0)

pepsiLabel=Label(cooldrinksFrame,text='Pepsi',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
pepsiLabel.grid(row=1,column=0,pady=8,padx=10,sticky='w')
pepsiLabelentry=Entry(cooldrinksFrame,font=('arial',15),width=10,bd=5)
pepsiLabelentry.grid(row=1,column=1,pady=8,padx=10)
pepsiLabelentry.insert(0,0)

spriteLabel=Label(cooldrinksFrame,text='Sprite',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
spriteLabel.grid(row=2,column=0,pady=8,padx=10,sticky='w')
spriteLabelentry=Entry(cooldrinksFrame,font=('arial',15),width=10,bd=5)
spriteLabelentry.grid(row=2,column=1,pady=8,padx=10)
spriteLabelentry.insert(0,0)

dewLabel=Label(cooldrinksFrame,text='Mountain dew',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
dewLabel.grid(row=3,column=0,pady=8,padx=10,sticky='w')
dewLabelentry=Entry(cooldrinksFrame,font=('arial',15),width=10,bd=5)
dewLabelentry.grid(row=3,column=1,pady=8,padx=10)
dewLabelentry.insert(0,0)

frootiLabel=Label(cooldrinksFrame,text='Frooti',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
frootiLabel.grid(row=4,column=0,pady=8,padx=10,sticky='w')
frootiLabelentry=Entry(cooldrinksFrame,font=('arial',15),width=10,bd=5)
frootiLabelentry.grid(row=4,column=1,pady=8,padx=10)
frootiLabelentry.insert(0,0)

cocacolaLabel=Label(cooldrinksFrame,text='Coca cola',font=('Times New Roman',15,'bold'),bg='gray20',fg='white',bd=8)
cocacolaLabel.grid(row=5,column=0,pady=8,padx=10,sticky='w')
cocacolaLabelentry=Entry(cooldrinksFrame,font=('arial',15),width=10,bd=5)
cocacolaLabelentry.grid(row=5,column=1,pady=8,padx=10)
cocacolaLabelentry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)
billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=20,width=55,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill menu',font=('Times New Roman',10,'bold'),bg='gray20',fg='gold',bd=8)
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('Times New Roman',12,'bold'),bg='gray20',fg='white',bd=8)
cosmeticpriceLabel.grid(row=0,column=0,pady=4,padx=10,sticky='w')
cosmeticpriceLabelentry=Entry(billmenuFrame,font=('arial',12),width=10,bd=5)
cosmeticpriceLabelentry.grid(row=0,column=1,pady=4,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('Times New Roman',12,'bold'),bg='gray20',fg='white',bd=8)
grocerypriceLabel.grid(row=1,column=0,pady=4,padx=10,sticky='w')
grocerypriceLabelentry=Entry(billmenuFrame,font=('arial',12),width=10,bd=5)
grocerypriceLabelentry.grid(row=1,column=1,pady=4,padx=10)

cooldrinkspriceLabel=Label(billmenuFrame,text='CoolDrinks Price',font=('Times New Roman',12,'bold'),bg='gray20',fg='white',bd=8)
cooldrinkspriceLabel.grid(row=2,column=0,pady=4,padx=10,sticky='w')
cooldrinkspriceLabelentry=Entry(billmenuFrame,font=('arial',12),width=10,bd=5)
cooldrinkspriceLabelentry.grid(row=2,column=1,pady=4,padx=10)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('Times New Roman',12,'bold'),bg='gray20',fg='white',bd=8)
cosmetictaxLabel.grid(row=0,column=2,pady=4,padx=10,sticky='w')
cosmetictaxLabelentry=Entry(billmenuFrame,font=('arial',12),width=10,bd=5)
cosmetictaxLabelentry.grid(row=0,column=3,pady=4,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('Times New Roman',12,'bold'),bg='gray20',fg='white',bd=8)
grocerytaxLabel.grid(row=1,column=2,pady=4,padx=10,sticky='w')
grocerytaxLabelentry=Entry(billmenuFrame,font=('arial',12),width=10,bd=5)
grocerytaxLabelentry.grid(row=1,column=3,pady=4,padx=10)

cooldrinkstaxLabel=Label(billmenuFrame,text='CoolDrinks Tax',font=('Times New Roman',12,'bold'),bg='gray20',fg='white',bd=8)
cooldrinkstaxLabel.grid(row=2,column=2,pady=4,padx=10,sticky='w')
cooldrinkstaxLabelentry=Entry(billmenuFrame,font=('arial',12),width=10,bd=5)
cooldrinkstaxLabelentry.grid(row=2,column=3,pady=4,padx=10)

buttonframe=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=Total)
totalButton.grid(row=0,column=0,pady=20,padx=15)

billButton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=15)

emailButton=Button(buttonframe,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=15)

printButton=Button(buttonframe,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=Print_bill)
printButton.grid(row=0,column=3,pady=20,padx=15)

clearButton=Button(buttonframe,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=15)
root.mainloop()