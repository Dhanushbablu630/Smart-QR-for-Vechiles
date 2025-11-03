

# 🚗 Smart Auto QR

**Smart Auto QR** is a smart vehicle identification system built with **Python (Flask)** that generates unique, car-shaped **QR codes** for vehicles. Scanning the QR gives access to the vehicle’s public page — allowing visitors to view trip details, send messages, and request contact information from the owner securely.

---

## 🧠 Project Overview

This project solves a real-world problem — when a parked or moving vehicle needs to be contacted (e.g., blocking a path, misplaced items, ride inquiries) without exposing the owner’s personal details publicly.

Each vehicle is registered in the system, generating a **unique QR code** linked to that specific vehicle’s webpage. Users can scan it to communicate with the owner through a controlled, secure channel.

---

## ⚙️ Features

### 👤 For Vehicle Owners

* Register vehicle and automatically generate a **QR code**.
* Access a **personal dashboard** to:

  * View **messages** and **contact requests**.
  * **Approve or reject** requests before sharing contact details.
  * **Upload and view trip images**.

### 🚶‍♂️ For General Users

* Scan vehicle QR to open a **public vehicle page**.
* Send messages to the owner.
* Request the owner’s contact details (with owner approval).
* View public images or trip logs.

---

## 🏗️ Tech Stack

| Category                       | Technologies Used                   |
| ------------------------------ | ----------------------------------- |
| **Backend**                    | Python, Flask                       |
| **Database**                   | SQLite                              |
| **Frontend**                   | HTML, CSS, JavaScript               |
| **QR Generation**              | qrcode, PIL                         |
| **Image Handling**             | Flask-Uploads / Flask static folder |
| **Hosting (Planned/Deployed)** | Render / AWS EC2                    |
| **Version Control**            | Git & GitHub                        |

---

## 🧩 System Architecture

1. **Vehicle Registration** → Generates a unique QR code (car-shaped).
2. **QR Scan** → Redirects to public vehicle info page.
3. **Message / Contact Request** → Sent to database.
4. **Owner Dashboard** → Shows requests & messages with actions.
5. **Image Uploads** → Stored and displayed on both sides.

---

## 🚀 How to Run Locally

### Prerequisites

* Python 3.x
* pip (Python package manager)
* Git

### Steps

```bash
# Clone this repository
git clone https://github.com/<your-username>/Smart-Auto-QR.git

# Navigate into the folder
cd Smart-Auto-QR

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate  # on macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser and visit:
👉 `http://127.0.0.1:5000`

---

## 📸 Screenshots

* Vehicle registration form
* Owner dashboard view
* Message and contact request interface
* QR code preview

*(Add your own screenshots in a `/screenshots` folder and link them here)*

---

## 🔐 Security Features

* Owner approval system for contact sharing.
* Secure database storage for user messages.
* Unique QR link for every registered vehicle.

---

## 📦 Future Enhancements

* ✅ Deployment on Render / AWS EC2
* 📱 Android mobile app for scanning and managing requests
* 🗺️ Integration with Google Maps for trip display
* ☁️ Cloud database (PostgreSQL / DynamoDB)

---

## 💡 Use Cases

* Parking assistance (contact owner easily)
* Lost vehicle item return system
* Rideshare contact gateway
* Secure communication between unknown users

---

## 🧑‍💻 Author

**Dhanush**
📧 [[sangisetti.dhanush.work@gmail.com](sangisetti.dhanush.work@gmail.com)]
🔗 [(https://www.linkedin.com/in/Dhanush-Sangisetti/)](#) | [](#)


