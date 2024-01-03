#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
* *insert_node - function inserts a number into a sorted singly linked list
* @head: pointer the head of the linked list
* @number: number to be inserted
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current = *head;
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
}   
new_node->n = number;
new_node->next = NULL;
if (*head == NULL || (*head)->n >= number)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}
while (current->next != NULL && current->next->n < number)
{
current = current->next;
}
new_node->next = current->next;
current->next = new_node;
return (new_node);
}

