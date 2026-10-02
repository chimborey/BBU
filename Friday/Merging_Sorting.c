#include<stdio.h>
#define max 7

int a[8] = {14, 33, 27, 10, 35, 19, 42, 44};
int b[8];

void merging(int low, int mid, int hight){
      int left, right, i;
      left = low;
      right = mid + 1;
      for (i = low; left <= mid && right <= hight; i++)
      {
            if (a[left] <= a[right])
            {
                  b[i] = a[left];
                  left++;
            }else
            {
                  b[i] = a[right];
                  right++;
            }
      }
      while (left <= mid)
      {
            b[i] = a[left];
            i++;
            left++;
      }
      while (left <= mid)
      {
            b[i] = a[right];
            i++;
            right++;
      }
      for (i = low; i <= hight; i++)
      {
            a[i] = b[i];
      }
}

void sort(int low, int hight){
      int mid;
      if (low < hight)
      {
            mid = (low + hight)/2;
            sort(low, mid);
            sort(mid + 1, hight);
            merging(low, mid, hight);
      }
      
}


int main(){
      int i;
      printf("Array before sorting: \n");
      for (i = 0; i <= max; i++)
      {
            printf("%d ", a[i]);
      }
      sort(0, max);
      printf("\n\nArray after sorting: \n");
      for (i = 0; i <= max; i++)
      {
            printf("%d ", a[i]);
      }
      return 0;
}