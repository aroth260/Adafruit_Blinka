
# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""A Pin class for use with Rockchip RK3568."""

from adafruit_blinka.microcontroller.generic_linux.sysfs_pin import Pin

GPIO1_A0 = Pin(32)
GPIO1_A1 = Pin(33)
GPIO3_B7 = Pin(111)
GPIO3_C4 = Pin(116)
GPIO3_C5 = Pin(117)
GPIO0_C0 = Pin(16)
GPIO0_C1 = Pin(17)
GPIO4_C3 = Pin(147)
GPIO4_C5 = Pin(149)
GPIO4_C2 = Pin(146)
GPIO0_B6 = Pin(14)
GPIO2_D7 = Pin(95)
GPIO3_A0 = Pin(96)
GPIO3_C3 = Pin(115)
GPIO3_A4 = Pin(100)
GPIO3_C0 = Pin(112)
GPIO0_D1 = Pin(25)
GPIO0_D0 = Pin(24)
GPIO3_A3 = Pin(99)
GPIO3_A1 = Pin(97)
GPIO3_B2 = Pin(106)
GPIO4_C6 = Pin(150)
GPIO4_D1 = Pin(153)
GPIO0_B5 = Pin(13)
GPIO3_C2 = Pin(114)
GPIO3_A2 = Pin(98)
GPIO3_A6 = Pin(102)
GPIO3_A5 = Pin(101)
ADC_IN5 = 1

# I2C
I2C1_SDA = GPIO0_B6
I2C1_SCL = GPIO0_B5
I2C2_SDA = GPIO1_A0
I2C2_SCL = GPIO1_A1

SDA = I2C1_SDA
SCL = I2C1_SCL
# SPI
SPI1_CS = GPIO4_C6
SPI1_SCLK = GPIO3_A0
SPI1_MISO = GPIO4_C5
SPI1_MOSI = GPIO4_C3
SPI2_CS = GPIO4_D1
SPI2_SCLK = GPIO4_C2
#SPI2_MISO = GPIO2_B1
#SPI2_MOSI = GPIO2_B2

# UART
UART0_TX = GPIO0_C1
UART0_RX = GPIO0_C0
UART3_TX = GPIO3_B7
UART3_RX = GPIO3_C0
UART5_RX = GPIO3_C3
UART5_TX = GPIO3_C2
UART7_RX = GPIO3_C5
UART7_TX = GPIO3_C4
UART8_RX = GPIO3_A0
UART8_TX = GPIO2_D7
UART9_RX = GPIO4_C6
UART9_TX = GPIO4_C5
# PWM
PWM1 = GPIO0_C0
PWM2 = GPIO0_C1
PWM9 = GPIO3_B2
PWM12 = GPIO3_B7
PWM13 = GPIO3_C0
PWM14 = GPIO3_C4
PWM15 = GPIO3_C5

# ordered as i2cId, SCL, SDA
i2cPorts = (
    (0, I2C1_SCL, I2C1_SDA),
    (1, I2C2_SCL, I2C2_SDA),
    (7, I2C3_SCL, I2C3_SDA),
)

# ordered as spiId, sckId, mosiId, misoId
spiPorts = ((1, SPI1_SCLK, SPI1_MOSI, SPI1_MISO),)

# SysFS pwm outputs, pwm channel and pin in first tuple
pwmOuts = (
    ((1, 0), PWM1),
    ((2, 0), PWM2),
    ((9, 0), PWM9),
    ((12, 0), PWM12),
    ((13, 0), PWM13),
    ((14, 0), PWM14),
    ((15, 0), PWM15),
)

# SysFS analog inputs, Ordered as analog analogInId, device, and channel
analogIns = ((ADC_IN5, 0, 0),)
