<script lang="ts">
    import { useSvelteFlow } from '@xyflow/svelte';
  
    const { toObject } = useSvelteFlow();
      useSvelteFlow();


    function saveJson() {
        let flowData = toObject();
        const jsonString = JSON.stringify(flowData);
        const blob = new Blob([jsonString], { type: 'application/json' });

        console.log(blob)
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'svelte-flow-graph.json';
        a.click();
        URL.revokeObjectURL(url);
    } 


</script>

<button on:click={saveJson}> Save as Json</button>
