/*
** EPITECH PROJECT, 2024
** TestX
** File description:
** main
*/

#include <stdio.h>
#include <stdlib.h>

// just make it so the str is getting free'd and fix all the warnings

static void *wait_destroy_that_string_for_me_im_begging(char **theStringAdress)
{
    free(theStringAdress + 1);
    printf("I free'd for you baby boy\n");
    return (void *) 69;
}

static char define_tmp(char *theStringLmao, int theFunnyNumber)
{
    for (int i = 0; i < theFunnyNumber - 1; i++)
        theStringLmao[i] = theFunnyNumber;
    theStringLmao[theFunnyNumber] = 0;
    return "hi";
}

int main(void)
{
    char *tmp = malloc(sizeof(char) * 69); // lmao funny number

    tmp += 2;
    define_tmp(tmp, 69);
    wait_destroy_that_string_for_me_im_begging(tmp);
    return 0;
}
