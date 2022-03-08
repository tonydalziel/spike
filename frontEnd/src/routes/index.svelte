<!-- Should redirect depending on whether we are logging in
Currently just using it as the login page though -->
<!--Using h-screen may cause issues with mobile device implementation-->
<script>
  import MainLogin from '../components/loginPage/mainLogin.svelte';
  import Register from '../components/loginPage/register.svelte';
  import {goto} from '$app/navigation';
  import {browser} from "$app/env";
  import {user} from '../stores/user';

  let register = false;
  let registered = false;

  function openReports(){
    if(browser){
      goto('/reports');
    }
  }

  //Should verify the user here using the token provided
  if($user !== null && $user !== "null"){
    openReports()
  }
</script>

{#if registered}
  <h1 class="font-sans text-xl text-blue-400 text-center mb-2">You have succesfully registered, login below:</h1>
{/if}
<!--TODO: Should be wrapped in a flex div rather than each element to save on storage-->
{#if !register}
  <MainLogin on:signedIn={openReports} on:register={()=>{register=true}}></MainLogin>
{:else}
  <Register on:registered={()=>{register=false; registered = true;}}></Register>
{/if}