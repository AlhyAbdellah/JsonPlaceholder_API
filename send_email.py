import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = os.environ.get("EMAIL_ADDRESS")
PASSWORD = os.environ.get("APP_PASSWORD")
RECEIVER = "abdellah.alhyan98@gmail.com"  # ou une autre adresse

# Email setup
msg = MIMEMultipart("alternative")
msg["Subject"] = "🧪 Rapport Test API JSONPlaceholder"
msg["From"] = SENDER
msg["To"] = RECEIVER

# Charger le rapport HTML
with open("report_api.html", "r", encoding="utf-8") as f:
    html = f.read()

part_html = MIMEText(html, "html")
msg.attach(part_html)

# Envoyer via SMTP Gmail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(SENDER, PASSWORD)
    server.sendmail(SENDER, RECEIVER, msg.as_string())

print("✅ Email envoyé avec succès.")

