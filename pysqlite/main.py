from tkinter import ttk
from tkinter import *
import sqlite3

class Productos:

    base = "productos.sqlite3"

    def __init__(self, root):
        self.wind = root
        self.wind.title("Proxductos")
        self.wind.geometry("850x600")

        frame1 = LabelFrame(self.wind, text="Informacion del producto", font=("calibri", 14))
        frame2 = LabelFrame(self.wind, text="Datos del producto", font=("calibri", 14))
        
        frame1.pack(fill="both", expand="yes", padx=20, pady=10)
        frame2.pack(fill="both", expand="yes", padx=20, pady=10)
        
        self.trv = ttk.Treeview(frame1, columns=(1,2,3,4), show="headings", height="5")
        self.trv.pack()
        self.trv.heading(1, text="ID del producto")
        self.trv.heading(2, text="Nombre")
        self.trv.heading(3, text="Precio")
        self.trv.heading(4, text="Cantidad")
        self.consulta()

        lbl1 = Label(frame2, text="ID del producto", width=20)
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        self.ent1 = Entry(frame2)
        self.ent1.grid(row=0, column=1, padx=5, pady=3)

        lbl1 = Label(frame2, text="Nombre del producto", width=20)
        lbl1.grid(row=1, column=0, padx=5, pady=3)
        self.ent2 = Entry(frame2)
        self.ent2.grid(row=1, column=1, padx=5, pady=3)

        lbl1 = Label(frame2, text="Precio del producto", width=20)
        lbl1.grid(row=2, column=0, padx=5, pady=3)
        self.ent3 = Entry(frame2)
        self.ent3.grid(row=2, column=1, padx=5, pady=3)

        lbl1 = Label(frame2, text="Cantidad del producto", width=20)
        lbl1.grid(row=3, column=0, padx=5, pady=3)
        self.ent4 = Entry(frame2)
        self.ent4.grid(row=3, column=1, padx=5, pady=3)

        btn1 = Button(frame2, text="Agregar", command=self.agregar, width=12, height= 1)
        btn1.grid(row=4, column=0)

        btn2 = Button(frame2, text="Eliminar", width=12, height= 1)
        btn2.grid(row=4, column=1)

        btn3 = Button(frame2, text="Acualizar", width=12, height= 1)
        btn3.grid(row=4, column=2)



    def runquery(self, query, parameters = ()):
        with sqlite3.connect(self.base) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
            return result
            
    def consulta(self):
        book = self.trv.get_children()
        for element in book:
            self.trv.delete(element)
        query = "SELECT ID, NOMBRE, PRECIO, CANTIDAD FROM ARTICULOS"
        rows = self.runquery(query)
        for row in rows:
            self.trv.insert('', 0, text=row[1], values=row)
        
    def validation(self):
        return len(self.ent1.get()) != 0 and len(self.ent2.get()) != 0 and len(self.ent3.get()) != 0 and len(self.ent4.get()) != 0
            
    def agregar(self):
        if (self.validation()):
            query = "INSERT INTO ARTICULOS (ID, NOMBRE, PRECIO, CANTIDAD) VALUES (?,?,?,?)"
            parameters = (self.ent1.get(), self.ent2.get(), self.ent3.get(), self.ent4.get())
            self.runquery(query, parameters)
            self.ent1.delete(0, END)
            self.ent2.delete(0, END)
            self.ent3.delete(0, END)
            self.ent4.delete(0, END)
        else:
            print("No salvado")
        self.consulta()

    def eliminar(self):
        try:
            self.trv.item(self.trv.selection())['text']
        except IndexError as e:
            pass


if __name__ == "__main__":
    root = Tk()
    product = Productos(root)
    root.mainloop()