<script lang="ts">
    import { Handle, Position } from '@xyflow/svelte';
    export let data: { id: string };
</script>
 
<div class="buttonSetup">

    <div>
        button id: <strong>{data.id}</strong>
        <div class="connector">
            <Handle id="n_clicks" type="source" position={Position.Right} />
            <div class="onHoverText">n_clicks</div>
        </div>
    </div>

</div>
 
<style>
    .buttonSetup {
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

    .connector:hover .onHoverText {
        visibility: visible;
        opacity: 1;
    }

</style>