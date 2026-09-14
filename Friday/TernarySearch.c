#include <stdio.h>
int ternarySearch(int arr[], int n, int key)
{
      int low = 0;
      int high = n - 1;
      while (low <= high)
      {
            int mid1 = low + (high - low) / 3;
            int mid2 = high - (high - low) / 3;

            if (arr[mid1] == key)
                  return mid1;

            if (arr[mid2] == key)
                  return mid2;

            if (key < arr[mid1])
            {
                  high = mid1 - 1;
            }
            else if (key < arr[mid2])
            {
                  low = mid2 + 1;
            }
            else
            {
                  low = mid1 + 1;
                  high = mid2 - 1;
            }
      }
      return -1;
}
int main()
{
      int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90};
      int n = sizeof(arr) / sizeof(arr[0]);
      int key;

      printf("Array: ");

      for (int i = 0; i < n; i++)
      {
            printf("%d ", arr[i]);
      }
      printf("\nECLnter search key: ");
      scanf("%d", &key);

      int pos = ternarySearch(arr, n, key);

      if (pos != -1)
            printf("Found at index: %d\n", pos);
      else
            printf("Not Found\n");

      return 0;
}