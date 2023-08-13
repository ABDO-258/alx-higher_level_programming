#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
*is_palindrome - check if the lincked list is a palindrome
*
*@head:pointer to the head of the linked list
*
*Return: 1 if palindrome or 0 if not
*
*/
int is_palindrome(listint_t **head)
{
	listint_t *current, *temp = NULL;
	int len = 0, i = 0, j = 0, last = 0, palindrome = 0;

	current = (*head);
	while (current != NULL)
	{
		current = current->next;
		len++;
	}
	last = len;
	while (i < (len / 2))
	{
		current = (*head);
		while (j < last - 1)
		{
			current = current->next;
			j++;
		}
		add_nodeint_end(&temp, current->n);
		last--;
		j = 0;
		i++;
	}
	current = (*head);
	while (temp != NULL)
	{
		if (current->n != temp->n)
			palindrome++;
		temp = temp->next;
		current = current->next;
	}
	free_listint(temp);
	if (palindrome == 0)
		return (1);
	else
		return (0);
}
