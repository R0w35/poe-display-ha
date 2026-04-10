import time
import socket
import subprocess
import os
import json
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=32)

try:
    font = ImageFont.truetype("FreeSans.ttf", 16)
except:
    font = ImageFont.load_default()

def get_ip():
    try:
        import urllib.request, json
        req = urllib.request.Request(
            "http://supervisor/network/info",
            headers={"Authorization": "Bearer " + os.environ.get("SUPERVISOR_TOKEN", "")}
        )
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            for interface in data["data"]["interfaces"]:
                if interface["ipv4"]["address"]:
                    return interface["ipv4"]["address"][0].split("/")[0]
    except Exception as e:
        print(f"DEBUG: IP Fetch failed: {e}") # This will show up in your HA Logs
        return "No IP"

def get_temp():
    try:
        result = subprocess.run(
            ["cat", "/sys/class/thermal/thermal_zone0/temp"],
            capture_output=True, text=True
        )
        temp = int(result.stdout.strip()) / 1000
        return f"{temp:.1f}C"
    except:
        return "N/A"

while True:
    with canvas(device) as draw:
        draw.text((0, 0),  f"IP:   {get_ip()}",   fill="white")
        draw.text((0, 18), f"Temp: {get_temp()}", fill="white")
    time.sleep(5)
