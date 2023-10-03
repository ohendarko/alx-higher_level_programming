#include "lists.h"
/**
* insert_node : function name
* @head: parameter
* @number: another one
* Return: anything
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));
	
	if (newNode == NULL)
		exit(EXIT_FAILURE);
	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	while (current->next != NULL && current->next->n < number)
		current = current->next;
	newNode->next = current->next;
	current->next = newNode;

	return (newNode);
}
