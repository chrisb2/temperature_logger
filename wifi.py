"""WiFi configuration."""
import network
from utime import ticks_ms, ticks_diff, sleep
import secrets

WIFI_DELAY = 10
CHECK_INTERVAL = 0.1


def connect():
    """Connect to WiFi."""
    secs = WIFI_DELAY
    start = ticks_ms()

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSPHRASE)

    while secs >= 0 and not sta_if.isconnected():
        sleep(CHECK_INTERVAL)
        secs -= CHECK_INTERVAL

    if sta_if.isconnected():
        print('Connected WiFi')
        return True
    else:
        sta_if.active(False)
        return False


def disconnect():
    """Disconnect from WiFi."""
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        sta_if.disconnect()

    secs = WIFI_DELAY
    while secs >= 0 and sta_if.isconnected():
        sleep(CHECK_INTERVAL)
        secs -= CHECK_INTERVAL

    sta_if.active(False)
