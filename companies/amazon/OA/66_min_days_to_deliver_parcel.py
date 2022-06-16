# https://leetcode.com/discuss/interview-question/2061294/Amazon-OA

'''
Got these questions in OA recently. Hope it will help someone.

#################################################################################################################
Find Minimum Days to Deliver Parcels
https://leetcode.com/discuss/interview-question/1998840/Amazonor-OA-or-Minimum-Days-to-Deliver-All-Parcels

#################################################################################################################
There is N delivery centers. Each Devliery Outlet has some packages to be delivered, denoted by parcels[i]. There is a Rule how delivery should be completed. On each day, an equal number of parcerls are to be dispatched from each delivery center that has atleast one parcel remaining.

Find minimum nunmber of days needed to deliver all the parcels.
Input:
parcels= {2,3,4,3,3}

Output
3

Solutions:
Iterate over the list/ array, count distinct elements i.e desired minimum days

Please post if you know any other logic/ soultions.

#################################################################################################################
Find Maximum Sustainable Cluster Size
https://leetcode.com/discuss/interview-question/1636493/Amazon-or-OA-or-Max-Length-of-Valid-Server-Cluster
################################################################################################################# 


Question2:
Give you a list servers. Their processing power is given as a array of integer, and boot power as a array of integer.
Write a function to return the max length of sub array which's power consumption is less than or equal to max power limit.
Formula to calculate the power consumption for a subArray is:
Max(bootPower[i...j]) + Sum(processPower[i....j]) * length of subArray.

Note: Single server is also a subArray, return 0 if no such subArray can be found.

public int MaxLengthValidSubArray(int[] processingPower, int[] bootingPower, int maxPower)
{}
Does anyone know what is the similar question in leetcode?
Its a variant to the most popular Amazon Question Sliding Window Maximum(https://leetcode.com/problems/sliding-window-maximum/). 
My solution works for all test cases: https://leetcode.com/playground/E9ogoZrS
'''

int findMaximumSustainableClusterSize(vector<int> processingPower, vector<int> bootingPower, long powerMax){
    int n = processingPower.size();
    int i = 0;
    int j = 0;
    
    deque<vector<int>> q;
    long sum = 0;
    int ans = 0;
    while(j < n){
        sum += processingPower[j];
        while(!q.empty() && q.back()[0] <= bootingPower[j]){
            q.pop_back();
        }
        q.push_back({bootingPower[j], j});
        
        while(i <= j and q.front()[0] + sum*(j-i+1) > powerMax){
            if (q.front()[1] == i){
                q.pop_front();
            }
            sum -= processingPower[i];
            i++;
        }
        ans = max(ans, j-i+1);
        j++;
        
    }
    
    return ans;
}
int main() {
    vector<int> processingPower{4,1,4,5,3}, bootingPower{8,8,10,9,12};
    long powerMax = 1;
    
    cout << findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax);
}
