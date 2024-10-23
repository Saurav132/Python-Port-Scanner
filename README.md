Python Port Scanner with GUI
Project Overview:
This project is a Python-based port scanner equipped with a Graphical User Interface (GUI) built using Tkinter. It leverages Nmap to perform advanced network scanning operations, such as detecting open ports, services running on those ports, and the operating system (OS) of the target machine. This project aims to provide both beginners and intermediate users a way to easily interact with port scanning functionality through a user-friendly interface.

Key Features:
Simple GUI: The project features an intuitive graphical interface that allows users to input the target IP address/domain and the range of ports to scan.
Port Scanning: Perform TCP SYN scans to identify open ports on the target system.
Service Detection: Option to enable service version detection (-sV), which identifies what services are running on the open ports.
OS Detection: Option to detect the operating system of the target host using the Nmap OS detection feature (-O).
Progress Bar: A visual progress bar shows the status of the scan while it's running, improving user experience.
Save Results: Scan results can be exported and saved as a CSV file for further analysis.
Clear and Reset: Users can clear the input fields and results for a new scan with the click of a button.
Technologies Used:
Python: The core programming language used to build the scanner.
Tkinter: The standard Python library used for creating the GUI.
Nmap: A powerful network scanning tool used to perform port and service scans.
How It Works:
The user inputs a target IP address or domain and specifies a port range to scan.
Optional checkboxes allow the user to enable service detection and OS detection for a more detailed scan.
When the "Start Scan" button is clicked, the program uses Nmap to scan the specified ports and display the results in the GUI.
Users can choose to save the results to a CSV file, which can be useful for network analysis and documentation.
The progress bar provides feedback during the scan, ensuring that the user can track the progress of the operation.
Installation and Setup:
To run this project, follow these steps:

Install Nmap:

Download and install Nmap from https://nmap.org/download.html.
Ensure that Nmap is accessible from your system's command line.

Potential Use Cases:
Network Security Auditing: Use the scanner to identify open ports and vulnerable services in a network.
Penetration Testing: This tool can assist in the initial reconnaissance phase of a penetration test by mapping the attack surface.
Educational Tool: A great project for students learning about networking and cybersecurity basics.
Future Improvements:
Multi-threading: Add support for multi-threaded scanning to speed up the process.
Authentication and Encryption: Implement SSH or SSL support for scanning secure services.
Interactive Report Generation: Allow for more detailed reporting with visual charts or graphs.
License:
This project is licensed under the MIT License.
