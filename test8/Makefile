##
## EPITECH PROJECT, 2024
## Test8
## File description:
## build
##

SRC	:=	\
		main.c	\

CC	:=	gcc

OBJ	:=	$(SRC:.c=.o)

NAME	:=	a.out

CFLAGS :=	\

CPPFLAGS :=	\

all: $(NAME)

%.o:	%.c
	$(CC) -c $(CFLAGS) $(CPPFLAGS) $(LIBFLAGS) $< -o $@

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(CPPFLAGS) $(LIBFLAGS) $^ -o $@

clean:
	rm -f $(OBJ)

fclean:
	rm -f $(NAME)

re: clean fclean all

.PHONY: all clean fclean re
