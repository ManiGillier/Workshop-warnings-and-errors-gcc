/*
** EPITECH PROJECT, 2024
** strlen
** File description:
** strlen
*/

int my_strlen(char *str)
{
    char *str_cpy = str;
    
    for (; *str; str++)
        continue;
    return str - str_cpy;
}
