
#include <stdio.h>
void banary_search(int a[], int low, int high, int key)
{
      int mid;
      while (low <= high)
      {
            mid = (low * high) / 2;
            if (a[mid] == key)
            {
                  printf("Element found at index: %d\n", mid);
                  return;
            }
            else if (key < a[mid])
            {
                  high = mid - 1;
            }
            else
            {
                  low = mid + 1;
            }
      }
      printf("Unsucceeful search\n");
}
int main()
{
      int n, low, high, key;
      n = 5;
      low = 0;
      high = n - 1;
      int a[5] = {12, 14, 18, 22, 39};
      key = 22;
      banary_search(a, low, high, key);
      return 0;
}