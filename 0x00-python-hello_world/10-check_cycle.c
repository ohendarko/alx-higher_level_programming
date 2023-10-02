#include "lists.h"
/**
* check_cycle - check if there's a cycle
* @list: parameter
* Return: zero
*/
int check_cycle(listint_t *list)
{
	/*Checking if linked list has a cycle*/
	listint_t *snail = list;
	listint_t *rabbit = list;

	while (rabbit != NULL && rabbit->next != NULL)
	{
		snail = snail->next; /*move 1 step*/
		rabbit = rabbit->next->next; /*2 steps*/
		if (snail == rabbit) /*if 2 pointers meet...*/
			return (1); /*cycle detected*/
	}
	return (0); /*else no cycle detected*/
}
