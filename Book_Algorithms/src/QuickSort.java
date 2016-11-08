/**
 * Created by Zcl on 2016/11/7.
 *
 * 快速排序，不支持排序数组中有重复元素
 */

public class QuickSort {
    // 如果数组中有两个一样的元素？
    private static int partition(int[] a ,int lo ,int hi){
        int i = lo+1;
        int j = hi;
        while (i<j){
            while (i < hi && less(a,i,lo))
                i++;
            while (j >= lo+1 && less(a,lo,j))
                j--;
            if(i<j)
                exch(a,i,j);
        }
        exch(a,lo,j);
        return j;  //返回中间大小的指针
    }

    private static void exch(int[] a ,int i ,int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    private static void sort(int[] a , int lo ,int hi){
        if (lo > hi-1)
            return;
        int index = partition(a, lo, hi);
        sort(a, lo, index - 1);   //左排序
        sort(a, index + 1, hi);   //右排序
    }

    private static boolean less(int[] a , int i , int j){
        return a[i]<a[j];
    }

    private static void show(int[] a){
        for (int i=0 ; i<a.length ; i++)
            System.out.println(a[i]);
    }

    private static void isSorted(int[] a){
        int i = 1;
        while (i < a.length)
            if (a[i-1] <= a[i++])
                return;
        System.out.println("Is sorted !");
    }

    public static void main(String[] args){
        int[] a = {6,1,2,15,24,16,498,64,54,48,465,32,136,546,86,468,5,3,4};
        sort(a,0,a.length-1);
        show(a);
        isSorted(a);
    }

}
