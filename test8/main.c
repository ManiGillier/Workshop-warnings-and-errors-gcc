/*
** EPITECH PROJECT, 2024
** Test8
** File description:
** main
*/

int main(void)
{
    int fd = open("test", O_CREAT);
    close(fd);
    puts("Helloooo");
    return 0;
}
