// https://leetcode.com/problems/path-with-maximum-probability/   
class Solution {
       public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {  
        // E maps a vert to a map of vert/weight pairs representing an edge
        HashMap<Integer, HashMap<Integer, Double>> E = new HashMap<>();
        for(int j = 0; j < edges.length; j++) {
            int from   = edges[j][0];
            int to     = edges[j][1];
            double succ= succProb[j];
            
            // since edges are undirectional both verts store an egde with the same
            // probability to the other edge
            HashMap<Integer, Double> h  = E.getOrDefault(from, new HashMap<>());
            h.put(to  , succ);
            E.put(from, h);
            
            h = E.getOrDefault(to, new HashMap<>());
            h.put(from, succ);
            E.put( to,   h);
        }
        
        HashMap<Integer, Double> empty = new HashMap<>();
        
        int[]    Heap = new int[n];    // id of node in heap
        int[]    Pos  = new int[n];    // position of node in heap
        double[] Cost = new double[n]; // cost of node
           
        // initialize
        int sz = n;
        
        for(int i = 0; i < n; i++) {
            Pos[i]  = i;
            Heap[i] = i;
            Cost[i] = 0.0;
        }
        
        /// put starting node at top of heap
        Heap[0]     = start;
        Pos[start]  = 0;
        Cost[start] = 1.0;
        
        Heap[start] = 0;
        Pos[0]      = start;
        
        // pop top of priority queue from heap which is the node with the highest
        // probability
        while (sz != 0) {
            int anode = Heap[0];
            
            // pop node
            Heap[0] = Heap[sz - 1];
            Pos[Heap[0]] = 0;
            
            // put bottom node switched with top node in the right position
            sz--;
            
            int cur = 1;
            while (true) {
                int swap  = cur;
                int left  = cur * 2;
                int right = left + 1;
                
                if (left  <= sz && Cost[Heap[left - 1]]  > Cost[Heap[swap - 1]]) 
                    swap = left;
                
                if (right <= sz && Cost[Heap[right - 1]] > Cost[Heap[swap - 1]]) 
                    swap = right;
                
                if (swap == cur)
                    break;
                
                int pid = Heap[cur - 1];
                int cid = Heap[swap - 1];
                
                Pos[Heap[swap - 1]] = cur - 1;
                Pos[Heap[cur - 1] ] = swap - 1;
                
                int tmp   = Heap[swap - 1];
                Heap[swap - 1] = Heap[cur - 1];
                Heap[cur - 1 ] = tmp;
                
                cur = swap;               
            }

            // from the current node update every edge with higher probability
            // if possible
            for(Integer e : E.getOrDefault(anode, empty).keySet()) {
                
                // update edge if probability is higher from anode to e
                double newcost = Cost[anode] * E.get(anode).get(e);
                if (newcost > Cost[e]) {
                    Cost[e] = newcost;
                    
                    // lift up node in heap because the probability has increased
                    cur = Pos[e] + 1;
                    while (cur != 1) {
                        int parent = cur / 2;
                        int pid = Heap[parent - 1];
                        int cid = Heap[cur - 1];
                        if (Cost[pid] > Cost[cid]) 
                            break;

                        Pos[Heap[parent - 1]] = cur - 1;
                        Pos[Heap[cur - 1]]    = parent - 1;
                        
                        int h = Heap[parent - 1];
                        Heap[parent - 1] = Heap[cur - 1];
                        Heap[cur - 1] = h;
                        
                        cur = parent;
                    }
                }
            }
        }
    
        // return answer        
        return Cost[end];
    }
}
