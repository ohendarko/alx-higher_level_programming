#include "lists.h"
/**
* revList - reverse list
* @head: head
* Return: return
*/
listint_t *revList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
* is_palindrome - function name
* @head: parameter
* Return: whatever
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow = revList(slow); /*Reverse*/

	while (slow != NULL)
	{
		if ((*head)->n != slow->n)
			return (0);
		*head = (*head)->next;
		slow = slow->next;
	}
	return (1);
}
