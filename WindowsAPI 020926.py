import time
import ctypes
import webbrowsw

# 1. Bloqueia a tela
ctypes.windll.user32.LockWorkStation()

# 2. Espera
time.sleep(2)

# 3. Move o mouse
ctypes.windll.user32.SetCursorPos(500, 300)