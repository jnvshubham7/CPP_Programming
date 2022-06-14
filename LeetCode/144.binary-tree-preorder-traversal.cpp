/*
 * @lc app=leetcode id=144 lang=cpp
 *
 * [144] Binary Tree Preorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> ans;
    void solve(TreeNode* root)
    {
        if(root==NULL)
        {
            return;
        }
        ans.push_back(root->val);
        solve(root->left);
        solve(root->right);
    }

    
    vector<int> preorderTraversal(TreeNode* root) {
        solve(root);
        return ans;
        
    }
};
// @lc code=end









#include<bits/stdc++.h>
using namespace std;
#define ll long long


struct TreeNode{
        int val;
        TreeNode* left;
        TreeNode* right;

       TreeNode() : val(0), left(nullptr), right(nullptr) {}
       TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
       TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}

    };



    void solve(TreeNode* root)
    {
        if(root==NULL)
        return;
       
       cout<<root->val<<" ";
        solve(root->left);
        solve(root->right);
        
    }

 
    

int main(){

   //take input from user and create a tree
    //Input: root = [1,null,2,3]

    TreeNode* root = new TreeNode(1);
    root->left = NULL;
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);

   solve(root);

    return 0;
}