
# Defines and protocol details from here: https://www.digis.ru/upload/iblock/f5a/VPL-VW320,%20VW520_ProtocolManual.pdf

ACTIONS = {
    "GET": 0x01,
    "SET": 0x00
}

COMMANDS = {
    "SET_POWER": 0x0130,
    "CALIBRATED_PRESET": 0x0002,
    "ASPECT_RATIO": 0x0020,
    "INPUT": 0x0001,
    "GET_STATUS_ERROR": 0x0101,
    "GET_STATUS_POWER": 0x0102,
    "GET_STATUS_LAMP_TIMER": 0x0113,
    "LAMP_CONTROL": 0x001A,
    "MOTIONFLOW": 0x0059,
    "COLOR_TEMPERATURE": 0x0017,
    "FILM_MODE": 0x001F,
    "REALITY_CREATION": 0x0067,
    "CONTRAST_ENHANCER": 0x001C,
    "COLOR_SPACE": 0x003B,
    "COLOR_CORRECTION": 0x0086,
    "GAMMA_CORRECTION": 0x0022,
}

INPUTS = {
    "HDMI_1": 0x002,
    "HDMI_2": 0x003,
}

ASPECT_RATIOS = {
    "NORMAL": 0x001,
    "V_STRETCH": 0x00B,
    "ZOOM_1_85": 0x00C,
    "ZOOM_2_35": 0x00D,
    "STRETCH": 0x00E,
    "SQUEEZE": 0x00F
}

POWER_STATUS = {
    "STANDBY": 0,
    "START_UP": 1,
    "START_UP_LAMP": 2,
    "POWER_ON": 3,
    "COOLING": 4,
    "COOLING2": 5
}

CALIBRATED_PRESETS = {
    "CINEMA_FILM_1": 0x000,
    "CINEMA_FILM_2": 0x001,
    "REF": 0x002,
    "TV": 0x003,
    "PHOTO": 0x004,
    "GAME": 0x005,
    "BRIGHT_CINE": 0x006,
    "BRIGHT_TV": 0x007,
    "USER": 0x008,
}

LAMP_CONTROLS = {
    "LOW": 0x0000,
    "HIGH": 0x0001,
}

MOTIONFLOW_OPTIONS = {
    "OFF": 0x0000,
    "SMOOTH_HIGH": 0x0001,
    "SMOOTH_LOW": 0x0002,
    "IMPULSE": 0x0003,
    "COMBINATION": 0x0004,
    "TRUE_CINEMA": 0x0005,
}

COLOR_TEMPERATURE_OPTIONS = {
    "D93": 0x0000,
    "D75": 0x0001,
    "D65": 0x0002,
    "CUSTOM_1": 0x0003,
    "CUSTOM_2": 0x0004,
    "CUSTOM_3": 0x0005,
    "CUSTOM_4": 0x0006,
    "CUSTOM_5": 0x0008,
    "D55": 0x0009,
}

FILM_MODE_OPTIONS = {
    "OFF": 0x0000,
    "AUTO": 0x0002,
}

REALITY_CREATION_OPTIONS = {
    "OFF": 0x0000,
    "ON": 0x0001,
}

CONTRAST_ENHANCER_OPTIONS = {
    "OFF": 0x0000,
    "LOW": 0x0001,
    "HIGH": 0x0002,
    "MIDDLE": 0x0003,
}

COLOR_SPACE_OPTIONS = {
    "BT709": 0x0000,
    "COLOR_SPACE_1": 0x0003,
    "COLOR_SPACE_2": 0x0004,
    "COLOR_SPACE_3": 0x0005,
    "CUSTOM": 0x0006,
    "BT2020": 0x0008,
}

COLOR_CORRECTION_OPTIONS = {
    "OFF": 0x0000,
    "ON": 0x0001,
}

GAMMA_CORRECTION_OPTIONS = {
    "OFF": 0x0000,
    "GAMMA_1_8": 0x0001,
    "GAMMA_2_0": 0x0002,
    "GAMMA_2_1": 0x0003,
    "GAMMA_2_2": 0x0004,
    "GAMMA_2_4": 0x0005,
    "GAMMA_2_6": 0x0006,
    "GAMMA_7": 0x0007,
    "GAMMA_8": 0x0008,
    "GAMMA_9": 0x0009,
    "GAMMA_10": 0x000A,

}
