<script>
    import mapStyles from './mapStyle.js'; // optional
    import {tempReports} from '../stores/reportStore';

    let container;
    let map;
    const durham = { lat: 54.774, lng: -1.576 };

    import { onMount } from 'svelte';

    onMount(async () => {
        map = new google.maps.Map(container, {
            zoom: 15,
            center: durham,
            styles: mapStyles,
            scrollwheel: false,
            navigationControl: false,
            streetViewControl: false,
            mapTypeControl: false
        });
        let heatmapData = []
        $tempReports.forEach((report)=>{
            if(report.lat && report.lng && report.reports && report.reports > 0 ){
                heatmapData.push({location: new google.maps.LatLng(report.lat, report.lng), weight: report.reports})
            }
        });
        var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData,
        radius: 0.001,
        dissipating: false
        });
        heatmap.setMap(map);
    });
</script>


<div class="w-100 md:w-8/12 mx-auto md:h-96 h-screen mb:mt-36 mt-8" bind:this={container}></div>