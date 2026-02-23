import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to predict spam or not
def check_spam():
    message = entry.get("1.0", tk.END).strip()
    
    if message == "":
        messagebox.showwarning("Warning", "Please enter a message!")
        return
    
    # Transform input text
    message_vector = vectorizer.transform([message])
    
    # Predict
    prediction = model.predict(message_vector)
    
    if prediction[0] == 1:
        result_label.config(text="Spam Message ❌", fg="red")
    else:
        result_label.config(text="Not Spam ✅", fg="green")

# Create GUI window
root = tk.Tk()
root.title("Spam Detection App")
root.geometry("500x400")
root.resizable(False, False)

# Heading
title_label = tk.Label(root, text="Spam Email Detection", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Text box
entry = tk.Text(root, height=8, width=50)
entry.pack(pady=10)

# Button
check_button = tk.Button(root, text="Check", command=check_spam, bg="blue", fg="white")
check_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run app
root.mainloop()