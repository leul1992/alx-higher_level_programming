#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *n_list, *nn_list;

	if (list == NULL)
		return (0);
	n_list = list;
	nn_list = list;

	while (nn_list->next && nn_list->next->next)
	{
		n_list = n_list->next;
		nn_list = nn_list->next->next;

		if (n_list == nn_list)
			return (1);
	}

	return (0);
}
