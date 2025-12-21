**Bilal’s MacroPad**  
It is my first ever engineering-related project and I think I did really good. It consists of 6 keys using Seeed XIAO RP2040 with a rotary encoder and 128x64 OLED display.

It will be helping me making my time more efficient and help me in tasks that are very common but are taking too much time off my schedule \+ I can always change its code to program it the way I want.

**Features:** 

* 6 MX-style keys (in a 3×2 layout)  
* EC11 rotary encoder  
  (Rotate: Volume Up / Down  
  Press: Mute)  
* 0.91” 128×64 OLED display

(- Shows volume level  
\- Encoder press state  
\- Last key pressed)

* Direct GPIO wiring  
* Macro-ready firmware \- keys can be easily remapped  
* No RGB \- clean, simple, and functional (and maybe minimalistic)

**CAD Model:**  
The model is really simple, just using the simple guide. Top and bottom part held together with 4 M3 screws and headset inserts while having cut-outs for 6 switches, a rotary knob and the display. 

It has 2 separate printed parts, a bottom base that holds the pcb and everything on top while the top plate hides it all.
<img width="1280" height="516" alt="Final HackPad (Fully Assembled)2" src="https://github.com/user-attachments/assets/00e491bd-b7ca-440e-9935-fafb1da5a165" />

 
Made in Fusion360 (using it for the first time btw :\>). I noticed it right now that I didn’t add the 3D model of XIAO RP 2040 (I wonder if it even exists)   
**PCB:**  
Here is my PCB\! I made it myself in KiCad with the help of a tutorial at HackClub and some google too\! It is a 2 layered PCB board with through-hole XIAO RP2040, 6 switches, a rotary knob and an OLED display. 

<img width="673" height="527" alt="Screenshot 2025-12-21 at 10 57 12 PM" src="https://github.com/user-attachments/assets/f3961b03-5e4e-43ac-a7a3-9091947357d0" />

Schematic

 <img width="582" height="519" alt="Screenshot 2025-12-21 at 10 58 25 PM" src="https://github.com/user-attachments/assets/6254cd8b-5f3e-48c3-9eda-5ff5a6bd22e7" />

PCB  
**Firmware:**  
This hackpad uses KMK firmware for everything, written in CircuitPython it can handle 6 keys functions (which is really easy to change, just edit it in keyboard.keymap in [main.py](http://main.py)), a rotary knob for volume up/down and pressing it down mutes the volume and an OLED showing volume level, encoder press state and the last key pressed.

## **Bill of Materials (BOM)**

* 1× Seeed XIAO RP2040 (through-hole)  
* 6× MX-style mechanical switches  
* 6× Blank DSA keycaps (white)  
* 1× EC11 rotary encoder  
* 1× 0.91” OLED display (128×64, I²C)  
* 4× M3×16mm screws  
* 4× M3 heatset inserts  
* 1× 3D printed case (top \+ bottom)  
* Custom PCB (2-layer)  
* CircuitPython \+ KMK firmware

## **Notes**

* No RGB LEDs were used in this design.  
* All parts comply with the provided allowed materials list (by hackclub).  
* The project stays within all size and input limits.
