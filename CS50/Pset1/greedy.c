/**
 * greedy.c
 *
 * Francis Lee
 * francis.g.lee@gmail.com
 *
 * Outputs the smallest number of coins need make change.
 */


#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Declare variable; x = value of change
    float x;
    
    // check whether the input is positive
    while (true)
    {
        printf("How much change do you need? ");
        x = GetFloat();
        if (x >= 0)
            break;
    }
    
    // converts dollars to cents; it seems easier to work with values in cents instead of dollars; y = change in cents
    int y = x * 100;
    
    // Determine number of each coin needed
    int quarters = y / 25;
    int dimes = y % 25 / 10;
    int nickels = y % 10 / 5;
    int pennies = y % 5;
    
    // sum total of coins; z = total number of coins
    int z = quarters + dimes + nickels + pennies;
    
    // Output calculation
    if (z > 0)
    {   
        //specify total number of coins
        printf("Total number of coin(s) required: %d\n", z);

        // specify optimal set of coins
        printf("You need:\n");
        
        if (quarters > 1)
            printf("%d quarters \n", quarters);
        else if (quarters == 1)
            printf("%d quarter \n", quarters);
    
        if (dimes > 1)
            printf("%d dimes \n", dimes);
        else if (dimes == 1)
            printf("%d dime \n", dimes);
    
        if (nickels > 1)
            printf("%d nickels \n", nickels);
        else if (nickels == 1)
            printf("%d nickel \n", nickels);
    
        if (pennies > 1)
            printf("%d pennies \n", pennies);
        else if (pennies == 1)
            printf("%d penny \n", pennies);
    }
    else
    {
        printf("No change for you.\n");
    }
    
    return 0;
}
