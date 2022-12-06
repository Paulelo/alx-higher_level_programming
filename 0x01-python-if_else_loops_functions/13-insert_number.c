#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* insert_node - inserts new node in a sorted linked list
* @head: is pointer to next node
* @number: is value in node
* Return: on success adress of new node or NULL on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}


