#include <stdio.h>
int exponentailSearch(int arr[], int n, int key)
{
      if (arr[0] == key)
            return 0;
      int i = 1;
      while (i < n && arr[i] <= key)
            i = i * 2;
      int low = i / 2;
      int hight = (i < n) ? i : n - 1;
      while (low < hight)
      {
            int mid = (low + hight) / 2;
            if (arr[mid] == key)
                  return mid;
            if (arr[mid] < key)
                  low = mid + 1;
            else
                  hight = mid - 1;
      }
      return -1;
}
int main()
{
      int arr[10] = {6, 11, 19, 24, 33, 54, 67, 81, 94, 99};
      int n = 10;
      int key = 99;
      printf("Array element: ");
      for (int i = 0; i < n; i++)
            printf("%d ", arr[i]);
      printf("\nSearch key: %d ", key);
      int pos = exponentailSearch(arr, n, key);
      if(pos != -1)
            printf("\nFound at index: %d", pos);
      else
            printf("\nNot Found!!!");
}