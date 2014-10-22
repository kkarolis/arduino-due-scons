# -*- coding: utf-8 -*-
# Main configuration file for building the project
main_file = 'Blink.cpp'
port = 'ttyACM0'
ar_dir = '/home/karolis/programs/arduino-1.5.8/hardware/'


# Should not be modified currently
env = Environment()
variant_src_dir = os.path.join(ar_dir, 'arduino/sam/variants/arduino_due_x')
core_src_dir = os.path.join(ar_dir, 'arduino/sam/cores/arduino')
tool_dir = os.path.join(ar_dir, 'tools/gcc-arm-none-eabi-4.8.3-2014q1/bin')
flash_dir = os.path.join(
    ar_dir, 'arduino/sam/variants/arduino_due_x/linker_scripts/gcc/flash.ld')
gcc_rel = os.path.join(
    ar_dir, 'arduino/sam/variants/arduino_due_x/libsam_sam3x8e_gcc_rel.a')

env.Repository([core_src_dir, variant_src_dir])


inc_dir = os.path.join(ar_dir, 'arduino/sam')
lib_sam = os.path.join(inc_dir, 'system/libsam')
lib_cmsis = os.path.join(inc_dir, 'system/CMSIS/CMSIS/Include')
lib_atmel = os.path.join(inc_dir, 'system/CMSIS/Device/ATMEL')
lib_arduino = os.path.join(inc_dir, 'cores/arduino')
lib_arduino_due = os.path.join(inc_dir, 'variants/arduino_due_x')
incs = [lib_sam, lib_cmsis, lib_atmel, lib_arduino, lib_arduino_due]


cc = os.path.join(tool_dir, 'arm-none-eabi-gcc')
cxx = os.path.join(tool_dir, 'arm-none-eabi-g++')
ar = os.path.join(tool_dir, 'arm-none-eabi-ar')
objcopy = os.path.join(tool_dir, 'arm-none-eabi-objcopy')
bossac = os.path.join(ar_dir, 'tools/bossac')




ccflags = [
    '-g', '-Os', '-w', '-ffunction-sections', '-fdata-sections', '-nostdlib',
    '--param', 'max-inline-insns-single=500', '-Dprintf=iprintf',
    '-mcpu=cortex-m3', '-DF_CPU=84000000L', '-DARDUINO=158',
    '-DARDUINO_SAM_DUE', '-DARDUINO_ARCH_SAM', '-D__SAM3X8E__', '-mthumb',
    '-DUSB_VID=0x2341', '-DUSB_PID=0x003e', '-DUSBCON',
    '-DUSB_MANUFACTURER="Unknown"', '-DUSB_PRODUCT=\"$ARMODEL\"']
cxxflags = ['-fno-threadsafe-statics', '-fno-rtti', '-fno-exceptions']
elfflags = ['-Os', '-Wl,--gc-sections', '-mcpu=cortex-m3',
            '-T$FLASHDIR', '-Wl,-Map,${SOURCE}.map', '-o',
            '$TARGET', '-L$COREDIR', '-mthumb', '-Wl,--cref',
            '-Wl,--check-sections', '-Wl,--gc-sections',
            '-Wl,--entry=Reset_Handler',
            '-Wl,--unresolved-symbols=report-all', '-Wl,--warn-common',
            '-Wl,--warn-section-align', '-Wl,--warn-unresolved-symbols',
            '-Wl,--start-group', '$COREDIR/syscalls_sam3.o',
            '${SOURCE}', '$COREDIR/variant.o', '$GCCRELDIR',
            '$COREDIR/core.a', '-Wl,--end-group', '-lm', '-gcc']
bossac_flags = ['-i', '--port=$ARDUINOPORT', '-U', 'false', '-e', '-w', '-v', '-b']
objcopyflags = ['-O', 'binary']
env.Append(
    ARMODEL="Arduino Due",
    BOSSAC=bossac,
    BOSSACFLAGS=bossac_flags,
    ARDUINOPORT=port,
)
env.Replace(
    AR=ar,
    OBJCOPY=objcopy,
    ARFLAGS='rcs',
    LIBPREFIX='',
    CC=cc,
    CXX=cxx,
    CCFLAGS=ccflags,
    CXXFLAGS=cxxflags,
    CPPPATH=incs,
    FLASHDIR=flash_dir,
    GCCRELDIR=gcc_rel,
    COREDIR=core_dir,
    ELFFLAGS=elfflags,
    OBJCOPYFLAGS=objcopyflags,
)

