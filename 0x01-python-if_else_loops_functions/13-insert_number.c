#include "lists.h"
/**
*insert_node - insert a number in sorted list
*
*@head:pointer to pointer to the head of the list
*@number:number to add to the list
*
*Return: address of the new element or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
		if (newnode == NULL)
			return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	current = *head;
	if (*head == NULL || number < current->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (current->next != NULL)
	{
		if (number > current->n && number < current->next->n)
		{
			newnode->next = current->next;
			current->next = newnode;
			break;
		}
		current = current->next;
	}
	if (current->next == NULL)
	{
		current->next = newnode;
	}
	return (newnode);
}

