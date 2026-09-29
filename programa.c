#include <stdio.h>

int main() {
    int cookie;
    char buf[4];

    printf("buf: %p cookie: %p\n", (void*)&buf, (void*)&cookie);

    gets(buf);

    if (cookie == 0x45464748) {
        printf("\nGanaste!\n");
    } else {
        printf("\nPerdiste!\n");
    }
    return 0;
}
