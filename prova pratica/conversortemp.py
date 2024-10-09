import customtkinter as ctk

#-------Funções--------------

def button1():
    n1 = float(num1.get())
    kel = n1 + 273.15
    resultado.configure(text=f'{n1}• graus celsius para kelvin é : {kel}• graus kelvin')

def button2():
    n1 = float(num1.get())
    fah = (n1*9/5) + 32
    resultado.configure(text=f'{n1}• graus celsius para  fahrenheit é : {fah}• fahrenheit')









#-------------------------------

janela = ctk.CTk()
janela.geometry('800x600')
janela.title("Conversor de temperatura")
janela.resizable(width=False,height=False)
ctk.set_appearance_mode('dark')


ctk.CTkLabel(janela,
             text='Conversor de temperatura',
             font=('verdana',50,'bold')).pack(pady=20)


num1 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    placeholder_text='Digite a temperuta em celsius: ',
                    )
num1.pack(pady=10)


botao1 = ctk.CTkButton(janela,
                      width=400,
                      height=30,
                      text='Converter para kelvin',
                      cursor='hand2',
                      command=button1)
botao1.pack(pady=10)
botao2 = ctk.CTkButton(janela,
                      width=400,
                      height=30,
                      text='conveter para fahrenheit',
                      cursor='hand2',
                      command=button2)
botao2.pack(pady=10)


resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('verdana',15,'bold'))
resultado.pack(pady=10)









janela.mainloop()