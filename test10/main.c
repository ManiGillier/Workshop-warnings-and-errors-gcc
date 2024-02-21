/*
** EPITECH PROJECT, 2024
** Test10
** File description:
** main
*/

int my_putstr(char *str)
{
    if (!str || *!str)
        return -1;
    write(1, str, 1);
    my_putstr(str + 1);
    return 0;
}

int main (void)
{
    char str[6] = "salut";
    
    my_putstr(str);
    return 0;
}
