<script lang="ts">
    import { Handle, Position } from '@xyflow/svelte';  
    export let data: { id: string };
</script>
 
<div class="callbackSetup">

  <div>
    callback id: <strong>{data.id}</strong>
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
    position: absolute;
    padding: 1rem;
    border: 1px solid #00aeff;
    border-radius: 10px;
    font-size: 0.9rem;
    background: white;
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