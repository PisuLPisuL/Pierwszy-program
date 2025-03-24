import tkinter as tk
from tkinter import messagebox

def przelicz_wzrost():
    try:
        operacja = operacja_var.get()
        wzrost = float(wzrost_entry.get())

        # Przeliczanie na cm lub inch
        if operacja == "1":
            jednostka = "inch"
            wynik_cm = round(wzrost * 2.54, 3)
            wynik_label.config(text=f"{wzrost} inch = {wynik_cm} cm", bg="white", fg="navy", font=("Arial", 16, "bold"))
        elif operacja == "2":
            jednostka = "cm"
            wynik_inch = round(wzrost * 0.393701, 3)
            wynik_label.config(text=f"{wzrost} cm = {wynik_inch} inch", bg="white", fg="navy", font=("Arial", 16, "bold"))
        else:
            messagebox.showerror("Błąd", "Dokonano niewłaściwego wyboru.")
            return

        # Przeliczenie na stopy, jeśli wybrano "Y"
        if przeliczenie_var.get() == "Y":
            if jednostka == "cm":
                stopki = round(wzrost * 0.0328084, 3)
                stopki_label.config(text=f"{wzrost} cm = {stopki} feet", bg="white", fg="navy", font=("Arial", 14))
            else:
                stopki = round(wzrost * 0.0833333, 3)
                stopki_label.config(text=f"{wzrost} inch = {stopki} feet", bg="white", fg="navy", font=("Arial", 14))
        else:
            stopki_label.config(text="")

    except ValueError:
        messagebox.showerror("Błąd", "Proszę podać poprawny wzrost!")

# Utworzenie głównego okna
root = tk.Tk()
root.title("Przelicznik jednostek")
root.geometry("400x450")  # Większy rozmiar okna, aby pomieścić wyniki

# Opis i etykieta
etkieta_wzrost = tk.Label(root, text="Podaj wzrost/odległość:")
etkieta_wzrost.pack(pady=10)

# Pole do wpisania wzrostu
wzrost_entry = tk.Entry(root)
wzrost_entry.pack(pady=10)

# Wybór jednostki (inch / cm)
operacja_var = tk.StringVar(value="1")
operacja_label = tk.Label(root, text="Wybierz jednostkę:")
operacja_label.pack(pady=5)

operacja_inch = tk.Radiobutton(root, text="Inch na cm", variable=operacja_var, value="1")
operacja_inch.pack()

operacja_cm = tk.Radiobutton(root, text="Cm na inch", variable=operacja_var, value="2")
operacja_cm.pack()

# Czy przeliczyć na stopy?
przeliczenie_var = tk.StringVar(value="N")
przeliczenie_label = tk.Label(root, text="Czy chcesz przeliczyć na stopy? (Y/N):")
przeliczenie_label.pack(pady=5)

przeliczenie_yes = tk.Radiobutton(root, text="Tak (Y)", variable=przeliczenie_var, value="Y")
przeliczenie_yes.pack()

przeliczenie_no = tk.Radiobutton(root, text="Nie (N)", variable=przeliczenie_var, value="N")
przeliczenie_no.pack()

# Przycisk do obliczeń
przycisk_oblicz = tk.Button(root, text="Przelicz", command=przelicz_wzrost)
przycisk_oblicz.pack(pady=20)

# Miejsce na wynik cm/inch
wynik_label = tk.Label(root, text="", font=("Arial", 16), width=30, height=2)
wynik_label.pack(pady=10)

# Miejsce na wynik przeliczenia na stopy
stopki_label = tk.Label(root, text="", font=("Arial", 14), width=30, height=2)
stopki_label.pack(pady=10)

# Uruchomienie okna
root.mainloop()


