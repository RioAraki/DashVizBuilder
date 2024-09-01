<script lang="ts">
    import { Handle, Position } from '@xyflow/svelte';
    export let data: { id: string, type: string };
</script>
 
<div class="inputSetup">
    <div>
        <p>
            input id: <strong>{data.id}</strong>
            <br/>
            type: {data.type}
        </p>
    </div>
    
    <div class="handle-container">
        <Handle id="value" type="source" position={Position.Right} />
        <div class="onHoverText">value</div>
    </div>
</div>
 
<style>
    .inputSetup {
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
</style>
