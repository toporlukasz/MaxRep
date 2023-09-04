import tkinter as tk
from tkinter import messagebox

def oblicz_maksymalny_ciezar():
    try:
        c = float(ciezar_entry.get())
        p = int(powtorzenia_entry.get())

        maksymalny_ciezar = c * p * 0.03333333 + c
        wynik_label.config(text=f"Maksymalny ciężar: {maksymalny_ciezar:.2f}")

        if ten_sam_mc.get():
            aktualizuj_tabele(maksymalny_ciezar, p, "Ciężar (Ten sam max)")
        else:
            aktualizuj_tabele(c, p, "Ciężar")
        
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne dane (ciężar powinien być liczbą, a ilość powtórzeń liczbą całkowitą).")

def aktualizuj_tabele(ciezar, powtorzenia, naglowek):
    tabela_text.config(state=tk.NORMAL)
    tabela_text.delete(1.0, tk.END)
    tabela_text.insert(tk.END, f"{'Reps':<10}{'{:<32}'.format(naglowek)}{'{:<10}'.format('Estimated max')}\n")
    for p in range(1, 11):
        if ten_sam_mc.get():
            wynik = ciezar / (p * 0.03333333333 + 1)
            tabela_text.insert(tk.END, f"{p:<10}{wynik:<32.2f}{ciezar:<10.2f}\n")


        else:
            wynik = ciezar * p * 0.03333333 + ciezar
            tabela_text.insert(tk.END, f"{p:<10}{'{:<32}'.format(ciezar)}{'{:.2f}'.format(wynik):<10}\n")
    tabela_text.config(state=tk.DISABLED)

def toggle_rozszerzona_tabela():
    if not rozszerzona_tabela.get():
        tabela_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        tabela_button.config(text="Ukryj zwiększoną tabelę")
    else:
        tabela_text.grid_forget()
        tabela_button.config(text="Wyświetl zwiększoną tabelę")
    
    rozszerzona_tabela.set(not rozszerzona_tabela.get())

def toggle_ten_sam_mc():
    oblicz_maksymalny_ciezar()

root = tk.Tk()
root.title("Kalkulator Maksymalnego Ciężaru")

ciezar_label = tk.Label(root, text="Ciężar podnoszony w serii:")
ciezar_entry = tk.Entry(root)
powtorzenia_label = tk.Label(root, text="Ilość powtórzeń w serii:")
powtorzenia_entry = tk.Entry(root)
oblicz_button = tk.Button(root, text="Oblicz", command=oblicz_maksymalny_ciezar)
wynik_label = tk.Label(root, text="Maksymalny ciężar:")
tabela_button = tk.Button(root, text="Wyświetl zwiększoną tabelę", command=toggle_rozszerzona_tabela)
ten_sam_mc = tk.BooleanVar()
ten_sam_mc_check = tk.Checkbutton(root, text="Przelicz na 'Ten sam max'", variable=ten_sam_mc, command=toggle_ten_sam_mc)
rozszerzona_tabela = tk.BooleanVar()

tabela_text = tk.Text(root, height=15, width=60)
tabela_text.config(state=tk.DISABLED)

ciezar_label.grid(row=0, column=0, padx=10, pady=10)
ciezar_entry.grid(row=0, column=1, padx=10, pady=10)
powtorzenia_label.grid(row=1, column=0, padx=10, pady=10)
powtorzenia_entry.grid(row=1, column=1, padx=10, pady=10)
oblicz_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
wynik_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
tabela_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
ten_sam_mc_check.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
