---
title: hash表 
date: 2023-12-14
tags: 
  - hash表 
  - problem 
  - C++
categories: 
  - CS
---

# 🟠 hash 表

算法中常用到的内容

<!-- more -->

## 题目：1748.唯一元素的和

给你一个整数数组 `nums` 。数组中唯一元素是那些只出现 **恰好一次** 的元素。

请你返回 `nums` 中唯一元素的 **和** 。

### 我的解法

```c++
class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int hash[101]={0};//定义一个哈希表
        int n=nums.size();
        for(int i=0;i<n;i++)//暴力遍历，每遍历一个数，就在该值所对应的哈希表序号上+1
        {
            hash[nums[i]]++;
        }
        int ans=0;
        for(int i=0;i<101;i++)//将所得到的所有唯一的值相加，这里遍历的是整个hash表
        {
            if(hash[i]==1)
            {
                ans+=i;//这里的i就是哈希表的序号，因此也就是数组的值
            }
        }
        return ans;
    }
};
```

初学时没有搞清楚哈希表的含义，从原理上理解其实就是抓住唯一特性

我们创建一个哈希表令表中所有的值全为0，遍历数组，碰到一个数就+1，有重复的我们就得想办法在之前的地方在原有的基础上+1，但是怎么实现呢？

这里就得抓住数组元素的核心特征：

数的**值(key)**

因此只需：

遍历i的时候`hash[nums[i]]++`,在这个值所对应的hash表序号上，这样值就可以与序号唯一确定，这就是hash表的实际应用

现在想来还是挺简单的