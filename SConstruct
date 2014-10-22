# -*- coding: utf-8 -*-
# vim: set filetype=python : #
from subprocess import call


def run_tests(target, source, env):
    for src_f in source:
        call(src_f.abspath)
    return None

# Build env
SRCBUILDDIR = 'build_src'
TESTBUILDDIR = 'build_test'
BINDIR = 'bin'

# Mount directories
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

obj_unity = env.Object('build_src/unity.o', 'unity.c')
obj_src = SConscript('src/SConscriptHOST', variant_dir=SRCBUILDDIR, duplicate=0,
                     exports='env')
test_runners = SConscript('test/SConscript', variant_dir=TESTBUILDDIR,
                          duplicate=0, exports=['env', 'obj_src', 'obj_unity'])
env.AlwaysBuild(env.Alias('test', test_runners, run_tests))
