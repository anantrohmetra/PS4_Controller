# 🎮 PS4 Controller to Wekinator (OSC Input)

URL: https://github.com/anantrohmetra/PS4_Controller/blob/main/gamecontroller2_Ps4.py 

This Python script uses a **PS4 controller** to send real-time X and Y values from both joysticks to **Wekinator** via **OSC** (Open Sound Control). It's useful for creative coding, interactive machine learning, and real-time control of generative audio/visual systems.

## 🧠 What It Does

- Reads input from both left and right joysticks using the `pygame` library.
- Normalizes the joystick values from `[-1, 1]` to `[0, 1]`.
- Sends 4 continuous control values via OSC:
  - `left_x`, `left_y`, `right_x`, `right_y`
- Compatible with **Wekinator**'s default OSC input port (`6448`).

---

## 📦 Requirements

Install dependencies using `pip`:

```bash
pip install pygame python-osc
