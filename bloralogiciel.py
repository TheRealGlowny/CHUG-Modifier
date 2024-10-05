import winreg
import tkinter as tk
from tkinter import messagebox
import ctypes

def change_gpu_details():
    gpu_description = gpu_description_entry.get()
    gpu_family_name = gpu_family_name_entry.get()
    gpu_manufacturer = gpu_manufacturer_entry.get()
    
    if not gpu_description or not gpu_family_name or not gpu_manufacturer:
        messagebox.showwarning("Input Error", "Please enter GPU description, family name, and manufacturer.")
        return
    
    try:
        # Modifier les détails pour le GPU
        gpu_key_path = r"SYSTEM\ControlSet001\Enum\PCI\VEN_10DE&DEV_2187&SUBSYS_38501462&REV_A1\4&1bced36e&0&0019"
        gpu_reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, gpu_key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(gpu_reg_key, "DeviceDesc", 0, winreg.REG_SZ, gpu_description)
        winreg.SetValueEx(gpu_reg_key, "FriendlyName", 0, winreg.REG_SZ, gpu_family_name)
        winreg.SetValueEx(gpu_reg_key, "Manufacturer", 0, winreg.REG_SZ, gpu_manufacturer)
        winreg.CloseKey(gpu_reg_key)
        
        messagebox.showinfo("Success", "GPU details changed successfully.")
    except PermissionError:
        messagebox.showerror("Permission Error", "Run this program as Administrator to modify system settings.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def change_cpu_details():
    cpu_description = cpu_description_entry.get()
    cpu_family_name = cpu_family_name_entry.get()
    cpu_manufacturer = cpu_manufacturer_entry.get()
    
    if not cpu_description or not cpu_family_name or not cpu_manufacturer:
        messagebox.showwarning("Input Error", "Please enter CPU description, family name, and manufacturer.")
        return
    
    try:
        # Modifier les détails pour le CPU
        cpu_key_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
        cpu_reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cpu_key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(cpu_reg_key, "ProcessorNameString", 0, winreg.REG_SZ, cpu_description)
        winreg.SetValueEx(cpu_reg_key, "Identifier", 0, winreg.REG_SZ, cpu_family_name)
        winreg.SetValueEx(cpu_reg_key, "Manufacturer", 0, winreg.REG_SZ, cpu_manufacturer)
        winreg.CloseKey(cpu_reg_key)
        
        messagebox.showinfo("Success", "CPU details changed successfully.")
    except PermissionError:
        messagebox.showerror("Permission Error", "Run this program as Administrator to modify system settings.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Interface graphique
app = tk.Tk()
app.title("CHUG Modifier by Glowny")
app.geometry("400x400")
app.configure(bg="#282c34")

# Styles
header_label = tk.Label(app, text="Change GPU and CPU Details", font=("Arial", 16), bg="#282c34", fg="#61afef")
header_label.pack(pady=10)

# GPU Section
gpu_label = tk.Label(app, text="Enter new GPU details:", font=("Arial", 12), bg="#282c34", fg="#ffffff")
gpu_label.pack(pady=5)

gpu_family_name_entry = tk.Entry(app, width=40)
gpu_family_name_entry.insert(0, "GPU Family Name")
gpu_family_name_entry.pack(pady=5)

gpu_description_entry = tk.Entry(app, width=40)
gpu_description_entry.insert(0, "GPU Description")
gpu_description_entry.pack(pady=5)

gpu_manufacturer_entry = tk.Entry(app, width=40)
gpu_manufacturer_entry.insert(0, "GPU Manufacturer")
gpu_manufacturer_entry.pack(pady=5)

# Button to change GPU details
change_gpu_button = tk.Button(app, text="Change GPU Details", command=change_gpu_details, bg="#61afef", fg="#ffffff")
change_gpu_button.pack(pady=10)

# CPU Section
cpu_label = tk.Label(app, text="Enter new CPU details:", font=("Arial", 12), bg="#282c34", fg="#ffffff")
cpu_label.pack(pady=5)

cpu_family_name_entry = tk.Entry(app, width=40)
cpu_family_name_entry.insert(0, "CPU Family Name")
cpu_family_name_entry.pack(pady=5)

cpu_description_entry = tk.Entry(app, width=40)
cpu_description_entry.insert(0, "CPU Description")
cpu_description_entry.pack(pady=5)

cpu_manufacturer_entry = tk.Entry(app, width=40)
cpu_manufacturer_entry.insert(0, "CPU Manufacturer")
cpu_manufacturer_entry.pack(pady=5)

# Button to change CPU details
change_cpu_button = tk.Button(app, text="Change CPU Details", command=change_cpu_details, bg="#61afef", fg="#ffffff")
change_cpu_button.pack(pady=10)

app.mainloop()
