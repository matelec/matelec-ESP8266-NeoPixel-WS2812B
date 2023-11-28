
# -- CHARGER BIBLIOTHEQUE ---------------------------
# ESP8266 NEOPIXEL - utiliser bibliothèque native
from machine import Pin
from neopixel import NeoPixel

# ESP8266 Définir la broche_sortie et la configurer en sortie
pixel_pin = Pin(2, Pin.OUT)

# -- INSTANCE NEOPIXEL ------------------------------
# ESP8266 NeoPixel( broche_signal, nbre_de_led )
np = NeoPixel(pixel_pin, 4)

# Fixer la couleur la couleur du premier pixel
# avec un tuple (r,g,b) ou chaque valeur est
# située entre 0 et 255
np[0] = (255,0,0) # rouge

# couleur des autres pixels
np[1] = (255,0,0) # vert
np[2] = (255,0,0) # bleu (1/2 brillance)
np[3] = (255,0,0)
# Envoyer l'info au NeoPixels
np.write()
