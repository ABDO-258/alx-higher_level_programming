#include "lists.h"
#include <stdio.h>
/**
 * check_cycle -  check if the list had  a cycle
 * @list: pointer to list to be freed
 * Return: 1 if there is a cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2 = NULL;

	ptr1 = list;
	if (list != NULL)
	{
		ptr2 = list->next;
		while (ptr1 != NULL && ptr2 != NULL)
		{
			if (ptr1 == ptr2)
				return (1);
			ptr1 = ptr1->next;
			ptr2 = ptr2->next->next;
		}
	}
	return (0);

}
