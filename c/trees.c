#include <stdio.h>

typedef struct node {
	float value;
	struct node *next;
	int idx;
}node;

float getValue(int idx, node *root){
	while(root != NULL){
		if root->value == idx{
			return root->value;
		}
		root = root->next;
	}
	printf("Index not in list");
	return NULL;
}

void addNode(int newIdx, float newValue){
	while(root != NULL){
		if((root->idx < newIdx) and (
		root = root->next
	}
}

int main(){
	
	return 0;
}
