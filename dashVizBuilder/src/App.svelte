<script lang="ts">
  import { writable } from 'svelte/store';
  import {
    SvelteFlow,
    SvelteFlowProvider,
    useSvelteFlow,
    Controls,
    Background,
    MiniMap,
    type Node,
    type Edge,
  } from '@xyflow/svelte';

  import '@xyflow/svelte/dist/style.css';

  import ButtonNode from './ButtonNode.svelte';
  import CallbackNode from './CallbackNode.svelte';
  import DisplayNode from './DisplayNode.svelte';
  import SaveJsonButton from './saveJsonButton.svelte';

  const nodeTypes = {
    'button': ButtonNode,
    'callback': CallbackNode,
    'display': DisplayNode,
  };

  const nodes = writable<Node[]>([]);
  const edges = writable<Edge[]>([]);
  let instance;

  // Function to add a new node
  function addButtonNode() {
    nodes.update((n) => {
      const newNodeId = `Button${(n.length+1)}`
      const newNode: Node = {
        id: newNodeId,
        type: 'button',
        data: {  buttonName: writable("") },
        position: { x: Math.random() * 200, y: Math.random() * 200 }, 
      };
      return [...n, newNode];
    });
  }

  function addCallbackNode() {
    nodes.update((n) => {
      const newCallbackNodeId = `Callback${(n.length+1)}`
      const newNode: Node = {
        id: newCallbackNodeId,
        type: 'callback',
        data: { callbackName: writable("") },
        position: { x: Math.random() * 200, y: Math.random() * 200 },
      };
      return [...n, newNode];
    });
  }

  function addGraphNode() {
    nodes.update((n) => {
      const newNodeId = `Graph${(n.length+1)}`
      const newNode: Node = {
        id: newNodeId,
        data: { label: `${newNodeId}` },
        position: { x: Math.random() * 200, y: Math.random() * 200 },
      };
      return [...n, newNode];
    });
  }

  function addDisplayNode() {
    nodes.update((n) => {
      const newNodeId = `DisplayArea${(n.length+1)}`
      const newNode: Node = {
        id: newNodeId,
        type: 'display',
        data: {},
        position: { x: Math.random() * 200, y: Math.random() * 200 },
      };
      return [...n, newNode];
    });
  }



</script>

<div style="height:80vh">
  <button on:click={addButtonNode}>Add Button Node</button>
  <button on:click={addCallbackNode}>Add Callback Node</button>
  <button on:click={addGraphNode}>Add Graph Node</button>
  <button on:click={addDisplayNode}>Add Text Dsiplay Node</button>
  
  <SvelteFlowProvider>
    <SaveJsonButton />

    <SvelteFlow  {nodeTypes} {nodes} {edges} fitView  bind:this={instance}>
      <Controls />
      <Background />
      <MiniMap />
    </SvelteFlow>
  </SvelteFlowProvider>

</div>