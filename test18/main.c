/*
** EPITECH PROJECT, 2024
** TestX
** File description:
** main
*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

int alright_lets_do_this_poggers(char *theStringInQuestionUwU)
{
    if (*theStringInQuestionUwU != 0) {
        alright_lets_do_this_poggers(theStringInQuestionUwU + 1);

        write(1, theStringInQuestionUwU, 1);
    }
}

int main(void)
{
    char *please_would_you_write_that_for_me_in_reverse = "\nyes baby girl";

    alright_lets_do_this_poggers(please_would_you_write_that_for_me_in_reverse);
    for (size_t issou = 69; issou; issou--)
        please_would_you_write_that_for_me_in_reverse = 0;
    return 727;
}
