/*
** EPITECH PROJECT, 2024
** Test9
** File description:
** main
*/

#include <stdio.h>

int my_strlen(char *str)
{
    for (int i = 0;; i++)
        if (str[i] == '\0')
            break;
    return i;
}

int main (void)
{
    char *str = "this is a string";

    printf("string size : %d\n", my_strlen(str));
    return 0;
}
