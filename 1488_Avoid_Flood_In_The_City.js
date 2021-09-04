
/*
https://leetcode.com/problems/avoid-flood-in-the-city/submissions/
*/
var avoidFlood = function(rains) {
    let ans     = [];
    let lakes   = new Map(); // lake is key; value is rainy day 
    
    for (let [n, l] of rains.entries()) {
        ans[n] = 0; // dummy answer; this day can be used to dry a lake
        
        if (l == 0) 
            continue; // nothing to do
        
        // do nothing on a rainy day
        ans[n] = -1;
        
        // get the day the last time this lake was rained over
        let p = lakes.get(l);
        
        // lake l is rained over on this day
        lakes.set(l, n);

        // lake is full and today is raining
        if (p != undefined) {
            // start looking from the day the last time lake l was rained over + 1 
            // until the day before today to find a dry day when lake can be dried.
            let i = p + 1;
            
            while (true) {
                // no suitable day found; :(
                if (i == n) 
                    return [];
               
                if (ans[i] == 0) { 
                    // found a dry day so dry the lake
                    ans[i] = l;
                    break;
                }
                
                i++;
            }
        } 
    }
    
    // sad but need to do this
    return ans.map((i) => (i == 0) ? 1 : i);
};
