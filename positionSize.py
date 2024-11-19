import tkinter as tk
from tkinter import messagebox

def calculate_position_size():
    try:
        # Prendere gli input dall'utente
        capital = float(capital_entry.get())
        risk_per_trade_percent = float(risk_entry.get()) / 100
        entry_price = float(entry_price_entry.get())
        stop_loss_price = float(stop_loss_entry.get())
        risk_adjustment = float(risk_adjustment_entry.get())

        # Calcolo del rischio monetario per trade
        risk_per_trade = capital * risk_per_trade_percent

        # Calcolo della distanza tra prezzo di entrata e stop loss
        risk_distance = entry_price - stop_loss_price

        if risk_distance <= 0:
            messagebox.showerror("Errore", "Il prezzo di entrata deve essere maggiore dello stop loss.")
            return

        # Calcolo della size della posizione
        position_size = (risk_per_trade * risk_adjustment) / risk_distance

        # Mostrare il risultato
        result_label.config(text=f"Position Size: {position_size:.6f} unità")
    except ValueError:
        messagebox.showerror("Errore", "Per favore, inserisci valori validi.")

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatore Position Sizing - Altcoin")

# Etichette e campi di input
tk.Label(root, text="Capitale Totale (USD):").grid(row=0, column=0, padx=10, pady=10)
capital_entry = tk.Entry(root)
capital_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Rischio per Trade (%):").grid(row=1, column=0, padx=10, pady=10)
risk_entry = tk.Entry(root)
risk_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Prezzo di Entrata (USD):").grid(row=2, column=0, padx=10, pady=10)
entry_price_entry = tk.Entry(root)
entry_price_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Stop Loss Price (USD):").grid(row=3, column=0, padx=10, pady=10)
stop_loss_entry = tk.Entry(root)
stop_loss_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Coefficiente di Rischio (0-1):").grid(row=4, column=0, padx=10, pady=10)
risk_adjustment_entry = tk.Entry(root)
risk_adjustment_entry.grid(row=4, column=1, padx=10, pady=10)

# Pulsante per calcolare
calculate_button = tk.Button(root, text="Calcola", command=calculate_position_size)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Etichetta per mostrare il risultato
result_label = tk.Label(root, text="Position Size: ")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Avvio dell'interfaccia grafica
root.mainloop()
