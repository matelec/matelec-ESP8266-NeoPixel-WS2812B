
# -- CHARGER BIBLIOTHEQUE ---------------------------
# ESP8266 NEOPIXEL - utiliser bibliothèque native
from machine import Pin
from neopixel import NeoPixel

# ESP8266 Définir la broche_sortie et la configurer en sortie
pixel_pin = Pin(2, Pin.OUT)

# -- INSTANCE NEOPIXEL ------------------------------
# ESP8266 NeoPixel( broche_signal, nbre_de_led )
np = NeoPixel(pixel_pin, 7)

# Fixer la couleur la couleur de la totalité des pixels
# avec un tuple (r,g,b).
np.fill((255, 0, 0)) # rouge

# Envoyer l'info aux NeoPixels
np.write()
