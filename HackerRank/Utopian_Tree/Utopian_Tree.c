#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int SpringGrowthCycle(int Height) // Calculates Height growth during spring cycle
{
    return 2 * Height;
}

int SpringSummerGrowthCycle(int Height) // Calculates Height growth after spring summer cycle
{
    return 2 * Height + 1;
}

int SummerSpringGrowthCycle(int Height) // Calculates Height growth after summer spring cycle
{
    return 2 * (Height + 1);
}

int CalculateFinalHeight(int n) // measures the height of Tree after n cycles
{  
    // Declare variables    
    int StartingHeight = 1; 
    int Height;
    int FinalHeight;
    
    if (n == 0) // Growth cycle of 0
    {
        return StartingHeight;
    }
    
    else if (n == 1) // Spring Growth Cycle only
    {
        return SpringGrowthCycle(StartingHeight);
    }
    
    else if (n % 2 == 0) // Trees with even number growth cycles
    {
        Height = StartingHeight;
        for (int i = 0; i < n/2; i++)
        {
            Height = SpringSummerGrowthCycle(Height);
            FinalHeight = Height;
        }              
        return FinalHeight;
    }
    else // Trees with odd number growth cycles
    {
        Height = SpringGrowthCycle(StartingHeight);
        for (int i = 0; i < ((n - 1)/2); i++)
        {
            Height = SummerSpringGrowthCycle(Height);
            FinalHeight = Height;   
        }
    }
    return FinalHeight;  
}

int main() 
{
  // declare variables
  int t; // number of test cases
  int n; // test case
  int Height; // height of test case
    
  scanf("%d",&t);   
  
  for (int i = 0;i < t; i++) 
  {
    scanf("%d",&n);
    
    Height = CalculateFinalHeight(n);
    
    printf("%d\n", Height);
  }
  return 0;
}
