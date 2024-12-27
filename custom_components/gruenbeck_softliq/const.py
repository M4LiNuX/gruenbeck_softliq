DOMAIN = "gruenbeck_softliq"
DEFAULT_URL = "http://192.168.1.36/mux_http/"
DEFAULT_CODE = 142

# Sensor-Parameter mit spezifischen Eigenschaften
PARAMS = {
    "D_A_1_7": {
        "name": "Gesamtdurchfluss",
        "device_class": "volume_flow_rate",
        "unit_of_measurement": "m³/h",
        "state_class": "measurement",
        "suggested_display_precision": 3,
        "suggested_unit_of_measurement": "m³/h",
    },
    "D_A_2_3": {
        "name": "Salzreichweite",
        "device_class": "duration",
        "unit_of_measurement": "Tage",
        "state_class": "measurement",
        "suggested_display_precision": 0,
        "suggested_unit_of_measurement": "Tage",
    },
    "D_A_1_6": {
        "name": "Weichwasserhärte",
        "device_class": "none",
        "unit_of_measurement": "°dH",
        "state_class": "measurement",
        "suggested_display_precision": 1,
        "suggested_unit_of_measurement": "°dH",
    },
    "D_K_1": {
        "name": "Anzahl Regenerationen",
        "device_class": "none",
        "unit_of_measurement": "Zyklen",
        "state_class": "total_increasing",
        "suggested_display_precision": 0,
    },
    "D_K_2": {
        "name": "Weichwassermenge",
        "device_class": "volume",
        "unit_of_measurement": "m³",
        "state_class": "total_increasing",
        "suggested_display_precision": 2,
        "suggested_unit_of_measurement": "m³",
    },
    "D_A_2_2": {
        "name": "Tage bis Wartung",
        "device_class": "duration",
        "unit_of_measurement": "Tage",
        "state_class": "measurement",
        "suggested_display_precision": 0,
        "suggested_unit_of_measurement": "Tage",
    },
    "D_Y_1": {
        "name": "Wasserverbrauch gestern",
        "device_class": "volume",
        "unit_of_measurement": "l",
        "state_class": "measurement",
        "suggested_display_precision": 0,
        "suggested_unit_of_measurement": "l",
    },
    "D_Y_3": {
        "name": "Salzverbrauch",
        "device_class": "none",
        "unit_of_measurement": "kg/Jahr",
        "state_class": "measurement",
        "suggested_display_precision": 2,
        "suggested_unit_of_measurement": "kg/Jahr",
    },
    "D_Y_10_1": {
        "name": "Restkapazität Austauscher 1",
        "device_class": "none",
        "unit_of_measurement": "%",
        "state_class": "measurement",
        "suggested_display_precision": 0,
    },
    "D_Y_10_2": {
        "name": "Restkapazität Austauscher 2",
        "device_class": "none",
        "unit_of_measurement": "%",
        "state_class": "measurement",
        "suggested_display_precision": 0,
    },
}
