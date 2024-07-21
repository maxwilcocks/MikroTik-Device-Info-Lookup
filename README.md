# MikroTik Device Info Lookup

## Overview

The MikroTik Device Info Lookup tool is designed to help WISP installation technicians and non-technical staff quickly and easily fetch DHCP lease information for devices connected to MikroTik routers. This tool was developed to simplify the process for installation technicians, making it easier for them to retrieve necessary information without needing to perform network scans or have deep technical knowledge of router configurations.

## Features

- **Easy Login:** Enter your MikroTik router username and password.
- **Select Tower:** Choose the connected tower/router from a dropdown menu.
- **MAC Address Lookup:** Enter a MAC address to fetch detailed DHCP lease information from the connected MikroTik's DHCP server.

## How It Works

1. **Configuration:** The tool uses a `config.ini` file to store router IP addresses and default login credentials.
2. **Login:** The user enters the MikroTik router's username and password.
3. **Select Tower:** The user selects the tower they're connecting to from a dropdown menu.
4. **MAC Address Lookup:** The user enters the MAC address of the device they want to look up.
5. **Fetch Info:** The tool retrieves detailed DHCP lease information from the selected MikroTik's DHCP server.

## Information Pulled

When a MAC address is entered and the information is fetched, the tool retrieves and displays the following DHCP lease information:
- **MAC Address:** The MAC address of the device.
- **IP Address:** The IP address assigned to the device.
- **Hostname:** The hostname of the device.
- **Active Address:** The current active IP address of the device.
- **Lease Time:** The time duration for which the lease is valid.
- **Comment:** Any comments associated with the lease.

## Installation

### Python Dependencies

Ensure you have Python installed. You can install the required dependencies using pip:

```sh
pip install -r requirements.txt
