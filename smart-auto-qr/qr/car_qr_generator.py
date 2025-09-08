import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# ----------------------
# 📄 VEHICLE INFO
# ----------------------
vehicle_info = {
    "Owner": "Dhanush",
    "Vehicle Number": "TS09AB1234",
    "Car Model": "Hyundai i20",
    "Phone": "Hidden",
    "Message": "Scan to request contact"
}

# Link to webpage (you can change to your domain later)
qr_data = f"http://localhost:5000/vehicle/{vehicle_info['Vehicle Number']}"

# ----------------------
# 🧱 GENERATE QR
# ----------------------
qr = qrcode.QRCode(version=1, box_size=6, border=2)
qr.add_data(qr_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

# Resize QR
qr_img = qr_img.resize((200, 200))

# ----------------------
# 🏎️ LOAD CAR IMAGE
# ----------------------
car_image_path = "assets/car_frame.png"
if not os.path.exists(car_image_path):
    print("❌ Car image not found:", car_image_path)
    exit()

car_img = Image.open(car_image_path).convert("RGBA")
car_img = car_img.resize((400, 300))  # Resize car to uniform size

# ----------------------
# 🖼️ CREATE FINAL STICKER CANVAS
# ----------------------
canvas = Image.new("RGBA", (450, 500), "white")
canvas.paste(car_img, (25, 20), car_img)

# Paste QR in the middle of the car image
canvas.paste(qr_img, (125, 60), qr_img)

# ----------------------
# ✏️ ADD TEXT
# ----------------------
draw = ImageDraw.Draw(canvas)
font_path = "C:/Windows/Fonts/arial.ttf"  # Use any font installed
font = ImageFont.truetype(font_path, 18)

text_y = 320
for key in ["Vehicle Number", "Owner", "Car Model"]:
    value = vehicle_info[key]
    draw.text((20, text_y), f"{key}: {value}", font=font, fill="black")
    text_y += 30

# ----------------------
# 💾 SAVE
# ----------------------
output_path = "car_qr_sticker.png"
canvas.save(output_path)
print(f"✅ Sticker saved at: {output_path}")
