import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, messagebox, StringVar, OptionMenu, ttk
import time
from bus import Bus
from train import Train

class TransportApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Transportasi Umum")

        # Membuat objek bus
        self.bus = Bus()

        # Membuat objek kereta api
        self.train = Train()
        
        # Menambahkan elemen-elemen antarmuka pengguna
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        # Label waktu
        self.time_label = tk.Label(master, text="", font=("Helvetica", 14, "bold"), fg="red")
        self.time_label.pack()

        # Tabel untuk menampilkan jadwal
        self.tree = ttk.Treeview(master, columns=("No.", "Transportasi", "Jadwal"), show="headings")
        self.tree.heading("No.", text="No.")
        self.tree.heading("Transportasi", text="Transportasi")
        self.tree.heading("Jadwal", text="Jadwal")
        self.tree.column("No.", width=50, anchor=tk.CENTER)  # Set lebar kolom untuk nomor urut
        self.tree.column("Transportasi", width=100, anchor=tk.CENTER)
        self.tree.column("Jadwal", width=200, anchor=tk.CENTER)
        self.tree.pack(pady=20)

        # Button untuk CRUD
        self.crud_frame = tk.Frame(master)
        self.crud_frame.pack(pady=10)

        self.add_button = tk.Button(self.crud_frame, text="Tambah", command=self.show_add_schedule_form)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(self.crud_frame, text="Edit", command=self.show_edit_schedule_form)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.crud_frame, text="Hapus", command=self.delete_schedule)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Memperbarui waktu secara teratur (setiap 1000 milidetik)
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=f"Waktu: {current_time}")
        self.master.after(1000, self.update_time)  # Panggil fungsi ini lagi setiap 1000 milidetik

    def display_schedule(self, transport_type=None):
        # Menghapus data yang ada pada tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Menampilkan jadwal untuk Bus
        bus_schedule = self.bus.display_info()
        for i, time_slot in enumerate(bus_schedule.split(", ")):
            self.tree.insert("", i, values=(i + 1, "Bus", time_slot))

        # Menampilkan jadwal untuk Kereta
        train_schedule = self.train.display_info()
        for j, time_slot in enumerate(train_schedule.split(", ")):
            self.tree.insert("", i + j + 1, values=(i + j + 2, "Kereta", time_slot))

        if transport_type:
            # Pilih transportasi yang sesuai jika diberikan
            if transport_type.lower() == "bus" and i > 0:
                self.tree.selection_set(i - 1)
            elif transport_type.lower() == "kereta" and i + j + 1 > 0:
                self.tree.selection_set(i + j + 1)

    def show_add_schedule_form(self):
        add_schedule_window = Toplevel(self.master)
        add_schedule_window.title("Tambah Jadwal Transportasi")

        # Label dan option menu untuk nama transportasi
        label_name = Label(add_schedule_window, text="Nama Transportasi:")
        label_name.grid(row=0, column=0, padx=10, pady=5)

        transport_options = ["Bus", "Kereta"]
        selected_transport = StringVar(add_schedule_window)
        selected_transport.set(transport_options[0])  # Set default value
        transport_menu = OptionMenu(add_schedule_window, selected_transport, *transport_options)
        transport_menu.grid(row=0, column=1, padx=10, pady=5)

        # Label dan entry untuk jadwal
        label_schedule = Label(add_schedule_window, text="Jadwal (pisahkan dengan koma):")
        label_schedule.grid(row=1, column=0, padx=10, pady=5)
        entry_schedule = Entry(add_schedule_window)
        entry_schedule.grid(row=1, column=1, padx=10, pady=5)

        # Button untuk menyimpan jadwal baru
        save_button = Button(add_schedule_window, text="Simpan", command=lambda: self.save_schedule(
            selected_transport.get(), entry_schedule.get(), add_schedule_window
        ))
        save_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_edit_schedule_form(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Pilih item terlebih dahulu.")
            return

        transport_type = self.tree.item(selected_item)["values"][1]
        current_schedule = self.tree.item(selected_item)["values"][2]

        edit_schedule_window = Toplevel(self.master)
        edit_schedule_window.title("Edit Jadwal Transportasi")

        # Label dan entry untuk nama transportasi
        label_name = Label(edit_schedule_window, text="Nama Transportasi:")
        label_name.grid(row=0, column=0, padx=10, pady=5)
        entry_name = Entry(edit_schedule_window, state="disabled")
        entry_name.insert(0, transport_type)
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Label dan entry untuk jadwal
        label_schedule = Label(edit_schedule_window, text="Jadwal (pisahkan dengan koma):")
        label_schedule.grid(row=1, column=0, padx=10, pady=5)
        entry_schedule = Entry(edit_schedule_window)
        entry_schedule.insert(0, current_schedule)
        entry_schedule.grid(row=1, column=1, padx=10, pady=5)

        # Button untuk menyimpan jadwal yang sudah diedit
        save_button = Button(edit_schedule_window, text="Simpan", command=lambda: self.edit_schedule(
            selected_item, entry_schedule.get(), edit_schedule_window
        ))
        save_button.grid(row=2, column=0, columnspan=2, pady=10)

    def save_schedule(self, name, schedule, window):
        # Validasi input
        if not name or not schedule:
            messagebox.showerror("Error", "Mohon isi semua field.")
            return

        # Menambahkan jadwal baru sesuai jenis transportasi
        if name.lower().startswith("bus"):
            self.bus.add_schedule(schedule)
        elif name.lower().startswith("kereta"):
            self.train.add_schedule(schedule)
        else:
            messagebox.showerror("Error", "Jenis transportasi tidak dikenali.")

        # Menampilkan pesan sukses
        messagebox.showinfo("Sukses", f"Jadwal {name} berhasil ditambahkan.")

        # Menutup jendela formulir
        window.destroy()

        # Memperbarui tampilan tabel
        self.display_schedule()

    def edit_schedule(self, selected_item, new_schedule, window):
        # Validasi input
        if not new_schedule:
            messagebox.showerror("Error", "Mohon isi field jadwal.")
            return

        transport_type = self.tree.item(selected_item)["values"][1]

        # Mengedit jadwal sesuai jenis transportasi
        if transport_type.lower().startswith("bus"):
            selected_index = self.tree.index(selected_item)
            self.bus.schedules[selected_index] = new_schedule
        elif transport_type.lower().startswith("kereta"):
            selected_index = self.tree.index(selected_item)
            self.train.schedules[selected_index - len(self.bus.schedules)] = new_schedule
        else:
            messagebox.showerror("Error", "Jenis transportasi tidak dikenali.")

        # Menampilkan pesan sukses
        messagebox.showinfo("Sukses", f"Jadwal {transport_type} berhasil diubah.")

        # Menutup jendela formulir
        window.destroy()

        # Memperbarui tampilan tabel
        self.display_schedule()
        
    def delete_schedule(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Pilih item terlebih dahulu.")
            return

        transport_type = self.tree.item(selected_item)["values"][1]

        # Menghapus jadwal sesuai jenis transportasi
        if transport_type.lower().startswith("bus"):
            self.bus.schedule = ""
        elif transport_type.lower().startswith("kereta"):
            self.train.schedule = ""
        else:
            messagebox.showerror("Error", "Jenis transportasi tidak dikenali.")
            return

        # Menampilkan pesan sukses
        messagebox.showinfo("Sukses", f"Jadwal {transport_type} berhasil dihapus.")

        # Menghapus item dari tabel
        self.tree.delete(selected_item)

def main():
    root = tk.Tk()
    app = TransportApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
