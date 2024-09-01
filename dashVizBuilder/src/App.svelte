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
import DivNode from './DivNode.svelte';
import SaveJsonButton from './SaveJsonButton.svelte';
import InputNode from './InputNode.svelte';

const nodeTypes = {
    'button': ButtonNode,
    'callback': CallbackNode,
    'div': DivNode,
    'input': InputNode,
};

const nodes = writable < Node[] > ([]);
const edges = writable < Edge[] > ([]);

let menu: {
    id: string;top ? : number;left ? : number;right ? : number;bottom ? : number
} | null;
let width: number;
let height: number;

let instance;
let selectedNode = writable<string | null>(null);

// Function to add a new node
function addButtonNode() {
    nodes.update((n) => {
        const newNodeId = `button${(n.length+1)}`
        var newNode: Node = {
            id: newNodeId,
            type: 'button',
            data: {
                id: `button${(n.length+1)}`,
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
        const newCallbackNodeId = `callback${(n.length+1)}`
        const newNode: Node = {
            id: newCallbackNodeId,
            type: 'callback',
            data: {
                id: `callback${(n.length+1)}`
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
                    id:`Graph${(n.length+1)}`
                },
                position: {
                    x: Math.random() * 200,
                    y: Math.random() * 200
                },
            };
            return [...n, newNode];
    });
}

function addInputNode() {
    nodes.update((n) => {
            const newNodeId = `Input${(n.length+1)}`
            const newNode: Node = {
                id: newNodeId,
                type: 'input',
                data: {
                    id: `Input${(n.length+1)}`,
                    type: "text"
                },
                position: {
                    x: Math.random() * 200,
                    y: Math.random() * 200
                },
            };
            return [...n, newNode];
    });
}


function addDivNode() {
    nodes.update((n) => {
        const newNodeId = `Div${(n.length+1)}`
        const newNode: Node = {
            id: newNodeId,
            type: 'div',
            data: {
                id:`Div${(n.length+1)}`
            },
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

function handleNodeClick({ detail: { node } }) {
    // Extract the data from the clicked node and set it to be displayed
    selectedNode.set(node);
}

function handleInputChange(key: string, value: string) {
    // Update the selected node's data when input changes
    selectedNode.update((node) => {
        if (node) {
            node.data[key] = value;
            // Update the nodes store with the modified node data
            nodes.update((n) =>
                n.map((nd) => (nd.id === node.id ? { ...nd, data: { ...node.data } } : nd))
            );
        }
        return node;
    });
}


</script>

<div style="height:100vh;" bind:clientWidth={width} bind:clientHeight={height}>

    <SvelteFlowProvider>
        <button on:click={addButtonNode}>Add Button Node</button>
        <button on:click={addCallbackNode}>Add Callback Node</button>
        <button on:click={addGraphNode}>Add Graph Node</button>
        <button on:click={addDivNode}>Add Div Node</button>
        <button on:click={addInputNode}>Add Input Node</button>

        <div class="nodeEditor">
            {#if $selectedNode}
                <p>{$selectedNode.id}</p>
                {#each Object.entries($selectedNode.data) as [key, value]}
                    <div class="inputGroup">
                        <label for={key}>{key}:</label>
                        <input
                            id={key}
                            type="text"
                            value={value}
                            on:input={(e) => handleInputChange(key, e.target.value)}
                        />
                    </div>
                {/each}
            {:else}
                display some text for now
            {/if}
        </div>



        <SaveJsonButton />
        <SvelteFlow
        {nodeTypes}
        {nodes}
        {edges}
        on:nodecontextmenu={handleContextMenu}
        on:paneclick={handlePaneClick}
        on:nodeclick={handleNodeClick}
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

<style>
    .nodeEditor {
        margin-top: 20px;
        padding: 10px;
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        z-index: 999;
    }

    .inputGroup {
        margin-bottom: 10px;
    }

    .inputGroup label {
        margin-right: 10px;
        font-weight: bold;
    }
</style>