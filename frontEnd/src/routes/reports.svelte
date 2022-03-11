<script>
    import GridReports from '../components/gridReports.svelte';
    import {onMount} from 'svelte';
    import MapView from '../components/mapView.svelte';
    //Should return a list from a store of all the reports currently on the server to then render to the events page
    let mapReady;
    onMount(()=>{
        window.initMap = function ready() {
            mapReady = true;
        }
    });
    
    let search;
    let mapView = false;
</script>

<div class="flex justify-around mx-12 md:w-1/2 md:mx-auto">
    <input bind:value={search} class="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none" placeholder="Search">
    <button on:click={()=> mapView = !mapView} class="rounded-full px-5 border-2 {mapView?'bg-teal-700 text-white':'bg-white text-black'} border-teal-700">
        {#if mapView}
            Grid View
            
        {:else}
            Map View
        {/if}
    </button>
</div>
{#if mapView}
    <MapView ready={mapReady}></MapView>
    <!-- <MapReports ></MapReports> -->
{:else}
    <GridReports {search}></GridReports>
{/if}