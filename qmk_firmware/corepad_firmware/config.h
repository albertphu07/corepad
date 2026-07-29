#pragma once

#define MATRIX_ROWS 1
#define MATRIX_COLS 3

//Switch Pins
#define DIRECT_PINS { \
{ GP26, GP27, GP28 } \
}


// Direct Connect to GND
#define DIRECT_PINS_PULLUP

#define DEBOUNCE 5

// OLED I2C
#define I2C_DRIVER I2CD1

#define I2C1_SDA_PIN GP6
#define I2C1_SCL_PIN GP7


// Vial security ID
#define VIAL_KEYBOARD_UID {0x12,0x34,0x56,0x78,0x9A,0xBC,0xDE,0xF0}


#define MANUFACTURER "CorePad Technologies INC"
#define PRODUCT "CorePad V1"
