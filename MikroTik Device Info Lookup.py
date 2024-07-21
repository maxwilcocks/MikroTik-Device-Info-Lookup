import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser
from librouteros import connect

def fetch_device_info():
    mac_address = entry_mac.get().upper()
    if not validate_mac_address(mac_address):
        messagebox.showerror("Invalid MAC Address", "Please enter a valid MAC address in the format XX:XX:XX:XX:XX:XX")
        return

    try:
        selected_router = router_var.get()
        host = config['routers'][selected_router]

        api = connect(username=username, password=password, host=host)
        leases = api(cmd='/ip/dhcp-server/lease/print')

        info_text.delete("1.0", tk.END)
        found = False
        for lease in leases:
            if lease.get('mac-address') == mac_address:
                found = True
                for key, value in lease.items():
                    info_text.insert(tk.END, f"{key}: {value}\n")
                break
        if not found:
            info_text.insert(tk.END, "No information found for the given MAC address.")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to connect to MikroTik API: {e}")

def validate_mac_address(mac):
    if len(mac) != 17 or not all(c in "0123456789ABCDEF:" for c in mac):
        return False
    return True

def auto_fill_colons(event):
    mac = entry_mac.get().replace(":", "").upper()
    if len(mac) > 12:
        mac = mac[:12]
    formatted_mac = ":".join([mac[i:i+2] for i in range(0, len(mac), 2)])
    entry_mac.delete(0, tk.END)
    entry_mac.insert(0, formatted_mac)

def login():
    global username, password
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Login Error", "Please enter the username and password.")
        return

    messagebox.showinfo("Login Success", "Login credentials saved successfully!")

def clear():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_mac.delete(0, tk.END)
    info_text.delete("1.0", tk.END)

# Load configuration
config = ConfigParser()
config.read('config.ini')

# GUI setup
root = tk.Tk()
root.title("MikroTik Device Info Lookup")

label_tool_name = tk.Label(root, text="MikroTik Device Info Lookup", font=("Helvetica", 16, "bold"))
label_tool_name.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

label_username = tk.Label(root, text="Username:")
label_username.grid(row=1, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=1, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=2, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=10)

label_router = tk.Label(root, text="Router:")
label_router.grid(row=3, column=0, padx=10, pady=10)

router_var = tk.StringVar(root)
router_var.set(list(config['routers'].keys())[0])  # default value

dropdown_router = tk.OptionMenu(root, router_var, *config['routers'].keys())
dropdown_router.grid(row=3, column=1, padx=10, pady=10)

button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=3, column=2, padx=10, pady=10)

label_mac = tk.Label(root, text="MAC Address:")
label_mac.grid(row=4, column=0, padx=10, pady=10)

entry_mac = tk.Entry(root)
entry_mac.grid(row=4, column=1, padx=10, pady=10)
entry_mac.bind("<KeyRelease>", auto_fill_colons)

button_fetch = tk.Button(root, text="Fetch Info", command=fetch_device_info)
button_fetch.grid(row=4, column=2, padx=10, pady=10)

button_clear = tk.Button(root, text="Clear", command=clear)
button_clear.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

info_text = tk.Text(root, width=60, height=20)
info_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
