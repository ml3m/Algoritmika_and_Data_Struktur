#include <stdio.h>
#include <stdlib.h>

struct Node {
	int data;
	struct Node* next, *prev;
};

struct LinkedList {
	struct Node* head;
	int size;
};

struct Node* createNode(int data) {
	/*
		Creates a new node with the provided data.
	*/

	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = data;
	newNode->next = NULL;
	newNode->prev = NULL;

	return newNode;
}

void push (struct LinkedList** ll, int data) {
	/*
		Pushes a new node behind the linked list's head node.
	*/

	struct Node* newNode = createNode(data);

	if ((*ll)->head == NULL) {
		(*ll)->head = newNode;
	} else {
		newNode->next = (*ll)->head;
		(*ll)->head->prev = newNode;
		(*ll)->head = newNode;
	}

	(*ll)->size += 1;
}

void append (struct LinkedList** ll, int data) {
	/*
		Append a new node to the end of the linked list
	*/

	struct Node* newNode = createNode(data);
	
	if ((*ll)->head == NULL) {
		(*ll)->head = newNode;
	} else {
		struct Node* currentNode = (*ll)->head;

		while (currentNode->next != NULL) {
			currentNode = currentNode->next;
		}

		currentNode->next = newNode;
		newNode->prev = currentNode;
	}

	(*ll)->size += 1;
}

int getValueAt(struct LinkedList** ll, int index) {
	/*
		Returns the value of a node at the given index.
		If node does not exist, program will exit.
	*/

	if (index >= (*ll)->size || index < 0) {
		printf("Index %d does not exist in size %d linked list! Exiting...\n", index, (*ll)->size);
		exit(-1);
	}

	struct Node* currentNode = (*ll)->head;
	while (index != 0) {
		currentNode = currentNode->next;
		index -= 1;
	}

	return currentNode->data;
}

int removeNodeAt(struct LinkedList** ll, int index) {
	/*
		Removes a node at the provided index.
		If node does not exist, program will exit.
	*/

	if (index >= (*ll)->size || index < 0) {
		printf("Index %d does not exist in size %d linked list! Exiting...\n", index, (*ll)->size);
		exit(-1);
	}

	struct Node* currentNode = (*ll)->head;
	int removedData = 0;

	while (index != 0) {
		currentNode = currentNode->next;
		index -= 1;
	}
	removedData = currentNode->data;

	if (currentNode->prev == NULL && currentNode->next == NULL) {
		(*ll)->head = NULL;

		free(currentNode);
	} else if (currentNode->prev == NULL && currentNode->next != NULL) {
		struct Node* temp = currentNode;

		(*ll)->head = currentNode->next;
		(*ll)->head->prev = NULL;
		free(temp);
	} else if (currentNode->prev != NULL && currentNode->next == NULL) {
		struct Node* temp = currentNode;

		currentNode->prev->next = NULL;
		free(currentNode);
	} else if (currentNode->prev != NULL && currentNode->next != NULL) {
		struct Node* temp = currentNode;

		currentNode->prev->next = currentNode->next;
		currentNode->next->prev = currentNode->prev;
		free(currentNode);
	}
	(*ll)->size -= 1;

	return removedData;
}

void clear(struct LinkedList** ll) {
	/*
		Removes all nodes from the linked list
	*/

	struct Node* currentNode = (*ll)->head;

	while (currentNode != NULL) {
		(*ll)->head = (*ll)->head->next;

		free(currentNode);
		(*ll)->size -= 1;

		currentNode = (*ll)->head;
	}
}

void printList(struct LinkedList** ll) {
	struct Node* currentNode = (*ll)->head;

	printf("Size %d: ", (*ll)->size);
	while (currentNode != NULL) {
		printf("%d ", currentNode->data);
		currentNode = currentNode->next;
	}
	printf("\n\n");
}

int main() {

	// Initialize an empty linked list
	struct LinkedList* linkedList = (struct LinkedList*)malloc(sizeof(struct LinkedList));;
	linkedList->head = NULL;
	linkedList->size = 0;
	
	printf("Appending 1, 2, 3 to the linked list\n");
	append(&linkedList, 1);
	append(&linkedList, 2);
	append(&linkedList, 3);
	printList(&linkedList);

	printf("Pushing 4, 5, 6 to the linked list\n");
	push(&linkedList, 4);
	push(&linkedList, 5);
	push(&linkedList, 6);
	printList(&linkedList);

	printf("Getting some values from linked list\n");
	printf("Index 0: %d\n", getValueAt(&linkedList, 0));
	printf("Index 3: %d\n", getValueAt(&linkedList, 3));
	printf("Index %d: %d\n", linkedList->size-1, getValueAt(&linkedList, linkedList->size-1));

	printf("\nRemoving some values from linked list\n");
	printf("Removing Index 0: %d\n", removeNodeAt(&linkedList, 0));
	printList(&linkedList);
	printf("Removing Index %d: %d\n", linkedList->size - 1, removeNodeAt(&linkedList, linkedList->size - 1));
	printList(&linkedList);
	printf("Removed Index 1: %d\n", removeNodeAt(&linkedList, 1));
	printList(&linkedList);

	printf("Clearing linked list\n");
	clear(&linkedList);
	printList(&linkedList);
}
