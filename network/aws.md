AWS
https://www.youtube.com/watch?v=SOTamWNgDKc

公司最近开始在使用AWS我在这里记录一下每天使用的过程那么公司最近开始在使用AWS我在这里记录一下每天使用的过程:

## AWS CLI
 
 从官网down就好

## ADFS

  这个其实就是我们自己实现的一个小工具,原理用python 就打开AWS的登陆页面输入账号密码,选择一个IAM账户,
  之后拿到token信息把aws账户的token 写到本地的 ~/.aws/credentials中,大概这个样子

    ```
     [saml]
     output = json
     aws_access_key_id = dfasdf
     aws_access_key_id = dfasdf
     region = eu-west-1
     aws_sestion_token = dfasdf

    ```

## terrform   
 [官网](https://www.terraform.io/)     
 ### 介绍
 一门脚本语言, 目的是 Infostruct as language(架构作为语言), 简单地说在使用aws的各种组件时一步一步的点击,一步步配置时间久了大家都记不住,所以搞成一些脚本,自己定义比变量,定义组建名字等. 统一管理方便快捷,高端大气有格调.
 [下载地址](https://www.terraform.io/downloads)
 ### 实践
 没什么废话就是 一个地址告诉这东西怎么用:[教程] (https://learn.hashicorp.com/collections/terraform/aws-get-started)
 感觉so easy. 


1 AWS IAM user
IAM user 是 root user 创建的,用ID or allias 登陆.
IAM 里可以配置用户组,没个组有一定的权限.
公司给开发都是IAM user 的账户, 没有root 账户
计算网络: 

操作系统:

数据结构:

区块链:
    密码学
         RSA --> 不可逆转 
         DH    

AWS

