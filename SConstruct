# -*- coding: utf-8 -*-
# vim: set filetype=python : #
from subprocess import call
from config import *


def run_tests(target, source, env):
    for src_f in source:
        call(src_f.abspath)
    return None


env_target = Environment()
Repository([CORE_SRC, VARIANT_SRC])
env_target.Append(
    ARMODEL="Arduino Due",
    BOSSAC=BOSSAC,
    BOSSACFLAGS=FLAGS_BOSSAC,
    ARDUINOPORT=ARDUINO_PORT,
    MAIN_FILE='build_src/Blink',
    COREDIR='lib',
)
env_target.Replace(
    AR=AR,
    OBJCOPY=OBJ_COPY,
    ARFLAGS='rcs',
    LIBPREFIX='',
    CC=CC,
    CXX=CXX,
    CCFLAGS=FLAGS_CC,
    CXXFLAGS=FLAGS_CXX,
    CPPPATH=incs,
    FLASHDIR=FLASH,
    GCCRELDIR=GCC_REL,
    ELFFLAGS=FLAGS_LINK,
    OBJCOPYFLAGS=FLAGS_OBJ_COPY,
)
# Mount code directories
Repository(['#./vendor/ceedling/vendor/unity/src'])

CCCOM = '$CC -c $_CCCOMCOM $SOURCE -o $TARGET '
CPPPATH = ['#./vendor/ceedling/vendor/unity/src', '#./include']
UNITYHELPDIR = '#./vendor/ceedling/vendor/unity/auto'

env = Environment()
env.Append(
    UNITYHELPDIR=UNITYHELPDIR,
)

env.Replace(
    CCCOM=CCCOM,
    CPPPATH=CPPPATH,
)

core_variant_syscalls = SConscript('lib/SConscript', duplicate=0,
                                   exports='env_target')
bin_main = SConscript('src/SConscriptTARGET', duplicate=0,
                      variant_dir='build_src', exports=[
                          'env_target', 'core_variant_syscalls', 'MAIN_FILE'])

env_target.AlwaysBuild(env_target.Alias('compile', bin_main))
bossacrule = '$BOSSAC $BOSSACFLAGS $SOURCE -R'
stty_refresh = env_target.AlwaysBuild(env_target.Alias(
    'stty_refresh',[] ,'stty -F /dev/$ARDUINOPORT cs8 1200 hupcl'))
env_target.AlwaysBuild(env_target.Alias('upload', [bin_main, stty_refresh], bossacrule))

# obj_unity = env.Object('build_src/unity.o', 'unity.c')
# obj_src = SConscript('src/SConscriptHOST', variant_dir=SRCBUILDDIR, duplicate=0,
                     # exports='env')
# test_runners = SConscript('test/SConscript', variant_dir=TESTBUILDDIR,
                          # duplicate=0, exports=['env', 'obj_src', 'obj_unity'])
# env.AlwaysBuild(env.Alias('test', test_runners, run_tests))
