import base64

caminho = r"C:\Users\seidi\Pictures\Screenshots\Captura de tela 2026-11-10 234756.png"

with open(caminho, "rb") as file:
    image_base64 = base64.b64encode(file.read()).decode("utf-8")

print(image_base64)