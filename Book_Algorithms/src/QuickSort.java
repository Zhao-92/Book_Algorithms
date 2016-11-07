/**
 * Created by Zcl on 2016/11/7.
 */

public class QuickSort {
    // 如果数组中有两个一样的元素？
    private static int partition(int[] a ,int lo ,int hi){
        System.out.println("test_part");
        int i = lo+1;
        int j = hi;
        while (i<j){
            while (less(a,i,lo))
                i++;
            while (less(a,lo,j))
                j--;
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
        System.out.println("test");
        while (true){
            if (lo >= hi)
                break;
            int index = partition(a , lo , hi);
            show(a);
            sort(a,lo,index-1);   //左排序
            sort(a,index+1,hi);   //右排序
        }

    }

    // i 比 j 小
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
            if (a[i-1] > a[i++])
                System.out.println("Is sorted !");
            else
                System.out.println("Not sorted !");

    }

    public static void main(String[] args){
        int[] a = {6,1,2,5,3,4};
        show(a);
        sort(a,0,a.length-1);
//        show(a);
//        isSorted(a);
    }

}
