# include <stdio.h>
#include <unistd.h>
int main(int argc, char **argv)
{
    printf("argv[1] => %s \n", argv[1]);
    if (argc < 2 || !argv || !argv[0] || !argv[1])
    {
        printf("A7A\n");
        return (-1);

    }
    char *em = argv[1];
    printf("%s \n", em);
    for (int i = 0;  em[i] != '\0'; i++)
        printf("[%c : %i]", em[i], em[i]);
    putchar(10);
    return (0);
}