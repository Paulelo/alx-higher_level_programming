#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - checks if a linked list is palindrome
* @head: is pointer to head node of list to be checked
* Return: 0 if palidrome and 1 if not
*/
int is_palindrome(listint_t **head)
{
	/*listint_t *ele = *head;*/
	listint_t *move = *head;
        int *my_arr = NULL;
	int i = 0;
	int j = 0;

	if ((move->next == NULL) || (head == NULL))
		return (1);
	while (move->next != NULL)
		my_arr[i] = move->n;
		move = move->next;
		/*ele = ele->n;*/
		i++;
	while (i)
		for (j = 0; j <= i; j++)
			if(my_arr[j] == my_arr[i])
				i--;
		return (1);
	return (0);
}
