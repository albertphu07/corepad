#include QMK_KEYBOARD_H


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

[0] = LAYOUT(
    KC_A,
    KC_B,
    KC_C
)

};


#ifdef OLED_ENABLE

bool oled_task_user(void) {

    oled_write_P(
        PSTR("NodeX V1\n"),
        false
    );

    oled_write_P(
        PSTR("Ready"),
        false
    );

    return false;
}

#endif
