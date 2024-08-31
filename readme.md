# dashVizBuilder

## Stage 1: 找一个 node/edge 的 graph库，用户可以轻松画图并保存。
具体来说：
1. drag and drop 新的 node 进 canvas，node本身可以吸附式移动，node可以吸附式调节大小，node和node之间通过edge相连。
2. 自定义几种预设的 node，比如 button，input，callback，每一种node都有各种child，child之间可以互相连接
3. 可以导出 canvas 里 node 的位置和连接情况，serialization and deserialization

目标：有一个完整的project，用户可以 drag and drop一些ui组件进去，按照自己想要的方式做layout，连接不同组件的children，最后按照一些格式输出

### 实践与观察

市面上有非常多的 graph node 的前端库，但基本都局限于用代码把 graph 和 node 画出来，也就是#2，目前 #1 和 #3 可能是比较打的挑战。原理上来说画出图之后肯定希望有方法保存，所以感觉 #3 被实现过的概率更大，而 #1 可能比较难了。

方向：
1. dash studio （现成方案）
2. 改造比如 SVELVET 或者 rete.js 或者 Svelte flow

无论如何为了适应技术栈应该学习一下 SVELTE 怎么写

### Svelte Flow

1. [这个来自 react flow 的demo 应该可以套用](https://codesandbox.io/p/sandbox/react-flow-add-node-button-l9rcu)
2. This is the whole point of the library
3. https://svelteflow.dev/api-reference/hooks/use-svelte-flow

感觉理论上这个方案是行得通的。

## Milestone of Stage 1
1. Drag and drop Add node, 可以先用目前的 button 代替
2. Node editing, 可以 in place edit，但之后要调整的东西多难免要放到右侧，edit的内容要能够被记录

## Stage 2: 根据graph的输出，code gen 出 dash 代码

1. 根据输出的内容输出dash的layout，放入empty callback



## 工作记录

### 2024-08-24

用一天时间初步用 Svelte 实现了用按钮加node，自定义各种node，以及导出成json。目前看来技术方案基本敲定了，每个大流程都能跑通，接下来还有些问题要克服：
    1. callback generates new HTML (无法直接建出所有的 html 节点)。
    2. 多个源头都指向input/output。
    3. node的位置表示其最后在UI里的真实位置。

总的来说今天突破的难关比我想得多，对进程是比较满意的。

### 2024-08-26

实现了右键 delete node