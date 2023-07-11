from tkinter import*
root=Tk()
root.geometry("500x500")
root.config(bg="lightblue")

button_1=Button(root,text="calcular cosas")
button_1.place(relx=0.5,rely=0.5,anchor=CENTER)

class clase(self):
    def a(self,mango,pago):
        self.b=mango
        self.pago=int(pago)
        self.var1 = 200
        
    def b(self):
        var2=self.pago*self.var1
        print(var2)
    

root.mainloop()