
# -- CHARGER BIBLIOTHEQUE ---------------------------
# ESP8266 NEOPIXEL - utiliser bibliothèque native
from machine import Pin
from neopixel import NeoPixel

# ESP8266 Définir la broche_sortie et la configurer en sortie
pixel_pin = Pin(2, Pin.OUT)

# -- INSTANCE NEOPIXEL ------------------------------
# ESP8266 NeoPixel( broche_signal, nbre_de_led )
np = NeoPixel(pixel_pin, 7)

# Fixer la couleur la couleur du premier pixel
# avec un tuple (r,g,b) ou chaque valeur est
# située entre 0 et 255
np[0] = (255,0,0) # rouge

# couleur des autres pixels
np[1] = (0, 255, 0) # vert
np[2] = (0, 0, 128) # bleu (1/2 brillance)

# Envoyer l'info au NeoPixels
np.write()
