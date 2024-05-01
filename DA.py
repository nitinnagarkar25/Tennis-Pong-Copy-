import serial
import subprocess
import time

# Open serial connection to Arduino
ser = serial.Serial('/dev/cu.usbmodem1101', 9600)  # Replace 'COM3' with the appropriate port name
print("Serial connection established")

def open_image_with_size(image_path, width, height):
    subprocess.Popen(['open', '-W', str(width), '-H', str(height), image_path])

while True:
    # Read serial data from Arduino
    data = ser.readline().decode().strip()
    print("Received command:", data)
    
    # Check if command is to play audio
    if data == "Detected":
        # Use subprocess to play audio file
        audio_file_path = "China.wav"  # Sound path
        image_file_path = "China.jpeg" # image path
        subprocess.Popen(['open', audio_file_path])
        subprocess.Popen(['open', image_file_path])
        #open_image_with_size(image_file_path, 1500,1000)
        

    if data == "Detected2":
        # Use subprocess to play audio file
        audio_file_path2 = "India.wav"  # Sound path
        image_file_path2 = "India.jpeg" # image path
        subprocess.Popen(['open', audio_file_path2])
        subprocess.Popen(['open', image_file_path2])
    

    if data == "Detected3":
    # Use subprocess to play audio file
        audio_file_path3 = "US.wav"  # Sound path
        image_file_path3 = "US.jpeg" # image path
        subprocess.Popen(['open', audio_file_path3])
        subprocess.Popen(['open', image_file_path3])
    

    if data == "Detected4":
        # Use subprocess to play audio file
        audio_file_path4 = "Korea.wav"  # Sound path
        image_file_path4 = "Korea.jpeg" # image path
        subprocess.Popen(['open', audio_file_path4])
        subprocess.Popen(['open', image_file_path4])
    

    if data == "Detected5":
        # Use subprocess to play audio file
        audio_file_path5 = "Colombia.wav"  # Sound path
        image_file_path5 = "Colombia.jpeg" # image path
        subprocess.Popen(['open', audio_file_path5])
        subprocess.Popen(['open', image_file_path5])
    

    if data == "Detected6":
        # Use subprocess to play audio file
        audio_file_path6 = "Russia1.wav"  # Sound path
        image_file_path6 = "Russia.jpeg" # image path
        subprocess.Popen(['open', audio_file_path6])
        subprocess.Popen(['open', image_file_path6])
    

    if data == "Detected7":
        # Use subprocess to play audio file
        audio_file_path7 = "Russia2.wav"  # Sound path
        image_file_path7 = "Russia.jpeg" # image path
        subprocess.Popen(['open', audio_file_path7])
        subprocess.Popen(['open', image_file_path7])
    

    if data == "Detected8":
        # Use subprocess to play audio file
        audio_file_path8 = "Brazil.wav"  # Sound path
        image_file_path8 = "Brazil.jpeg" # image path
        subprocess.Popen(['open', audio_file_path8])
        subprocess.Popen(['open', image_file_path8])
        time.sleep(1)

    if data == "Detected9":
        # Use subprocess to play audio file
        audio_file_path9 = "Morocco.wav"  # Sound path
        image_file_path9 = "Morocco.jpeg" # image path
        subprocess.Popen(['open', audio_file_path9])
        subprocess.Popen(['open', image_file_path9])
   
    



        

