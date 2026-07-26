# Matrix Switch Controller Fixer

A lightweight, Matrix-themed Python GUI utility for Linux (Mint/Ubuntu) that fixes third-party Nintendo Switch Pro Controller connectivity issues and force-restarts Steam Input.

---

## Features
- Overrides raw `/dev/hidraw` device permissions
- Triggers Bluetooth scan and connects stored gamepads
- Restarts Steam cleanly to force device re-detection
- Cyberpunk / Matrix-styled terminal GUI console

---

## How to Find Your Controller MAC Addresses

Before running the script, you need to grab the MAC address for each of your controllers.

1. Put your controller into pairing mode (hold the sync button until the lights flash).
2. Open a terminal and start scanning:
   `bluetoothctl --timeout 5 scan on`
3. Look for your controller in the output list. It will display a MAC address structured like `XX:XX:XX:XX:XX:XX`:
   `[NEW] Device 30:31:7D:EF:A2:D9 Pro Controller`
4. Copy the MAC address (`30:31:7D:EF:A2:D9`) for each device you want to connect.

---

## Setup & Usage

1. Open `controller_fixer.py` in a text editor.
2. Replace the placeholder MAC addresses with your own:
   CONTROLLER_1 = "YOUR_FIRST_MAC_HERE"
   CONTROLLER_2 = "YOUR_SECOND_MAC_HERE"
3. Run the application:
   `python3 controller_fixer.py`
4. Click `[ OVERRIDE & LAUNCH ]` to pair your gamepads and relaunch Steam.
