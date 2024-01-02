#include "lists.h"
/**
* check_cycle - function checks if a singly linked list has a cycle in it
* @list: list to be checked
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
listint_t *first, *second;
if (list == NULL || list->next == NULL)
return (0);
first = list;
second = list->next;
while (second != NULL && second->next != NULL)
{
if (first == second)
{
return (1);
}
first = first->next;
second = second->next->next;
}
return (0);
}

