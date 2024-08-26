<script lang="ts">
  import { Handle, Position, type NodeProps } from '@xyflow/svelte';
  import type { Writable } from 'svelte/store';
 
  type $$Props = NodeProps;
 
</script>
 
<div class="displaySetup">

  <div>
    DisplayArea
  </div>

  <div class="handle-container">
    <Handle type="target" position={Position.Left} />
    <div class="onHoverText">input</div>
  </div>

</div>
 
<style>
  .displaySetup {
    padding: 0.5rem;
    background: #eee;
    border-radius: 0.125rem;
    font-size: 0.7rem;
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