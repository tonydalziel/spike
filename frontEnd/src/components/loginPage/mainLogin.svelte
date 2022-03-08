<script>
  import {user} from "../../stores/user.js";
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  let currentUsername;
  let currentPassword;
  let invalidUsername =false;
  let invalidPassword =false;
  let invalidAttempt = false;
  
  //Check validity and attempt to sign in -> pass a message saying logged in
  function register(){
    dispatch('register');
  }

  async function signIn(){
    invalidAttempt = false;
    if(typeof currentUsername == "undefined" || currentUsername == "" ){
      invalidUsername = true;
    }else{
      invalidUsername = false;
    }
    if(typeof currentPassword == "undefined" || currentPassword == ""){
      invalidPassword = true;
    }else{
      invalidPassword = false;
    }

    if((!(invalidPassword))&&(!(invalidUsername))){
      const res = await fetch(`http://127.0.0.1:8090/login?username=${currentUsername}&password=${currentPassword}`);
      const data = await res.json();
      if(data.valid){
        $user = {username: data.username, lastReport: data.lastReport};
        dispatch('signedIn');
      }else{
        invalidAttempt = true;
      }
    }
  }
</script>

<div class="flex justify-center items-center h-screen px-4">
    <div class="grow max-w-xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        {#if invalidAttempt}
          <p class="text-red-500 text-md italic text-center">Invalid Login Attempt</p>
        {/if}
        <div class="mb-4">
          <label class="block text-grey-darker text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input bind:value={currentUsername} class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker mb-3" id="username" type="text" placeholder="Username">
          {#if invalidUsername}
            <p class="text-red-500 text-xs italic">Please input a username.</p>
          {/if}
        </div>
        <div class="mb-6">
          <label class="block text-grey-darker text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input bind:value={currentPassword} class="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" id="password" type="password" placeholder="******************">
          {#if invalidPassword}
            <p class="text-red-500 text-xs italic">Please input a password.</p>
          {/if}
        </div>
        <div class="flex items-center justify-between">
          <button on:click={signIn} class="bg-blue hover:bg-blue-dark text-black font-bold py-2 px-4 rounded" type="button">
            Sign In
          </button>
          <button class="inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker" on:click={register}>
            Register an account
          </button>
        </div>
        <!-- <div class="flex items-center justify-center">
            <a class="font-bold text-sm text-blue hover:text-blue-darker" href="/">
                Register an account
            </a>
        </div> -->
    </div>
</div>