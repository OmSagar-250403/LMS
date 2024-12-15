import requests
import json
import platform

def get_device_info():
    """Retrieve mock device information."""
    device_info = {
        "device_id": "12345-ABCDE",  # Mock device ID
        "os_version": platform.version(),  # OS version
        "device_model": platform.system(),  # Device model (e.g., Windows, Linux)
        "available_memory": "2048 MB"  # Mock available memory
    }
    return device_info

def add_app_to_server(app_data):
    """Send app data to the Django backend server."""
    url = "http://localhost:8000/add-app/"  # Updated to match your Django API endpoint
    try:
        response = requests.post(url, json=app_data)
        response.raise_for_status()  # Raise an error for bad responses
        print("App added successfully.")
        print("Server response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to server: {e}")

def main():
    """Main function to run the tasks."""
    device_info = get_device_info()
    print("Device Information:", json.dumps(device_info, indent=4))

    # Prepare mock app data to send to the server
    app_data = {
        "app_name": "Mock App",
        "version": "1.0.0",
        "description": "This is a mock application for testing."
    }
    
    add_app_to_server(app_data)

if __name__ == "__main__":
    main()