https://leetcode.com/problems/subsets/discuss/1572198/Java-and-recursion

//https://leetcode.com/problems/subsets/
class Solution {
    List<List<Integer>> sol = new ArrayList<List<Integer>>();
    int[] ns;
    void gen(int n, List<Integer> l) {
        if (n == ns.length) {
            sol.add(l);
            return;
        }

        List<Integer> l2 = new ArrayList(l);
        l2.add(ns[n]);
        gen(n + 1, l2);
        gen(n + 1, l);
    }

    public List<List<Integer>> subsets(int[] nums) {
        ns = nums;
        gen(0, new ArrayList<Integer>());
        return sol;
    }
}
