<script lang="ts">
    import { Handle, Position } from '@xyflow/svelte';  
    export let data: { callbackName: string };
</script>
 
<div class="callbackSetup">

  <div>
    Callback Name: <strong>{data.callbackName}</strong>
  </div>

  <div class="handle-container">
    <Handle id="input" type="target" position={Position.Left} />
    <div class="onHoverText">input</div>
  </div>  
  
  <div class="handle-container">
    <Handle id="state" type="target" position={Position.Top} />
    <div class="onHoverText">state</div>
  </div>

  <div class="handle-container">
    <Handle id="output" type="source" position={Position.Right} />
    <div class="onHoverText">output</div>
  </div>

</div>
 
<style>
  .callbackSetup {
    padding: 0.5rem;
    background: #eee;
    border-radius: 0.125rem;
    font-size: 0.7rem;
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