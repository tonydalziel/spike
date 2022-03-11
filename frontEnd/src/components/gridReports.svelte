<script>
    import {tempReports} from '../stores/reportStore';
    import ReportCard from '../components/report.svelte';
    let displayedReports = $tempReports;
    export let search;
    $: {
        if(search && search != ""){
            displayedReports = $tempReports.filter(element => element.name.toUpperCase().includes(search.toUpperCase()));
        }else{
            displayedReports = $tempReports;
        }
    }
</script>

<div class="py-4 w-4/5 mx-auto grid gap-4 md:grid-cols-2 grid-cols-1">
    {#each displayedReports as report}
        <!--Could be made more efficient by altering the tempReports object-->
        <ReportCard reports={report.reports} name={report.name} lastReport={report.lastReport} severity={report.severity} photoID={report.photoID}></ReportCard>
    {/each}
</div>