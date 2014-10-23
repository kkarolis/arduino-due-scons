# -*- coding: utf-8 -*-
# Main configuration file for building the project
import os

MAIN_FILE = 'Blink.cpp'
ARDUINO_PORT = 'ttyACM0'
AR_DIR = '/home/karolis/programs/arduino-1.5.8/hardware/'

# Build env
SRC_BUILD_DIR = 'build_src'
TEST_BUILD_DIR = 'build_test'

# Should not be modified currently
VARIANT_SRC = os.path.join(AR_DIR, 'arduino/sam/variants/arduino_due_x')
CORE_SRC = os.path.join(AR_DIR, 'arduino/sam/cores/arduino')
TOOLS = os.path.join(AR_DIR, 'tools/gcc-arm-none-eabi-4.8.3-2014q1/bin')
FLASH = os.path.join(
    AR_DIR, 'arduino/sam/variants/arduino_due_x/linker_scripts/gcc/flash.ld')
GCC_REL = os.path.join(
    AR_DIR, 'arduino/sam/variants/arduino_due_x/libsam_sam3x8e_gcc_rel.a')
# Mount core repositories


INC_DIR = os.path.join(AR_DIR, 'arduino/sam')
LIB_SAM = os.path.join(INC_DIR, 'system/libsam')
LIB_CMSIS = os.path.join(INC_DIR, 'system/CMSIS/CMSIS/Include')
LIB_ATMEL = os.path.join(INC_DIR, 'system/CMSIS/Device/ATMEL')
LIB_ARDUINO = os.path.join(INC_DIR, 'cores/arduino')
LIB_ARDUINO_DUE = os.path.join(INC_DIR, 'variants/arduino_due_x')
incs = [LIB_SAM, LIB_CMSIS, LIB_ATMEL, LIB_ARDUINO, LIB_ARDUINO_DUE]


CC = os.path.join(TOOLS, 'arm-none-eabi-gcc')
CXX = os.path.join(TOOLS, 'arm-none-eabi-g++')
AR = os.path.join(TOOLS, 'arm-none-eabi-ar')
OBJ_COPY = os.path.join(TOOLS, 'arm-none-eabi-objcopy')
BOSSAC = os.path.join(AR_DIR, 'tools/bossac')




FLAGS_CC = [
    '-g', '-Os', '-w', '-ffunction-sections', '-fdata-sections', '-nostdlib',
    '--param', 'max-inline-insns-single=500', '-Dprintf=iprintf',
    '-mcpu=cortex-m3', '-DF_CPU=84000000L', '-DARDUINO=158',
    '-DARDUINO_SAM_DUE', '-DARDUINO_ARCH_SAM', '-D__SAM3X8E__', '-mthumb',
    '-DUSB_VID=0x2341', '-DUSB_PID=0x003e', '-DUSBCON',
    '-DUSB_MANUFACTURER="Unknown"', '-DUSB_PRODUCT=\"$ARMODEL\"']
FLAGS_CXX = ['-fno-threadsafe-statics', '-fno-rtti', '-fno-exceptions']
FLAGS_LINK = [
    '-Os', '-Wl,--gc-sections', '-mcpu=cortex-m3', '-T$FLASHDIR', '-lm',
    '-gcc', '-L$COREDIR', '-mthumb', '-Wl,--cref', '-Wl,--check-sections',
    '-Wl,--gc-sections', '-Wl,--entry=Reset_Handler',
    '-Wl,--unresolved-symbols=report-all', '-Wl,--warn-common',
    '-Wl,--warn-section-align', '-Wl,--warn-unresolved-symbols']

FLAGS_BOSSAC = [
    '-i', '--port=$ARDUINOPORT', '-U', 'false', '-e', '-w', '-v', '-b']
FLAGS_OBJ_COPY = ['-O', 'binary']
