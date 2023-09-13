import serial

# Define command and response constants
COMMANDS = {
    "CHECK": 0x00,
    "GET_INPUT": 0x01,
    "PULSE": 0x02,
    "SET_DAC": 0x03,
    "DUMMY_COMMAND": 0xFF,  # Added for testing UNKNOWN_COMMAND response
}

RESPONSES = {
    0x00: "FAIL",
    0x01: "OK",
    0x03: "UNKNOWN_COMMAND",
}

# Configure the serial port settings
ser = serial.Serial('COM3', baudrate=38400, timeout=1)  # Change 'COM1' to your device's serial port

def send_command(command):
    try:
        # Open the serial connection
        if not ser.isOpen():
            ser.open()

        if command == COMMANDS["SET_DAC"]:
            # Prompt the user for a 12-bit integer value
            while True:
                try:
                    dac_value = int(input("Enter a 12-bit integer value for DAC (0-4095): "))
                    if 0 <= dac_value <= 4095:
                        break
                    else:
                        print("Invalid value. Please enter a value in the range 0-4095.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            # Send the SET_DAC command and value
            ser.write(bytes([command]))
            ser.write(dac_value.to_bytes(2, byteorder='little'))
            print(f"Sent command: {command} with value: {dac_value}\n")
        else:
            # Send the hex command to the serial device
            ser.write(bytes([command]))
            print(f"Sent command: {command}")

        # Read and print the response from the serial device
        response = ser.read(1)
        if response:
            response_code = int.from_bytes(response, byteorder='big')
            print(f"Received response: {RESPONSES.get(response_code, 'UNKNOWN')}\n")

    except KeyboardInterrupt:
        print("Program terminated by user.")

    finally:
        # Close the serial connection
        if ser.isOpen():
            ser.close()

if __name__ == "__main__":
    print("Serial Console Application")
    print("Available commands:")
    for cmd, hex_val in COMMANDS.items():
        print(f"{cmd}: 0x{hex_val:02X}")

    while True:
        user_input = input("Enter a command (or 'exit' to quit): ").strip().upper()
        
        if user_input == 'EXIT':
            break

        if user_input in COMMANDS:
            send_command(COMMANDS[user_input])
        else:
            print("Invalid command. Please enter a valid command.")
