---
title: Minecraft | 搭建MC服务器
date: 2024-08-17
tags:
  - Minecraft
  - Linux
categories:
  - Log
---

# 搭建MC服务器

这几天一直在高强度玩 Minecraft，于是就突然想在我的 ARM Linux 上开个服务器玩玩，结果一查资料发现开启其实很简单，但是要掌握服务器状态、自由修改服务器的版本模组等、以及服务器的维护并不是一个简单的事。私以为开好一个 MC 服务器不亚于一场计算机与网络知识应用的练习，那么就尝试一下吧

!!! info

    本教程使用的是 Linux 平台的 Ubuntu 系统，所有操作均在命令行中以命令的形式操作，因此具有一定门槛，但是胜在操作方便快捷，基本只需复制粘贴，且能够最大限度地发挥计算机的性能。想要查看 Windows 服务器版本的教程请移步 [【SherkHol】我的世界mod服务器开设教程 模组服 新手简单易学，Java版通用，内网穿透 - 服务器系列#2](https://www.bilibili.com/video/BV1Fv41147kb/)

<!-- more -->

## 安装依赖

由于`Java`的运行环境是`JVM`(Java virtual machine)，因此它有着可以在全平台运行的特性，这也是 Java 版 Minecraft 通常被用于构建服务器版本的原因之一。所以，我们需要先在服务器上安装对应版本的 JDK(Java Development Kit)，这里我们需要安装对应版本的 OpenJDK，它是对 Java 的一种官方的开源参考实现，可以认为 OpenJDK 和 OracleJDK 是一样的[^1]。这里我们要安装的 Minecraft 版本为 1.21 ，需要安装的 OpenJDK 对应版本为 JDK 21。注意这里两个软件的版本并不是一一对应的，只是在这里我们要安装的版本号恰好相同，对于你想要安装的 Minecraft 版本，请搜索所要求的对应的 JDK 版本，或按照此教程安装下去查看报错信息，安装报错信息中要求的版本也可

[^1]: 来源：[https://zh.minecraft.wiki/w/Tutorial:%E6%9E%B6%E8%AE%BEJava%E7%89%88%E6%9C%8D%E5%8A%A1%E5%99%A8?variant=zh-cn](https://zh.minecraft.wiki/w/Tutorial:%E6%9E%B6%E8%AE%BEJava%E7%89%88%E6%9C%8D%E5%8A%A1%E5%99%A8?variant=zh-cn)

``` shell
# 更新包列表
sudo apt update
# 安装OpenJDK
sudo apt install openjdk-21-jdk
```

安装完成后查看`Java`是否已经被添加到环境变量:

``` shell
java -version
```

至此，我们的前置工作就已经做完了，相当轻松

## 安装纯净游戏本体

如果你只想要体验纯净版的游戏，不安装任何 mod，那么这将非常轻松

## 安装 Fabric Server



## References

1. [Minecraft wiki: 教程:架设Java版服务器](https://zh.minecraft.wiki/w/Tutorial:%E6%9E%B6%E8%AE%BEJava%E7%89%88%E6%9C%8D%E5%8A%A1%E5%99%A8?variant=zh-cn)
2. [我的世界 Fabric 1.19.3 服务器搭建教程](https://blog.zeruns.tech/archives/699.html)
3. [【SherkHol】我的世界mod服务器开设教程 模组服 新手简单易学，Java版通用，内网穿透 - 服务器系列#2](https://www.bilibili.com/video/BV1Fv41147kb/)
4. [Getting started with MCSS](https://docs.mcserversoft.com/)