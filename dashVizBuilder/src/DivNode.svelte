<script lang="ts">
  import { Handle, Position } from '@xyflow/svelte'; 
  export let data: { id: string };

</script>
 
<div class="divSetup">

  <div class="output">
    div id: <strong>{data.id}</strong>
  </div>

  <div class="handle-container">
    <Handle id="children" type="target" position={Position.Left} />
    <div class="onHoverText">children</div>
  </div>

  <div class="handle-container">
    <Handle id="children" type="source" position={Position.Right} />
    <div class="onHoverText">children</div>
  </div>

</div>
 
<style>
  .divSetup {
    position: absolute;
    padding: 1rem;
    border: 1px solid #00aeff;
    border-radius: 10px;
    font-size: 0.9rem;
    background: white;
  }

  .handle-container {
    position: relative;
    display: flex;
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