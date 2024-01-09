#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
listint_t *reverse_list(listint_t **head);
/**
* is_palindrome - function that checks if a singly linked list is a palindrome
* @head: pointer to the head of the linked list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *slowtrav = *head;
listint_t *fasttrav = *head;
listint_t *prev_slowtrav = *head;
listint_t *first_half = *head;
listint_t *second_half = NULL;
if (*head == NULL && (*head)->next == NULL) 
return (1);
while (fasttrav != NULL && fasttrav->next != NULL) 
{
fasttrav = fasttrav->next->next;
prev_slowtrav = slowtrav;
slowtrav = slowtrav->next;
}
if (fasttrav != NULL) 
slowtrav = slowtrav->next;
prev_slowtrav->next = NULL; 
reverse_list(&slowtrav);
second_half = slowtrav;
while (first_half != NULL && second_half != NULL) 
{
if (first_half->n != second_half->n) 
return (0);
first_half = first_half->next;
second_half = second_half->next;
}
return (1);
}


/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;
while (current != NULL) 
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
return *head;
}

