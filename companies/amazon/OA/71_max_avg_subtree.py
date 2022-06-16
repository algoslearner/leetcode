# https://leetcode.com/discuss/interview-question/1786827/Amazon-OA
'''
Question 1
Maximum Avarage Subtree (In The Name Of Employee Tree)
Solution:
Java bottom-up naive recursion solution with complexity O(N).
(src-https://leetcode.com/problems/maximum-average-subtree)
My Solution-->

public class Solution {
    public class Result{
    int sum  , num;
    Result(int sum , int num){
        this.sum = sum;
        this.num = num;
    }
}
TreeNode maxNode = null;
Result maxResult = null;
    public TreeNode findSubtree2(TreeNode root) {
        MaxFinder(root);
        return maxNode;
    }
    public Result MaxFinder(TreeNode root){
        if(root == null)
            return new Result(0 , 0);
        Result left = MaxFinder(root.left);
        Result right = MaxFinder(root.right);
        Result rootResult= new Result(left.sum+ right.sum + root.val , left.num + right.num + 1);
        if(maxNode == null || maxResult.sum*rootResult.num<maxResult.num*rootResult.sum){
            maxResult = rootResult;
            maxNode =  root;
        }
        return rootResult;
}
}
Question 2 :
Find The Highest Profit(MaxHeap Problem)
Solution:
(Same as src- https://leetcode.com/problems/sell-diminishing-valued-colored-balls/)

FYI - Could not do the 2nd 

'''

