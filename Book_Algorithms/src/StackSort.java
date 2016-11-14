/**
 * Created by Zcl on 2016/11/9.
 *
 * 基于堆优先队列的排序
 */
public class StackSort {
    int num;
    int[] value;       //索引0不使用，从1开始

    public StackSort(int[] n){
        value = n;
    }

    public int size() {
        return num;
    }

    // 上浮操作，维护二叉堆顺序性
    public void swim(int index){
        while (index > 1 && value[index] > value[index/2]){
            exch(index,index/2);
            index = index / 2;
        }
    }

    // 下沉操作，维护二叉堆顺序性
    public void sink(int index){
        while (2*index <= num ){
            int j = 2*index;
            if (j < num && value[j] < value[j+1])
                j++;
            if (value[index] < value[j])
                break;;
            exch(index,j);
            index =j;
        }
    }

    public void insert(int v){
        value[++num] = v;
        swim(num);
    }

    public int delMax(){
        int max = value[1];
        value[1] = value[num];
        value[num--] = null;
        sink(1);
        return max;
    }

    public void exch(int i,int j){
        int temp = value[i];
    }
}
