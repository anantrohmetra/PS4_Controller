import pygame
from pythonosc.udp_client import SimpleUDPClient
import time

# Init OSC
osc = SimpleUDPClient("127.0.0.1", 6448)  # Wekinator default port

# Init pygame
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Using controller:", joystick.get_name())

try:
    while True:
        pygame.event.pump()  # Process event queue

        # Get raw joystick axes
        left_x = joystick.get_axis(0)  # Left stick X
        left_y = joystick.get_axis(1)  # Left stick Y
        right_x = joystick.get_axis(2) # Right stick X (may vary)
        right_y = joystick.get_axis(3) # Right stick Y (try 3 if this doesn’t work)

        # Normalize: convert from -1..1 to 0..1
        lx = (left_x + 1) / 2
        ly = (1 - left_y) / 2  # invert Y
        rx = (right_x + 1) / 2
        ry = (1 - right_y) / 2  # invert Y

        # Send to Wekinator
        osc.send_message("/wek/inputs", [lx, ly, rx, ry])
        print(f"Sent: LX={lx:.2f}, LY={ly:.2f}, RX={rx:.2f}, RY={ry:.2f}")

        time.sleep(0.03)

except KeyboardInterrupt:
    print("Stopped by user.")
    pygame.quit()
