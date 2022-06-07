#include <lists.h>
/**
 * reverse-reverse of the list
 * head:the start of the list
 * Return:pointer to the list
 */
listint_t reverse(listint_t **head)
{
	listint_t *temp, *mid;

	mid = head->next;
	temp = mid->next;

	while(mid != NULL)
	{
		mid->next = head;
		head = mid;
		mid = temp;
		temp = temp->next;
	}
	return head;
}
/**
 * is_palindrome-check if it is palindrome
 * head: the start of the list
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *rhead;

	rhead = (listint_t)malloc(sizeof(listint_t));
	rhead = reverse(rhead);

	while (rhead != NULL)
	{
		if (rhead != head)
			return 0;
		rhead = rhead->next;
		head = head->next;
	}
	return 1;


}
