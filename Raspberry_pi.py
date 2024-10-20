import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD

# Set up GPIO for button
GPIO.setmode(GPIO.BCM)
button_pin = 17  # GPIO pin connected to the button
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up resistor to handle button press

# Set up Camera
camera = PiCamera()

# Set up LCD
lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 11


lcd_columns = 16
lcd_rows = 2

lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

def capture_image():
    camera.start_preview()
    sleep(2)  # Allow the camera to stabilize
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
    lcd.clear()
    lcd.message('Done')
    print("Image captured!")

try:
    print("Press the button to capture an image...")
    lcd.message('Ready')
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:
            capture_image()
            sleep(0.5)  # Debounce delay to avoid multiple captures for a single press

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()
    camera.close()
    lcd.clear()


