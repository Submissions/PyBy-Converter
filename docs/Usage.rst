=====================
PyBy Converter Usage
=====================

Command Line
============

The converter will read bytes from the command line and produce the byte conversions
::
    ./converter.py 222222222222222

    This is the result for 222222222222222 bytes
    MB 211927625.86805534
    GB 206960.5721367728
    TB 202.10993372731718

Multiple bytes can be listed at a time
::
    ./converter.py 333333 7777777

    This is the result for 333333 bytes
    MB 0.31789112091064453
    GB 0.0003104405477643013
    TB 3.031645974260755e-07
    This is the result for 7777777 bytes
    MB 7.417466163635254
    GB 0.007243619300425053
    TB 7.0738469730713405e-06
