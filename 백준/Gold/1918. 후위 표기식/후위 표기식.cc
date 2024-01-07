#include <stdio.h> 
#include <string.h> 
#include <stdlib.h>



int p(char *string, int j,int num) {//stack인 경우 num=0
    char a=string[j];
 
    if (num==1&&j!=0&&(1 <= p(string, j - 1,1) && p(string, j - 1,1) <= 6)) {
        if (a == '-' || a == '+') {
            return 6;//앞에 부호가 있을 때, 단일연산자
        }
    }
    if (num == 1 && j == 0 && (a == '-' || a == '+')) {// 맨 앞 단일연산자
        return 6;
    }
    else if (a == '(') {
        return -7;
    }
    else if (a == '|') {
        return 1;
    }
    else if (a == '&') {
        return 2;
    }
    else if (a == '<' || a == '>') {
        return 3;
    }
    else if (a == '-' || a == '+') {
        return 4;
    }
    else if (a == '/' || a == '*') {
        return 5;
    }
    else if (a == '!')
        return 6;

    else {
        return 0;
    }
}


void convert(char* string) {

    char* stack;
    char ch;
    int top = -1;
    stack = (char*)malloc((strlen(string) + 1) * sizeof(char));
    int j;
    for (j = 0; j < strlen(string); j++) {
        ch = string[j];

        if (ch == '(') {
            top++;
            stack[top] = ch;
        }
        else if (ch == ')') {
            while (stack[top] != '(') {//열린 괄호가 나오기 전까지빼냄
                printf("%c", stack[top]);
                top--;
            }
            top--;
        }
        else if (p(string,j,1) == 0) {//피연산자인 경우
            printf("%c", ch);
        }
        else {//연산자인 경우
            if (j!=0&&!(p(string,j - 1,1) == 1 && p(string,j,1) == 1) && !(p(string,j - 1,1) == 2 && p(string,j,1) == 2)) {
                
                while ((top != -1) && (p(string,j,1) <= p(stack,top,0))) {//??

                    printf("%c", stack[top]);
                    top--;
                }
            }
            top++;
            stack[top] = ch;

        }
       

     
    }
    while ((top != -1) ){
        printf("%c", stack[top]);
        top--;
    }

    printf("\n");

    free(stack);
}


int main()
{
    char string[101];
    int n,i;
    char ch, top_op;
    
    //scanf("%d", &n);
    //getchar();
    //for (i = 0; i < n; i++) {
        scanf("%s",string);
        getchar();
        convert(string);
    //}
   
}