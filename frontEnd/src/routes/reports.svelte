<script>
    import {tempReports} from '../stores/reportStore';
    import ReportCard from '../components/report.svelte';
    //Should return a list from a store of all the reports currently on the server to then render to the events page
    //Make further calls when required
    //Add a search bar to this function
    let displayedReports = $tempReports;
    let search;
    $: {
        if(search && search != ""){
            displayedReports = $tempReports.filter(element => element.name.toUpperCase().includes(search.toUpperCase()));
        }else{
            displayedReports = $tempReports;
        }
    }
</script>

<!--Would like to sort the reports cards out based on severity-->
<div class="flex justify-center">
    <input bind:value={search} class="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none" placeholder="Search">
</div>
<div class="py-4 w-4/5 mx-auto grid gap-4 md:grid-cols-2 grid-cols-1">
    {#each displayedReports as report}
        <!--Could be made more efficient by altering the tempReports object-->
        <ReportCard reports={report.reports} name={report.name} lastReport={report.lastReport} severity={report.severity} photoID={report.photoID}></ReportCard>
    {/each}
</div>