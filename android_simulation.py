import subprocess
import time
import os
import platform

# Constants
ANDROID_EMULATOR_PATH = "C:/Program Files/BlueStacks_nxt/BlueStacks.exe"  # Update with your BlueStacks path
APK_PATH = "C:/path/to/sample.apk"  # Update with your APK path
EMULATOR_NAME = "Android_Emulator"  # Name of the emulator instance

def start_emulator():
    """Start the Android emulator."""
    print("Starting the Android emulator...")
    try:
        subprocess.Popen([ANDROID_EMULATOR_PATH])
        print("Emulator started. Waiting for it to be ready...")
        
        # Wait for the emulator to be ready
        while True:
            try:
                # Check if ADB can connect to the emulator
                subprocess.check_output(["adb", "get-state"])
                break  # If successful, exit the loop
            except subprocess.CalledProcessError:
                time.sleep(5)  # Wait and try again
        print("Emulator is ready.")
    except Exception as e:
        print(f"Failed to start emulator: {e}")

def install_apk():
    """Install the APK on the emulator."""
    print("Installing APK...")
    try:
        subprocess.run(["adb", "install", APK_PATH], check=True)
        print("APK installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install APK: {e}")

def get_system_info():
    """Retrieve and log system information."""
    print("Retrieving system information...")
    try:
        os_version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode().strip()
        device_model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode().strip()
        available_memory = subprocess.check_output(["adb", "shell", "cat", "/proc/meminfo | grep MemAvailable"]).decode().strip()

        print(f"OS Version: {os_version}")
        print(f"Device Model: {device_model}")
        print(f"Available Memory: {available_memory}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to retrieve system information: {e}")

def main():
    """Main function to run the tasks."""
    start_emulator()
    install_apk()
    get_system_info()

if __name__ == "__main__":
    main()