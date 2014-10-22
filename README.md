arduino-due-scons
=================
Integration of SCons build system for arduino-due
* automatic test building/running TDD (using Ceedling test framework)
* automatic uploading to the board itself


Requirements
============
* Python2 + SCons
* ruby (test generation)


Current Goals
=============
Make a blink LED example with TDD + upload to board


Usage
=====

    scons -c
    scons test
    scons compile
    scons upload
