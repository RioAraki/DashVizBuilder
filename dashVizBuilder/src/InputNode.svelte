<script lang="ts">
  import { Handle, Position, type NodeProps } from '@xyflow/svelte';
  import { writable, type Writable } from 'svelte/store';

  type $$Props = NodeProps;
 
  export let data: { inputName: Writable<string>, inputType: Writable<string> };
  const { inputName } = data;


  const options = ['String','Number'];

  let curInput = 'String';
  function handleChange(event) {
    curInput = event.target.value;
    data.inputType.set(curInput)
    console.log(curInput)
  }


</script>
 
<div class="InputSetup">
  <div>
    Input Name: <strong>{$inputName}</strong>
  </div>

  <input
    class="nodrag"
    type="text"
    on:input={(evt) => data.inputName.set(evt.target?.value)}
  />

  <div class="input-type">
    <label for="dropdown">Input Type:</label>
    <select id="dropdown" on:change={handleChange} bind:value={curInput}>
      {#each options as option}
        <option value={option} selected={option === 'String'}>{option}</option>
      {/each}
    </select>
  </div>

  <div class="handle-container">
    <Handle type="target" position={Position.Left} />
    <div class="onHoverText">Source</div>
  </div>
</div>
 
<style>
  .InputSetup {
    padding: 0.5rem;
    background: #eee;
    border-radius: 0.125rem;
    font-size: 0.7rem;
  }

  .handle-container {
    position: relative;
    display: flex;
  }

  .onHoverText {
    visibility: hidden;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 4px;
    padding: 0.25rem;
    position: absolute;
    z-index: 1;
    bottom: 125%;
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

  select {
    margin-top: 0.5rem;
    font-size: 0.7rem;
  }
</style>
