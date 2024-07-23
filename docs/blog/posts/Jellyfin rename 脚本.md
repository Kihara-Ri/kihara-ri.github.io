---
title: Jellyfin rename 脚本
date: 2024-07-23
tags:
  - Python
  - Regex
categories:
  - Logs
---

# Jellyfin rename 脚本

最近在 Jellyfin 上看番，发现一个问题：对于日常的追番，我们可以借助 AutoBangumi 等工具托管RSS订阅并由它自动生成格式，但是如果要下载一些老番，已完成的合集，我们直接通过qbittorrent下载的话，得到的文件，字幕组打包好的文件的确有规整的格式，但是这些冗长的文件格式对于 Jellyfin 这些媒体挂削器来说就成为了负担，经常会导致程序无法正常识别番剧，甚至有些视频文件重名，直接打不开。因此，我们需要将这些文件名称规范一下

<!-- more -->

## 命名规则

对于这些影视程序，一般都有相同的命名标准，我们需要遵循这样的命名结构：

``` plaintext title="命名结构"
/shows/大明王朝1566/S01E01-大明王朝1566.mp4
```

我们需要注意电影哪怕只有一个文件，也不能直接放在`shows`目录下，这样会识别不出，必须创建一个文件夹，程序是以文件夹来划分不同影视的

这里`S01`代表的是`Season 1`，`E01`代表的是`Episode 1`

在一些有多季度的番剧和电视剧中我们也可以单独创建`Season 1`、`Season 2`文件夹来划分不同季

## 正则表达式结构

现在进入问题：

有两部这样结构的番剧：

``` bash title="番剧名称"
# 家有女友
'[VCB-Studio] Domestic na Kanojo [01][Ma10p_1080p][x265_flac].mkv'

# 攻壳机动队
'[VCB-S&philosophy-raws][Ghost in the Shell：STAND ALONE COMPLEX][01][BDRIP][HEVC Main10P FLAC][1920X1040].mkv'
'[VCB-S&philosophy-raws][Ghost in the Shell：S.A.C. 2nd GIG][01][BDRIP][HEVC Main10P FLAC][1920X1040].mkv'
```

我们可以发现字幕组的命名策略大致不离开这个思路：由多个`[ ]`组成的部分用来描述番剧信息，其中我们需要关注的是前三项：
1. `[字幕组名称]`，有的字幕组会用`【 】`来代替
2. `[番剧名称]`，通常使用英文命名，当然我们例子中的第一部并没有使用`[ ]`进行包裹，不过我们仍有办法处理
3. `[集数]`，不排除有的字幕组有例外，但是绝大部分的字幕组都是如此命名，使用两位数字命名

