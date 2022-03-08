<script>
    import { page } from '$app/stores';
    import {user} from "../stores/user";
    import { goto } from '$app/navigation';

    function logout(){
        $user = null;
        goto('/');
    }
</script>

<nav class="flex justify-around w-100 mx-20 mb-10 text-center">

    <a class="basis-1/3 {$page.url.pathname ==="/makeAReport"? 'text-sky-900 font-bold text-4xl': 'text-gray-600/75 text-lg'}" href="/makeAReport">Make A Report</a>
    <a class="basis-1/3 {$page.url.pathname==="/reports"? 'text-sky-900 font-bold text-4xl': 'text-gray-600/75 text-lg'}" href="/reports">Reports</a>
    {#if ($user != "null") && ($user != null)}
        <h3 class="cursor-pointer basis-1/3 text-gray-600/75 text-lg" on:click={logout}>Logout</h3>
    {:else}
        <a class="basis-1/3 {$page.url.pathname==="/"? 'text-sky-900 font-bold text-4xl': 'text-gray-600/75 text-lg'}" href="/">Login</a>
    {/if}
</nav>