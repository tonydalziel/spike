<script>
	import Map from './Map.svelte';
	import { placesKey } from '../stores/apiKey';
	export let ready = false;
</script>

<svelte:head>
	{#if !ready}
		<script defer async
		src= "https://maps.googleapis.com/maps/api/js?key={placesKey}&callback=initMap&libraries=visualization">
		</script>
	{/if}
</svelte:head>

{ #if ready }
<Map></Map>
{ /if }