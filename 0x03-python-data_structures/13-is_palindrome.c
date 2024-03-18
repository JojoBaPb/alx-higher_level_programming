#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to first node in the list
 * Return: pointer to first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: double pointer to linked list
 * Return: 1 if it is, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *up = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{

			up = slow->next;
			break;
		}
		if (!fast->next)
		{
			up = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&up);

	while (up && temp)
	{
		if (temp->n == up->n)
		{
			up = up->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!up)
		return (1);

	return (0);
}
