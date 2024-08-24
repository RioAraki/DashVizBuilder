<script lang="ts">
  import { Handle, Position, type NodeProps } from '@xyflow/svelte';
  import type { Writable } from 'svelte/store';
 
  type $$Props = NodeProps;
 
  export let data: { buttonName: Writable<string> };
 
  const { buttonName } = data;
</script>
 
<div class="buttonSetup">

  <div>
    Button Name: <strong>{$buttonName}</strong>
  </div>

  <input
    class="nodrag"
    type="text"
    on:input={(evt) => data.buttonName.set(evt.target?.value)}
  />

  <div class="handle-container">
    <Handle type="source" position={Position.Right} />
    <div class="onHoverText">n_click</div>
  </div>

</div>
 
<style>
  .buttonSetup {
    padding: 0.5rem;
    background: #eee;
    border-radius: 0.125rem;
    font-size: 0.7rem;
  }

  .handle-container {
    position: relative;
    display: flex;
  }

  .handle-container:last-child {
  }

  /*TODO: connector placement is a bit misaligned */
  .onHoverText {
    visibility: hidden;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 4px;
    padding: 0.25rem;
    position: absolute;
    z-index: 1;
    bottom: 125%; /* Position above the handle */
    left: 90%;
    transform: translateX(-50%);
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 0.6rem;
    white-space: nowrap;
  }

  .handle-container:hover .onHoverText {
    visibility: visible;
    opacity: 1;
  }

</style>