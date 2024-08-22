# Milestones

## 找一个前端库可以支持：
1. drag and drop 新的 node 进 canvas，node本身可以吸附式移动，node可以吸附式调节大小
2. 自定义几种预设的 node，比如 button，input，callback，每一种node都有各种child，child之间可以互相连接
3. 可以导出 canvas 里 node 的位置和连接情况
目标：有一个完整的project，用户可以 drag and drop一些ui组件进去，按照自己想要的方式做layout，连接不同组件的children，最后按照一些格式输出

### 实践与观察

市面上有非常多的 graph node 的前端库，但基本都局限于用代码把 graph 和 node 画出来，也就是#2，目前 #1 和 #3 可能是比较打的挑战。原理上来说画出图之后肯定希望有方法保存，所以感觉 #3 被实现过的概率更大，而 #1 可能比较难了。

方向：
1. dash studio （现成方案）
2. 改造比如 SVELVET 或者 rete.js

无论如何为了适应技术栈应该学习一下 SVELTE 怎么写


## 根据输出的内容输出 dash 代码
1. 根据输出的内容输出dash的layout，放入empty callback
