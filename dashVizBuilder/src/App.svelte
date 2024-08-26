<script lang="ts">
import {
    writable
} from 'svelte/store';
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
import ContextMenu from './ContextMenu.svelte';
import DisplayNode from './DisplayNode.svelte';
import SaveJsonButton from './saveJsonButton.svelte';

const nodeTypes = {
    'button': ButtonNode,
    'callback': CallbackNode,
    'display': DisplayNode,
};

const nodes = writable < Node[] > ([]);
const edges = writable < Edge[] > ([]);

let menu: {
    id: string;top ? : number;left ? : number;right ? : number;bottom ? : number
} | null;
let width: number;
let height: number;

let instance;

// Function to add a new node
function addButtonNode() {
    nodes.update((n) => {
        const newNodeId = `Button${(n.length+1)}`
        const newNode: Node = {
            id: newNodeId,
            type: 'button',
            data: {
                buttonName: writable("")
            },
            position: {
                x: Math.random() * 200,
                y: Math.random() * 200
            },
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
            data: {
                callbackName: writable("")
            },
            position: {
                x: Math.random() * 200,
                y: Math.random() * 200
            },
        };
        return [...n, newNode];
    });
}

function addGraphNode() {
    nodes.update((n) => {
            const newNodeId = `Graph${(n.length+1)}`
            const newNode: Node = {
                id: newNodeId,
                data: {
                    label: `${newNodeId}`
                },
                position: {
                    x: Math.random() * 200,
                    y: Math.random() * 200
                },
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
            position: {
                x: Math.random() * 200,
                y: Math.random() * 200
            },
        };
        return [...n, newNode];
    });
}



function handleContextMenu({ detail: { event, node } }) {
    // Prevent native context menu from showing
    event.preventDefault();

    // Calculate position of the context menu. We want to make sure it
    // doesn't get positioned off-screen.



    menu = {
    id: node.id,
    top: event.clientY < height - 200 ? event.clientY : undefined,
    left: event.clientX < width - 200 ? event.clientX : undefined,
    right: event.clientX >= width - 200 ? width - event.clientX : undefined,
    bottom: event.clientY >= height - 200 ? height - event.clientY : undefined
    };
    console.log("menu?", menu)
}

// Close the context menu if it's open whenever the window is clicked.
function handlePaneClick() {
    menu = null;
}

</script>

<div style="height:80vh;" bind:clientWidth={width} bind:clientHeight={height}>

    <SvelteFlowProvider>
        <button on:click={addButtonNode}>Add Button Node</button>
        <button on:click={addCallbackNode}>Add Callback Node</button>
        <button on:click={addGraphNode}>Add Graph Node</button>
        <button on:click={addDisplayNode}>Add Text Dsiplay Node</button>
        <SaveJsonButton />
        <SvelteFlow
            {nodeTypes}
            {nodes}
            {edges}
            on:nodecontextmenu={handleContextMenu}
            on:paneclick={handlePaneClick}
            fitView
            bind:this={instance}>
            <Controls />
            <Background />
            {#if menu}
                <ContextMenu
                    onClick={handlePaneClick}
                    id={menu.id}
                    top={menu.top}
                    left={menu.left}
                    right={menu.right}
                    bottom={menu.bottom}
                />
            {/if}
            <MiniMap />
        </SvelteFlow>
    </SvelteFlowProvider>
</div>
