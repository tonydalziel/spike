<script>
	import Map from './Map.svelte';
	export let ready = false;
</script>

<svelte:head>
	<script defer async
	src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCtWIpiuuBPIArwGIgdwI6kCFH5xr18K1w&callback=initMap&libraries=visualization">
	</script>
</svelte:head>

{ #if ready }
<Map></Map>
{ /if }