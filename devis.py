import tkinter as tk
from PIL import Image,ImageTk
from tkinter import PhotoImage
import os

root = tk.Tk()

background="blue"
framebg='blue'
framefg="blue"

label = tk.Label(root, text="ISPM\n" +
                              "Institue Supérieur Politechnique de Madagascar", 
                              font=("Helvetica", 12, "bold"), bg="#8FBC8F", fg="#000000", width=200, height=6)
label.pack(side=tk.TOP, fill=tk.X)

input_image_path = "image/logo.jpg"
# Chemin de sortie pour l'image convertie en GIF
output_image_path = "image/logo.gif"
# Ouvrir l'image JPG avec Pillow
with Image.open(input_image_path) as img:
    # Convertir l'image en mode RVB (si ce n'est pas déjà le cas)
    img = img.convert("RGB")
    # Enregistrer l'image au format GIF
    img.save(output_image_path, format="GIF")

    # Chargement de l'image convertie en format GIF
logo_image = PhotoImage(file="image/logo.gif")

largeur = 80  # Largeur désirée
hauteur = 5  # Hauteur désirée
logo_image = logo_image.subsample(2, 2) 
# Création d'un widget Label pour afficher le logo
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()
logo_label.place(x=50, y=5)

label = tk.Button(root, text="Acceuil", font="Arial 13", fg="black", bg="white").place(x=60,y=150)
label = tk.Button(root, text="Materiaux", font="Arial 13", fg="black", bg="white").place(x=700,y=150)
label = tk.Button(root, text="Devis", font="Arial 13", fg="black", bg="white").place(x=70,y=400)


class CalculSurfaceApp:
    def __init__(self, master):
        self.master = master
        master.title("ISPM MADAGASCAR")

        # Frame principale
        self.main_frame = tk.Frame(master, bg="#f0f0f0", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # LabelFrame pour l'entrée de la surface, le bouton de calcul et le calcul (à gauche)
        self.left_frame = tk.LabelFrame(self.main_frame, text="Devis", font=("Helvetica", 12, "bold"))
        self.left_frame.grid(row=0, column=0, padx=150, pady=10, sticky="nsew")

        # Titre
        self.title_label = tk.Label(self.left_frame, text="Calcul nombre matériaux", font=("Helvetica", 10, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="nsew")

        # Entrée de la surface
        self.surface_label = tk.Label(self.left_frame, text="Entrer vos nombre:",font=("Helvetica", 8, "bold"))
        self.surface_label.grid(row=1, column=0, sticky="w")
        self.surface_entry = tk.Entry(self.left_frame)
        self.surface_entry.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=(0, 10))

        # Bouton de calcul
        self.calculate_button = tk.Button(self.left_frame, text="Valider", command=self.calculate_surface, padx=15, pady=5, bd=0, bg="#4caf50", fg="white")
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky="ew")

        # Résultat
        self.result_label = tk.Label(self.left_frame, text="", bg="#f0f0f0", fg="#4caf50", font=("Helvetica", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=(20, 0), sticky="nsew")

        # LabelFrame pour les options de matériaux (à droite)
        self.right_frame = tk.LabelFrame(self.main_frame, text="Options de matériaux", font=("Helvetica", 12, "bold"))
        self.right_frame.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

        self.brique_var = tk.IntVar()
        self.agglo_var = tk.IntVar()
        self.bois_var = tk.IntVar()

        self.brique_checkbox = tk.Checkbutton(self.right_frame, text="Brique", variable=self.brique_var,font=("Helvetica", 8, "bold"))
        self.brique_checkbox.grid(row=0, column=0, sticky="w", padx=(10, 0))
        
        self.agglo_checkbox = tk.Checkbutton(self.right_frame, text="Agglo", variable=self.agglo_var,font=("Helvetica", 8, "bold"))
        self.agglo_checkbox.grid(row=1, column=0, sticky="w", padx=(10, 0))
        
        self.bois_checkbox = tk.Checkbutton(self.right_frame, text="Bois", variable=self.bois_var,font=("Helvetica", 8, "bold"))
        self.bois_checkbox.grid(row=2, column=0, sticky="w", padx=(10, 0))

    def calculate_surface(self):
        try:
            surface = float(self.surface_entry.get())
            total_surface = 0

            if self.brique_var.get() == 1:
                total_surface += surface * 100
            if self.agglo_var.get() == 1:
                total_surface += surface * 20
            if self.bois_var.get() == 1:
                total_surface += surface * 15

            self.result_label.config(text="Nombre total: {:.2f}".format(total_surface))
        except ValueError:
            self.result_label.config(text="Erreur: Veuillez entrer un nombre valide", fg="red")
app = CalculSurfaceApp(root)


root.geometry("900x500+210+100")
root.config(bg="#E0FFFF")
root.mainloop()
