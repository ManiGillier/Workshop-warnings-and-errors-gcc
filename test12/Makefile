##
## EPITECH PROJECT, 2024
## Test12
## File description:
## build
##

SRC	:=	\
		main.c	\
		a.c	\

CC	:=	gcc

OBJ	:=	$(SRC:.c=.o)

NAME	:=	a.out

CFLAGS :=	\
		-Wall	\
		-Wextra	\

CPPFLAGS :=	\

all: $(NAME)

%.o:	%.c
	$(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(CPPFLAGS) $^ -o $@

clean:
	rm -f $(OBJ)

fclean:
	rm -f $(NAME)

re: clean fclean all

.PHONY: all clean fclean re
