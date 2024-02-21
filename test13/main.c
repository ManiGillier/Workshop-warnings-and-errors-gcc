/*
** EPITECH PROJECT, 2024
** Test13
** File description:
** main
*/

#include <stdio.h>

int return_main(void)
{
    return 2;
}

int main(void)
{
    int return_value =  return_main;

    printf("%d\n", return_value);
    return return_value;
}
