#include <stdio.h>
#include <ctype.h>
#include <time.h>

void print_border(int length) {
    for (int i = 0; i < length; i++) {
        printf("-");
    }
    printf("\n");
}

void convert_to_uppercase(char str[]) {
    for (int i = 0; str[i]; i++) {
        str[i] = toupper(str[i]);
    }
}

int main() {
    char first_name[50], last_name[50];

    // Accept user input for first and last names
    printf("Enter your first name: ");
    fgets(first_name, sizeof(first_name), stdin);

    printf("Enter your last name: ");
    fgets(last_name, sizeof(last_name), stdin);

    // Remove newline characters that fgets may add
    first_name[strcspn(first_name, "\n")] = 0;
    last_name[strcspn(last_name, "\n")] = 0;

    // Convert names to uppercase
    convert_to_uppercase(first_name);
    convert_to_uppercase(last_name);

    // Determine the width of the border
    int width = 2 + strlen(first_name) + strlen(last_name) + 1;

    // Print the top border
    print_border(width);

    // Print the names inside the border
    printf("| %s %s |\n", first_name, last_name);

    // Print the bottom border
    print_border(width);

    // Get and display the current date and time
    time_t t;
    struct tm *tm_info;

    time(&t);
    tm_info = localtime(&t);

    // Print current date and time
    printf("\nCurrent Date and Time: ");
    printf("%02d-%02d-%d %02d:%02d:%02d\n", tm_info->tm_mday, tm_info->tm_mon + 1, tm_info->tm_year + 1900,
           tm_info->tm_hour, tm_info->tm_min, tm_info->tm_sec);

    // Print copyright info at the bottom
    printf("\nCopyright (C) 2024 Your Company. All rights reserved.\n");

    return 0;
}
