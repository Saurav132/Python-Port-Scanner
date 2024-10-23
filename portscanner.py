import nmap
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import csv
import threading
from tkinter.ttk import Progressbar

# Initialize Nmap Port Scanner
nm = nmap.PortScanner()

# Function to perform port scan
def perform_scan():
    target = entry_target.get()  # Get target from user input
    port_range = entry_ports.get()  # Get port range from user input
    service_detection = var_service_detection.get()  # Check if service detection is selected
    os_detection = var_os_detection.get()  # Check if OS detection is selected
    
    # Clear the result window before starting a new scan
    text_result.delete(1.0, tk.END)

    if not target or not port_range:
        messagebox.showerror("Input Error", "Please enter both target and port range!")
        return

    # Set the Nmap arguments based on options
    nmap_args = '-sS'
    if service_detection:
        nmap_args += ' -sV'
    if os_detection:
        nmap_args += ' -O'
    
    # Function to run scanning in a separate thread
    def scan():
        try:
            btn_scan.config(state=tk.DISABLED)  # Disable the scan button during scanning
            progress_bar.start()
            
            scan_results = nm.scan(hosts=target, ports=port_range, arguments=nmap_args)
            
            progress_bar.stop()
            btn_scan.config(state=tk.NORMAL)  # Enable the scan button after scanning
            
            if target in scan_results['scan']:
                host_data = scan_results['scan'][target]
                if 'tcp' in host_data:
                    text_result.insert(tk.END, f"Scan Results for {target}:\n")
                    for port, details in host_data['tcp'].items():
                        if details['state'] == 'open':
                            service = details.get('name', 'unknown')
                            version = details.get('version', '')
                            product = details.get('product', '')
                            text_result.insert(tk.END, f"Port {port} is open ({service}) {product} {version}\n")
                else:
                    text_result.insert(tk.END, f"No open TCP ports found in range {port_range}.\n")
                
                if 'osclass' in host_data:
                    text_result.insert(tk.END, "\nOperating System Details:\n")
                    for os_class in host_data['osclass']:
                        os_name = os_class.get('osfamily', 'unknown')
                        os_vendor = os_class.get('vendor', 'unknown')
                        os_accuracy = os_class.get('accuracy', 'unknown')
                        text_result.insert(tk.END, f"OS: {os_name} (Vendor: {os_vendor}, Accuracy: {os_accuracy}%)\n")
            else:
                text_result.insert(tk.END, f"Unable to scan the target {target}.\n")
        except Exception as e:
            progress_bar.stop()
            btn_scan.config(state=tk.NORMAL)  # Re-enable the scan button after error
            text_result.insert(tk.END, f"Error scanning the target: {str(e)}\n")

    # Run the scan in a separate thread to avoid freezing the GUI
    threading.Thread(target=scan).start()

# Function to clear input fields and results
def clear_results():
    entry_target.delete(0, tk.END)
    entry_ports.delete(0, tk.END)
    text_result.delete(1.0, tk.END)

# Function to save the results to a CSV file
def save_results():
    results = text_result.get(1.0, tk.END).strip()
    if not results:
        messagebox.showerror("No Results", "No scan results to save!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if save_path:
        with open(save_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Scan Results"])
            writer.writerow([results])
        messagebox.showinfo("Saved", f"Results saved successfully to {save_path}")

# Create the main window
root = tk.Tk()
root.title("Advanced Python Port Scanner")
root.geometry("600x500")

# Target IP/Domain Label and Entry
label_target = tk.Label(root, text="Target IP/Domain:")
label_target.pack(pady=5)
entry_target = tk.Entry(root, width=50)
entry_target.pack(pady=5)

# Port Range Label and Entry
label_ports = tk.Label(root, text="Port Range (e.g., 1-1000):")
label_ports.pack(pady=5)
entry_ports = tk.Entry(root, width=50)
entry_ports.pack(pady=5)

# Checkbox for Service Detection
var_service_detection = tk.IntVar()
chk_service_detection = tk.Checkbutton(root, text="Enable Service Detection (-sV)", variable=var_service_detection)
chk_service_detection.pack(pady=5)

# Checkbox for OS Detection
var_os_detection = tk.IntVar()
chk_os_detection = tk.Checkbutton(root, text="Enable OS Detection (-O)", variable=var_os_detection)
chk_os_detection.pack(pady=5)

# Scan Button
btn_scan = tk.Button(root, text="Start Scan", command=perform_scan)
btn_scan.pack(pady=10)

# Clear Button
btn_clear = tk.Button(root, text="Clear", command=clear_results)
btn_clear.pack(pady=5)

# Save Results Button
btn_save = tk.Button(root, text="Save Results", command=save_results)
btn_save.pack(pady=5)

# Scrolled Text for Results
text_result = scrolledtext.ScrolledText(root, height=10, width=70)
text_result.pack(pady=10)

# Progress Bar for scan progress
progress_bar = Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='indeterminate')
progress_bar.pack(pady=10)

# Run the GUI loop
root.mainloop()
