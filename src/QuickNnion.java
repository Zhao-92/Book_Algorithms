/**
 * Created by Zcl on 2016/10/27.
 */
public class QuickNnion {

    private int[] id;   //每个节点指向的父节点
    private int[] sz;   //根节点所在集合大小
    private int count;  //连通分量数（集合数）

    public QuickNnion(int n){
        count = n;
        id = new int[n];
        sz = new int[n];
        for (int i=0;i<n;i++){
            id[i] = i;
            sz[i] = 1;
        }
    }

    public int getCount(){
        return count;
    }

    public int find(int p){
        while (p != id[p])
            p = id[p] ;
        return p;
    }

    public void union(int p,int q){
        int i = find(p);    // 根节点
        int j = find(q);    // 根节点
        if (i == j) return ;
        if(sz[i] > sz[j]){
            id[j] = i;   //小的树指向大的树
            sz[i] += sz[j];          //更新节点指向根节点所在集合大小
        }
        else{
            id[i] = j;   //小的树指向大的树
            sz[j] += sz[i];          //更新节点指向根节点所在集合大小
        }
        count --;
    }

}
