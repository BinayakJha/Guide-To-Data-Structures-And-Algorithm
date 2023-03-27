#include <stdio.h>
#include <stdlib.h>

int find_hacker_email(char *emails[], int size){
    int i,j;
    int max_count = 0;
    int count = 0;
    for(i=0;i<size;i++){
        for(j=1;j<size;j++){
            if(emails[i] == emails[j] && i != j){
                count++;
            }
        }
        if(count > max_count){
            max_count = count;
        }
        count = 0;
    }
    
    return printf("The hacker email is: %s", emails[max_count]);;
}

int main(){
//    emails are strings 
    char *emails[] = {"hey@skilled.dev",
                "a@b.test",
                "hey@skilled.dev",
                "hey@skilled.dev",
                "a@b.test",
                "c@d.test",
                "c@d.test",};
    int size = sizeof(emails)/ sizeof(emails[0]);
    find_hacker_email(emails, size);
}