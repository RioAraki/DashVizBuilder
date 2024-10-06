<script lang="ts">
    import { Handle, Position, NodeResizer, type NodeProps, } from '@xyflow/svelte';
    import { nodes } from './Stores';

    export let data: { id: string };

    type $$Props = NodeProps;
    export let selected: $$Props['selected'] = undefined;
    export let nodeWidth: $$Props['width'] = undefined;
    export let nodeHeight: $$Props['height'] = undefined;

    const handleResizeEnd = (event, params) => {
        console.log("onResizeEnd");
        console.log(params);
        let adjustW = Math.round(params.width / 50) * 50;
        let adjustH =  Math.round(params.height / 50) * 50;

        nodes.update((n) => {
            return n.map((node) =>
                node.id === data.id
                    ? { ...node, width: adjustW, height: adjustH }
                    : node
            );
        });

    };

</script>
 
<NodeResizer 
    minWidth={100} 
    minHeight={50}
    isVisible={selected} 
    color="rgb(255, 64, 0)" 
    onResizeEnd={handleResizeEnd}
/>
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
        padding: 1rem;
        font-size: 0.9rem;
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