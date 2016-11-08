/**
 * Created by Zcl on 2016/11/8.
 *
 * 基于堆的优先队列
 */
public class MaxPQ {
    int num;
    int[] value;       //索引0不使用，从1开始

    public MaxPQ(int n){
        value = new int[n];
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
        while (2*index <= num && value[index] < value[2*index]){
            exch(index,2*index);
            index = 2*index;
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
