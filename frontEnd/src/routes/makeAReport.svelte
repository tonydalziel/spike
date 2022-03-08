<script>
    import {user} from '../stores/user';
    import { onMount } from 'svelte';
    
    let locationName;
    let promise = Promise.resolve([]);
    const minDate = new Date(Date.now() - 2*24*60*60*1000);
    let min = minDate.toISOString().split(':').slice(0,2).join(':');
    const max = new Date(Date.now()).toISOString().split(':').slice(0,2).join(':');
    let time = max;
    let invalidTime = false;
    let reportMade = false; //Can just use the timeSince variable below
    $: timeSince = Date.now() - ($user !== null && $user !== "null"? parseInt($user.lastReport) : 24*60*60*1000)
    setInterval(async () => {
        timeSince = Date.now() - ($user !== null && $user !== "null"? parseInt($user.lastReport) : 24*60*60*1000)
    }, 5000);

    onMount(()=>{
        async function getLocations(){
            const res = await fetch('http://127.0.0.1:8090/locations');
            return res.json();
        }
        promise = getLocations();
    });

    async function makeReport(){
        console.log("click");
        //Ensure locations have loaded and user inputs are valid before advancing
        if($user !== "null" && $user !== null && typeof locationName != 'undefined' && locationName != "waiting"){
            //Add a check to ensure a valid location has been selected -> If not display the appropriate message
            if(!document.getElementById('time').checkValidity()){
                invalidTime = true;
            }else{
                invalidTime = false;
                const res = await fetch(`http://127.0.0.1:8090/makeReport?username=${$user.username}&name=${locationName}`);
                if(res.ok){
                    reportMade = true;
                    $user.lastReport = Date.now();
                }
                //Should blur the report box and display the sign saying report has been successful -> Add checks for all requests
            }
        }
    }
</script>

{#if reportMade}
    <h1 class="text-xl text-center font-sans font-bold text-red-400">You have successfully made a report</h1>
{/if}
<!--Want to display a message preventing users from clikcing twice-->
<div class="flex justify-center items-center h-screen px-4 {timeSince < 30*60*1000? "blur-sm": "blur-none"}">
    <div class="grow max-w-xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        {#if $user === "null" || $user === null}
          <p class="text-red-500 text-md italic text-center">You must be logged in to make a report</p>
        {/if}
        <div class="mb-4">
            <label class="block text-grey-darker text-sm font-bold mb-2" for="location">
            Location
            </label>
            <select disabled={timeSince < 30*60*1000} bind:value={locationName} id="Location" class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker">
                <option value="waiting">Please select a location</option>
                {#await promise}
                    <option value="waiting">...waiting</option>
                {:then locations}
                    {#each locations as location}
                      <option value={location}>{location}</option>
                    {/each}
                {:catch error}
                    <option>Error loading location names</option>
                {/await}
            </select>
        </div>
        {#if locationName && locationName == "waiting"}
          <p class="text-red-500 text-xs italic text-center">Ensure you have selected a location</p>
        {/if}
        <div class="mb-6">
          <label class="block text-grey-darker text-sm font-bold mb-2" for="time">
            Time of incident
          </label>
          <!--Show message ensuring it was within a given time frame-->
          <input {min} {max} disabled={timeSince < 30*60*1000} bind:value={time} class="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" id="time" type="datetime-local">
        </div>
        {#if invalidTime}
          <p class="text-red-500 text-xs italic text-center">Ensure the report is from within the last 48 hours</p>
        {/if}
        <!--Disable if waiting for a promise or if timeout-->
        <button disabled={timeSince < 30*60*1000} class="bg-blue hover:bg-blue-dark text-black font-bold py-2 px-4 rounded" type="button" on:click={makeReport}>
            Report
        </button>
    </div>
</div>